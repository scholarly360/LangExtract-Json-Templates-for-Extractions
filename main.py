""" 
Langextract examples 
>> fastapi run main.py



curl --request POST \
  --url https://fastapi-func-778374384781.asia-south1.run.app/extract \
  --header 'content-type: application/json' \
  --data '{
  "text": "Canada's Gildan to buy Hanesbrands for $2.2 billion to expand basic apparel businesss Russian counterpart"
}'

OR 

http POST http://localhost:8000/extract content-type:application/json text="Canada's Gildan to buy Hanesbrands for $2.2 billion to expand basic apparel businesss Russian counterpart"


http POST http://localhost:8000/extract content-type:application/json text="National Grid to Sell LNG Terminal to Centrica Consortium in $2 Billion Deal"

"""

from http import client
import httpx, os, uuid
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from vellox import Vellox
from pydantic import BaseModel
from typing import Optional
from google import genai
from pathlib import Path
from dotenv import load_dotenv

from langextract_util import *

load_dotenv()
app = FastAPI()
_security = HTTPBearer(auto_error=False)
# API_TOKEN = os.getenv("API_TOKEN")

class SummarizeTextRequest(BaseModel):
    text: Optional[str] = None

# def require_token(creds: HTTPAuthorizationCredentials = Depends(_security)):
#     if not creds or creds.scheme.lower() != "bearer" or creds.credentials != API_TOKEN:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")

""" Simple endpoint """
@app.get("/")
def health():
    return {"message": "Hello Running !"}

""" Simple extract as Markdown """
@app.post("/extract")
async def extract(req: SummarizeTextRequest):
    if not req.text:
        raise HTTPException(400, "Provide 'text'.")
    source = req.text
    param_template_json_file = "langextract_mna.json"
    param_api_key = os.getenv("LANGEXTRACT_API_KEY")

    if param_api_key is not None:
        param_api_key = os.getenv("LANGEXTRACT_API_KEY")
        param_model_id = "gemini-2.5-flash"
    else:
        param_api_key = os.getenv("OPENAI_API_KEY")
        param_model_id = "gpt-4o"

    res = util_load_extraction_data(param_template_json_file,param_api_key, source, param_model_id)
    return(res)