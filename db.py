from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine("postgresql://postgres:postgrespw@localhost:55000", echo=True, future=True)


class Foo(Base):
    __tablename__ = "foo"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Foo(id={self.id!r}, name={self.name!r})"


GENERATE_SCHEMA = False

if GENERATE_SCHEMA:
    print("INFO: Generating schema...")
    Base.metadata.create_all(engine)
