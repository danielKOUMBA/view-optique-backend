from app.models import Admin
from app import create_app
from werkzeug.security import generate_password_hash
from app.extension import db

app=create_app()
with app.app_context():
    

    admin_secondaire=Admin.query.filter_by(email='ngwepazajohndeborah@icloud.-com').first()
    admin_secondaire.email='hobryskwadjo23@gmail.com'
    db.session.add(admin_secondaire)
    db.session.commit()
    #  python -m waitress --host=0.0.0.0 --port=5000 app.wsgi:app