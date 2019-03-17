class TaskByMonthAndYear:
    task_id: int
    task_title: str
    task_info: str
    day_title: str
    day_info: str
    day_num: int

    def __init__(self, task_id, task_title, task_info, day_title, day_info, day_num):
        self.task_id = task_id
        self.task_title = task_title
        self.task_info = task_info
        self.day_title = day_title
        self.day_info = day_info
        self.day_num = day_num

    def returnJSon(self):
        return {
            "task_id": self.task_id,
            "task_title": self.task_title,
            "task_info": self.task_info,
            "day_title": self.day_title,
            "day_info": self.day_info,
            "day_num": self.day_num
        }