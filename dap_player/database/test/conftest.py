import pytest
import sqlalchemy as sqla
import sqlalchemy.orm as orm

from dap_player.database.database import Base


@pytest.fixture
def session():
    engine = sqla.create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()

    yield session

    session.close()
