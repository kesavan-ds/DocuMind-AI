from app.database.connection import engine, Base
from app.database.models import Conversation, Message


def init_database():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":
    init_database()