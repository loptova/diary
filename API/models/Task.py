class Task:
    id: int
    title: str
    info: str
    dayId: int

    def __init__(self, id, title, info, dayId):
        self.id = id
        self.title = title
        self.info = info
        self.dayId = dayId

    def returnJSon(self):
        return {
            "id": self.id,
            "title": self.title,
            "info": self.info,
            "dayId": self.dayId
        }
