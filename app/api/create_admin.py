from flask import Blueprint, jsonify
from app.models.admin_table import Admin
from app.extension import db
from werkzeug.security import generate_password_hash

create_admin_bp = Blueprint('create_admin_bp', __name__)

@create_admin_bp.route('/create-admins', methods=['GET'])
def create_admins():
    try:
        admin1 = Admin(email='mabrandy91@gmail.com', password=generate_password_hash('123brandy'), role='admin suppreme')
        admin2 = Admin(email="Nguiemaurine2@gmail.com", password=generate_password_hash('123maurine'), role='admin secondaire')
        admin3=Admin(email="hobryskwadjo23@gmail.com", password=generate_password_hash('123jhons'), role='bonus admin')

        db.session.add(admin1)
        db.session.add(admin2)
        db.session.add(admin3)
        db.session.commit()

        return jsonify({'message': 'Admins created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500