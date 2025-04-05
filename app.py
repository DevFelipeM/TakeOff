from flask import Flask, jsonify
from config import Config
from extensions import db, ma
from extensions import db, ma, jwt

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    jwt.init_app(app) 
    
    db.init_app(app)
    ma.init_app(app)
    
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    @app.route('/')
    def home():
        return jsonify({'message': 'Registration API'})
    
    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)