from flask import Flask, jsonify,Blueprint
from app.extension import db  # ton import SQLAlchemy


db_bp = Blueprint('db_bp', __name__)
@db_bp.route("/test-db")
def test_db():
    try:
        # Simple requête pour tester la connexion
        result = db.engine.execute("SELECT 1").fetchone()
        return jsonify({"db_connected": True, "result": result[0]})
    except Exception as e:
        return jsonify({"db_connected": False, "error": str(e)})