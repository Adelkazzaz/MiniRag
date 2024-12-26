from fastapi import FastAPI
app=FastAPI()


@app.get("/")
def home():
    return{
        "mass":"Wellcome in RAG"
    }
    