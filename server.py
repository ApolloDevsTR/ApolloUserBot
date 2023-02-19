import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Selamla(Resource):
    def get(self):
        return "Apollo Userbot Çalışıyor!"


api.add_resource(Selamla, '/')
app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
