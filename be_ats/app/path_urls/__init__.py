from app import api
from app.controllers.tes import Isi


def tesIsi_api_path():
    api.add_resource(Isi, "/api/data")
