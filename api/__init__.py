from flask import Flask
import os
from api.views import books_view
from api.views import users_view

app = Flask(__name__)

app_settings = os.getenv(
    'APPSETTINGS'
    'api.config.DevelopmentConfig'
)

print(app_settings)
app.config.from_object(app_settings)

#register blueprints
app.register_blueprint(books_view.books_bt, url_prefix='/api/v1')
app.register_blueprint(users_view.users_bt, url_prefix='/api/v1')