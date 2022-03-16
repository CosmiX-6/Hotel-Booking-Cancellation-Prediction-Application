from fastapi import FastAPI, Request
from server.routes.booking_check import router as Router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates('server/templates')

# inititating app
app = FastAPI()

# mounting staticfiles
app.mount("/static", StaticFiles(directory="server/static"), name="static")

app.include_router(Router, tags=["Room Cancellation Predictor"])

@app.get('/', tags=["Root"], include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})