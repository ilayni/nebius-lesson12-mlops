from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer

app = FastAPI()
# tokenizer = AutoTokenizer.from_pretrained(
#     “deepseek-ai/DeepSeek-V3”,
#     trust_remote_code=True
# )
tokenizer = AutoTokenizer.from_pretrained(“distilgpt2”)

class TextInput(BaseModel):
    text: str

@app.post("/tokenize")
def tokenize(body: TextInput):
    tokens = tokenizer.encode(body.text)
    return {"tokens": tokens, "count": len(tokens)}