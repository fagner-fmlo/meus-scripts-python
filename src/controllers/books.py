from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': 'Engenharia de confiabilidade'},
    {'id': 1, 'title': 'Manual Devops'}
]

@api.route('/books')
class BookList(Resource):
    def get(self, ):
        return books_db