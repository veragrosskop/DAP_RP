from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sqla
import sqlalchemy.orm as orm

# ---------- Database configuration ----------


_engine: Optional[sqla.Engine] = None

# engine creation
def get_engine(url="sqlite:///mp3player.db"):
    global _engine
    if _engine is not None:
        _engine = sqla.create_engine(
            url,
            echo=False,
            future=True,
            connect_args={"check_same_thread": False},
        )

    return _engine


@sqla.event.listens_for(sqla.Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")  # read while writing
    cursor.execute("PRAGMA synchronous=NORMAL;")
    cursor.execute("PRAGMA temp_store=MEMORY;")
    cursor.close()


def get_sessionmaker():
    return orm.sessionmaker(
    bind=get_engine(),
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# ---------- Session management ----------
@contextmanager
def session_scope():
    """
    Provide a transactional scope around a series of operations.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


Base = orm.declarative_base()

# ---------- Association Tables (Many-to-many) ----------
track_artist = sqla.Table(
    "track_artist",
    Base.metadata,
    sqla.Column("track_id", sqla.ForeignKey("tracks.id"), primary_key=True),
    sqla.Column("artist_id", sqla.ForeignKey("artists.id"), primary_key=True),
)

track_genre = sqla.Table(
    "track_genre",
    Base.metadata,
    sqla.Column("track_id", sqla.ForeignKey("tracks.id"), primary_key=True),
    sqla.Column("genre_id", sqla.ForeignKey("genres.id"), primary_key=True),
)


# ---------- Models ----------
class Artist(Base):
    __tablename__ = "artists"

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String, unique=True, nullable=False)

    albums = orm.relationship("Album", back_populates="album_artist")
    tracks = orm.relationship("Track", secondary=track_artist, back_populates="artists")


class Album(Base):
    __tablename__ = "albums"

    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column(sqla.String, nullable=False)

    album_artist_id = sqla.Column(sqla.Integer, sqla.ForeignKey("artists.id"))

    album_artist = orm.relationship("Artist", back_populates="albums")
    tracks = orm.relationship("Track", back_populates="album")


class Genre(Base):
    __tablename__ = "genres"

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String, unique=True, nullable=False)

    tracks = orm.relationship("Track", secondary=track_genre, back_populates="genres")


class PlayTimestamp(Base):
    __tablename__ = "play_timestamps"

    __table_args__ = (
        sqla.Index("ix_play_track_time", "track_id", "played_at"),
    )
    id = sqla.Column(sqla.Integer, primary_key=True)
    track_id = sqla.Column(sqla.Integer, sqla.ForeignKey("tracks.id"), nullable=False, index=True)

    played_at = sqla.Column(sqla.DateTime, nullable=False, default=datetime.now(timezone.utc), index=True)

    track = orm.relationship("Track", back_populates="play_timestamps")


class Track(Base):
    __tablename__ = "tracks"

    __table_args__ = (
        sqla.Index("ix_tracks_album_id", "album_id"),
    )

    id = sqla.Column(sqla.Integer, primary_key=True)
    filepath = sqla.Column(sqla.String, unique=True, nullable=False)

    title = sqla.Column(sqla.String, nullable=False)
    artists = orm.relationship("Artist", secondary=track_artist, back_populates="tracks")
    album_id = sqla.Column(sqla.Integer, sqla.ForeignKey("albums.id"), nullable=False, index=True)
    album = orm.relationship("Album", back_populates="tracks")
    genres = orm.relationship("Genre", secondary=track_genre, back_populates="tracks")

    sqla.Index('ix_track_album_id')

    play_count = sqla.Column(sqla.Integer, default=0)
    last_played = sqla.Column(sqla.DateTime)
    play_timestamps = orm.relationship("PlayTimestamp", back_populates="track", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Track id={self.id} title={self.title!r}>"





# ---------- Initialization ----------
def init_db():
    """Create all tables"""
    Base.metadata.create_all(_engine)

# ---------- UI ----------

def list_tracks():
    with session_scope() as session:
        tracks = (
            session.query(Track.id, Track.title)
            .order_by(Track.title)
            .limit(20)
            .offset(page * 20)
            .all()
        )
        return tracks

# ---------- Library Sync -----------

# To do!
def add_track(track):
    with session_scope() as session:

def add_artist(artist):
    with session_scope() as session:

def add_album(album):
    with session_scope() as session:


# ---------- Convenience helpers ----------
def record_track_play(track_id: int):
    """Increment play count and update last played time"""
    with session_scope() as session:
        track = session.get(Track, track_id)
        if track:
            track.play_count += 1
            track.last_played = datetime.now()


