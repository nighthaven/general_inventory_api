from models.movement_model import movement_model

class Movement_response_dto:
    def __init__(self, movement_model:movement_model):
        self.uuid = movement_model.uuid
        self.quantity = movement_model.quantity
        self.type = movement_model.type
        self.created_at = movement_model.created_at
        self.updated_at = movement_model.updated_at
