from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("my_index.html")


# альтернативный вариант
@app.get("/file", response_class=FileResponse)
def root_html():
    return "my_index.html"

#uvicorn Lesson_2_1:app --reload