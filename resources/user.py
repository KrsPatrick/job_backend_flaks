from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.User import User

class UserListResource(Resource):

    def post(self):

        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if User.get_by_username(username=username):
            return {'message': "Benutzername ist bereits vergeben"}, HTTPStatus.BAD_REQUEST

        verschlüsseltes_password = User.hash_password(password)

        user = User(
            username=username,
            password=verschlüsseltes_password
        )

        user.save()

        return user.data, HTTPStatus.CREATED
