from sqlalchemy import select

from app.database.connection import SessionLocal
from app.database.models import Conversation, Message


class DatabaseMemory:

    def get_history(self, session_id):

        with SessionLocal() as db:

            statement = (
                select(Message)
                .where(
                    Message.session_id == session_id
                )
                .order_by(Message.id)
            )

            messages = db.scalars(statement).all()

            history = ""

            for message in messages:

                if message.role == "user":
                    history += f"User: {message.content}\n"

                else:
                    history += (
                        f"Assistant: {message.content}\n"
                    )

            return history

    def add_message(
        self,
        session_id,
        role,
        content
    ):

        with SessionLocal() as db:

            conversation = db.scalar(
                select(Conversation)
                .where(
                    Conversation.session_id == session_id
                )
            )

            if conversation is None:

                conversation = Conversation(
                    session_id=session_id
                )

                db.add(conversation)

            message = Message(
                session_id=session_id,
                role=role,
                content=content
            )

            db.add(message)

            db.commit()