import langextract as lx
from pathlib import Path
import json
import uuid,os
from langextract_util import *
from dotenv import load_dotenv
load_dotenv()

### common
param_template_json_file = "langextract_mna.json"
param_text = "Associated British Foods (ABF.L), has agreed to buy Hovis, giving it another big UK bread brand on top of Kingsmill so they can better compete in a market that has seen a decline in demand for the packaged sliced loaf."


### Using Gemini

param_api_key = os.getenv("LANGEXTRACT_API_KEY")
param_model_id = "gemini-2.5-flash"
res = util_load_extraction_data(param_template_json_file,param_api_key, param_text, param_model_id)
print(res)

### Using OpenAI

param_api_key = os.getenv("OPENAI_API_KEY")
param_model_id = "gpt-4o"
res = util_load_extraction_data(param_template_json_file,param_api_key, param_text, param_model_id)
print(res)