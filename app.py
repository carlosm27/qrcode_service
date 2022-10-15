from fastapi import FastAPI, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Request
from starlette.responses import StreamingResponse

from dotenv import load_dotenv
import qrcode
from io import BytesIO
import os
from pydantic import BaseModel

from deta import Deta

app = FastAPI()

load_dotenv()

PROJECT_KEY = os.environ.get('PROJECT_KEY')
deta = Deta(PROJECT_KEY)
drive = deta.Drive("qr_codes")

origins = [
	
]



app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=['GET', 'POST'],
	allow_headers=["*"],
	)

class DataToConvert(BaseModel):
	name: str
	text: str



@app.get("/")
def hello():
    return "Hello, welcome to QR Code Generator!"

@app.post('/qr')
def qr_generator(data: DataToConvert):
    name = data.name
    data = data.text
    img = qrcode.make(data)
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    res = drive.put(name,img_io)
    return res

@app.get("/image/{name}")
def download_img(name:str):
	res = drive.get(name)
	
	return StreamingResponse(res.iter_chunks(1024), media_type="image/png")




