from flask import jsonify
from sqlalchemy import create_engine

from settings import connectionString

from models.Task import Task
from models.Day import Day
from models.TaskByMonthAndYear import TaskByMonthAndYear


class DataBaseWorker:

    engine = create_engine(connectionString)

    tasks: [] = []
    days: [] = []

    def getTasks(self):
        rs = self.engine.execute("select * from Tasks")
        self.tasks.clear()
        for row in rs:
            self.tasks.append(
                Task(
                    row['task_id'],
                    row['task_title'],
                    row['task_info'],
                    row['day_id']
                ).returnJSon()
            )
        return jsonify({ 'tasks': self.tasks })

    
    def getDays(self):
        rs = self.engine.execute("select * from Days")
        self.days.clear()
        for row in rs:
            self.days.append(
                Day(
                    row['day_id'],
                    row['day_title'],
                    row['day_info'],
                    row['day_daydate']
                ).returnJSon()
            )
        return jsonify({ 'days': self.days })


    # select to_char(day_daydate, 'MM') from days;
    def getTasksByMAY(self, month, year):
        rs = self.engine.execute("select task_id, task_title, task_info, day_title, day_info, to_char(days.day_daydate, 'DD')::int as day_num from tasks inner join days on tasks.day_id = days.day_id where to_char(days.day_daydate, 'YYYY')::int = '"+ year +"'::int and to_char(days.day_daydate, 'MM')::int = '"+ month +"'::int;")
        tasksByMonthAndYear = []
        for row in rs: 
            tasksByMonthAndYear.append(
                TaskByMonthAndYear(
                    row['task_id'],
                    row['task_title'],
                    row['task_info'],
                    row['day_title'],
                    row['day_info'],
                    row['day_num']
                ).returnJSon()
            )        
        return jsonify({ 'tasks': tasksByMonthAndYear })