"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr6hd269v5rj8a4820-a.oregon-postgres.render.com",
        database="todo_q4ub",
        user="root",
        password="TZRHuRE9K6tknfmiujChX8I2RuK9pU00")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
