from flask import Flask, render_template, url_for, session
from models.authentication.auth import auth, init_session_config



app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.secret_key = 'super_secret_key'
init_session_config(app)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)