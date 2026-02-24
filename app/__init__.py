from flask import Flask, render_template
import os

def create_app():
    # Get the absolute path to the app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    
    app = Flask(
        __name__,
        template_folder=os.path.join(app_dir, 'templates'),
        static_folder=os.path.join(app_dir, 'static'),
        static_url_path='/static'
    )

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
