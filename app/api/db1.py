from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extension import db

app_bp = Blueprint('app', __name__)

@app_bp.route("/upgrade-db")
def upgrade_db():
    try:
        db.session.execute(text("""
            ALTER TABLE IF EXISTS commande
            ALTER COLUMN created_at
            TYPE TIMESTAMP
            USING created_at::timestamp;
        """))

        db.session.execute(text("""
            ALTER TABLE IF EXISTS cout
            ALTER COLUMN created_at
            TYPE TIMESTAMP
            USING created_at::timestamp;
        """))

        db.session.commit()
        return jsonify({"upgraded": True})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500