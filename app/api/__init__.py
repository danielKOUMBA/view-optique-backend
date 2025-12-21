from app.api.login import login_bp
from app.api.modifier_password import modifier_password_bp
from app.api.refresh import refresh_bp
from app.api.commande import commande_bp
from app.api.Cout import cout_bp
from app.api.tresorerie import tresorerie_bp
from app.api.dash import dash_bp
from app.api.allcommande import allCommande_bp
from app.api.allcout import allCout_bp
from app.api.DeleteCommande import deleteCommande_bp
from app.api.delete_cout import deleteCout_bp
from app.api.updateCommande import update_bp
from app.api.test_db import db_bp


def register_bluprint(app):
    app.register_blueprint(login_bp,url_prefix='/api')
    app.register_blueprint(modifier_password_bp,url_prefix='/api')
    app.register_blueprint(refresh_bp,url_prefix='/api')
    app.register_blueprint(commande_bp,url_prefix='/api')
    app.register_blueprint(cout_bp,url_prefix='/api')
    app.register_blueprint(tresorerie_bp,url_prefix='/api')
    app.register_blueprint(dash_bp,url_prefix='/api')
    app.register_blueprint(allCommande_bp,url_prefix='/api')
    app.register_blueprint(allCout_bp,url_prefix='/api')
    app.register_blueprint(deleteCommande_bp,url_prefix='/api')
    app.register_blueprint(deleteCout_bp,url_prefix='/api')
    app.register_blueprint(update_bp,url_prefix='/api')
    app.register_blueprint(db_bp,url_prefix='/api')
 