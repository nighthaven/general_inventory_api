from fastapi import FastAPI


from connection.connection import engine
from models import article_model
from models import movement_model
from models import location_model
from models import category_model
from path.articles_path import path as path_article
from path.movement_path import path as path_movement
from path.category_path import path as path_category
from path.location_path import path as path_location


app = FastAPI()

app.include_router(path_article)
app.include_router(path_movement)
app.include_router(path_category)
app.include_router(path_location)


article_model.Base.metadata.create_all(engine)
movement_model.Base.metadata.create_all(engine)
location_model.Base.metadata.create_all(engine)
category_model.Base.metadata.create_all(engine)

@app.get("/")
def root():
    return "GENERAL INVENTORY : une API qui vous permet de gerer vos mouvements de stock"




