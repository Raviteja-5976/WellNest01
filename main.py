from flask import Flask, render_template, url_for, session
from models.authentication.auth import auth, init_session_config
from models.tests.test_view import test_view
from models.tests.test_routes import test_routes
from models.database_setup import init_db

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(test_view, url_prefix='/test')
app.register_blueprint(test_routes, url_prefix='/test')
app.secret_key = 'super_secret_key'
init_session_config(app)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    init_db()  # Initialize database tables
    app.run(debug=True)