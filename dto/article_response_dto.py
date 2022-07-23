from models.article_model import article_model

class article_response_dto:
    def __init__(self, article_model:article_model):
        self.uuid = article_model.uuid
        self.label = article_model.label
        self.description = article_model.description
        self.reference = article_model.reference
        self.location_uuid = article_model.location.uuid
        self.location_name = article_model.location.name