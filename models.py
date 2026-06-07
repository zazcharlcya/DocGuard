import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Document(db.Model):

    __tablename__ = "document"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    text = db.Column(db.Text, nullable=False)

    type = db.Column(db.String(20), nullable=False)

    filename = db.Column(db.String(255), nullable=True)

    file_path = db.Column(db.String(500), nullable=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


class ScanResult(db.Model):

    __tablename__ = "scan_result"

    id = db.Column(db.Integer, primary_key=True)

    document_id = db.Column(
        db.String(36),
        db.ForeignKey("document.id"),
        nullable=False
    )

    emails = db.Column(db.Text)
    cards = db.Column(db.Text)
    phones = db.Column(db.Text)       # телефонные номера
    keywords = db.Column(db.Text)

    predicted_type = db.Column(
        db.String(50),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    document = db.relationship(
        "Document",
        backref=db.backref("scan_results", lazy=True)
    )
