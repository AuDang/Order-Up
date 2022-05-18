from flask import Flask
from .config import Configuration
from .routes import orders
from .models import db
from flask_login import LoginManager
from .models import db, Employee

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
db.init_app(app)

login= LoginManager(app)
login.loggin_view = "session.login"

@login.user_loader
def load_user(id):
   return Employee.query.get(int(id))