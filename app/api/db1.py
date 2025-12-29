from sqlalchemy import text
from flask import Blueprint
from sqlalchemy import text
from app.extension import db  # ton objet SQLAlchemy

app_bp=Blueprint('app',__name__)
@app_bp.route("/upgrade-db")
def upgrade_db():
    db.session.execute(text("""
        ALTER TABLE commande
        ALTER COLUMN created_at
        TYPE TIMESTAMP
        USING created_at::timestamp;
    """))
    db.session.commit()
    db.session.execute(text("""
        ALTER TABLE cout
        ALTER COLUMN created_at
        TYPE TIMESTAMP
        USING created_at::timestamp;
    """))
    db.session.commit()
    return {"upgraded": True}