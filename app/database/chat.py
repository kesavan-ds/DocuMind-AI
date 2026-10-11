from sqlalchemy.orm import Session

from app.database.models import Message


def save_message(
    db: Session,
    session_id: str,
    role: str,
    content: str
):

    message = Message(
        session_id=session_id,
        role=role,
        content=content
    )

    db.add(message)
    db.commit()

    return message

def get_messages(
    db: Session,
    session_id: str):

    return (db.query(Message).filter(Message.session_id == session_id).order_by(Message.created_at.asc()).all())

def get_history(
    db: Session,
    session_id: str
):

    messages = get_messages(
        db,
        session_id
    )

    history = ""

    for message in messages:

        if message.role == "user":
            history += f"User: {message.content}\n"

        else:
            history += f"Assistant: {message.content}\n"

    return history