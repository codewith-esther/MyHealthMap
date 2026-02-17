from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # Import Blueprints
    from app.routes.obesity import obesity_bp
    from app.routes.heart import heart_bp

    # Register Blueprints
    app.register_blueprint(obesity_bp)  # URL will be /obesity/
    app.register_blueprint(heart_bp)    # URL will be /heart/

    # Home route
    @app.route('/')
    def home():
        return render_template('index.html')  # render your landing page

    # Optional: /index route
    @app.route('/index')
    def index():
        return render_template('index.html')

    return app
