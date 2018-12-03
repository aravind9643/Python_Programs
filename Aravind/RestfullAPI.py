from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "id": 101,
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "id": 102,
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "id": 103,
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    },
    {
        "id": 104,
        "name": "Aravind",
        "age": 22,
        "occupation": "Web Developer"
    },
    {
        "id": 105,
        "name": "Anil",
        "age": 24,
        "occupation": "Web Developer"
    },
    {
        "id": 106,
        "name": "Prashanth",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    def get(self, id):
        for user in users:
            if(id == user["id"]):
                return user,200
        return "user not found",404
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        for user in users:
            if(id == user["id"]):
                return "User {} alreay exists".format(args["name"]),400
        user = {
            "name": args["name"],
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user,201
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        for user in users:
            if(id == user["id"]):
                user["name"] = args["name"]
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user,200
        user = {
            "name": args["name"],
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user,201

    def delete(self, id):
        global users
        users = [user for user in users if user["id"] != id]
        return "user with id {} is deleted".format(id),200

class Users(Resource):
    def get(self):
        return users,200
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        user = {
            "name": args["name"],
            "id": args["id"],
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user,201


api.add_resource(Users,"/users")
api.add_resource(User, "/user/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)