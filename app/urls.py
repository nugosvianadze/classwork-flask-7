from app.user.views import user_bp
from app.library.views import library_bp


def register_blueprints(app) -> None:
    bps = [user_bp, library_bp]
    for bp in bps:
        print(bp)
        app.register_blueprint(bp)
