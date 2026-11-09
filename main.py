from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine

DB_URL = 'postgresql+psycopg://sd4:sd4@localhost:5432/insta'
app = create_engine(DB_URL, echo=True)

app = FastAPI()
template = Jinja2Templates

@app.get('/')
def home():
    return {'hi': 'hello'}