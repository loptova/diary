#!flask/bin/python
from flask import Flask, redirect, url_for, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

from services.database_worker import DataBaseWorker



app = Flask(__name__)
CORS(app)
api = Api(app)



@app.errorhandler(404)
def not_found(error):
    return jsonify({'ERROR' : {'status': '404', 'error': str(error)}})


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to Diary API"


class Tasks(Resource):
    def get(self):
        return DataBaseWorker().getTasks()


class Days(Resource):
    def get(self):
        return DataBaseWorker().getDays()


class TasksByMonthAndYear(Resource):
    def get(self, month, year):
        return DataBaseWorker().getTasksByMAY(month, year)



api.add_resource(Tasks, '/diary/api/tasks')
api.add_resource(Days, '/diary/api/days')
api.add_resource(TasksByMonthAndYear, '/diary/api/tasksbymonthandyear/<string:month>&<string:year>')




if __name__ == '__main__':
    app.run(debug=True)