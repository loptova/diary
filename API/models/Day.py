class Day:
    id: int
    title: str
    info: str
    dayDate = None

    def __init__(self, id, title, info, dayDate):
        self.id = id
        self.title = title
        self.info = info
        self.dayDate = dayDate

    def returnJSon(self):
        return {
            "id": self.id,
            "title": self.title,
            "info": self.info,
            "dayDate": self.dayDate
        }

    