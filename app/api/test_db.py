from flask import jsonify,Blueprint
from app.extension import db  # ton objet SQLAlchemy

db_bp = Blueprint("db_bp", __name__)

@db_bp.route("/test-db")
def test_db():
    try:
        # Crée une connexion avec le context manager
        with db.engine.connect() as conn:
            result = conn.execute("SELECT 1")
            first = result.scalar()  # récupère la première valeur
        return jsonify({"db_connected": True, "result": first})
    except Exception as e:
        return jsonify({"db_connected": False, "error": str(e)})