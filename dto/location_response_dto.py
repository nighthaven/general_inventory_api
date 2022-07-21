from models.location_model import location_model

class Location_response_dto:
    def __init__(self, location_model):
        self.uuid = location_model.uuid
        self.name = location_model.name