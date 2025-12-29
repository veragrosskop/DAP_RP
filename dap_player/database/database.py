from contextlib import contextmanager
from datetime import datetime
import sqlalchemy as sqla
import sqlalchemy.orm as orm

# ---------- Database configuration ----------
DATABASE_URL = "sqlite:///mp3player.db"

engine = sqla.create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = orm.sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = orm.declarative_base()


# ---------- Models ----------
class Track(Base):
    __tablename__ = "tracks"

    id = sqla.Column(sqla.Integer, primary_key=True)
    filepath = sqla.Column(sqla.String, unique=True, nullable=False)

    title = sqla.Column(sqla.String)
    artist = sqla.Column(sqla.String)
    album = sqla.Column(sqla.String)

    play_count = sqla.Column(sqla.Integer, default=0)
    last_played = sqla.Column(sqla.DateTime)

    def __repr__(self):
        return f"<Track {self.artist} - {self.title}>"


class Setting(Base):
    __tablename__ = "settings"

    id = sqla.Column(sqla.Integer, primary_key=True)
    key = sqla.Column(sqla.String, unique=True, nullable=False)
    value = sqla.Column(sqla.String, nullable=False)


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


# ---------- Initialization ----------
def init_db():
    """Create all tables"""
    Base.metadata.create_all(engine)


# ---------- Convenience helpers ----------
def record_track_play(track_id: int):
    """Increment play count and update last played time"""
    with session_scope() as session:
        track = session.get(Track, track_id)
        if track:
            track.play_count += 1
            track.last_played = datetime.now()
