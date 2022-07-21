from models.category_model import category_model

class category_response_dto:
    def __init__(self, category_model:category_model):
        self.uuid = category_model.uuid
        self.name = category_model.name


