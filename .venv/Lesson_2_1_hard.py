from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


class TwoNum(BaseModel):
    num1: int
    num2: int


@app.post("/calculate")
async def calculate(nums: TwoNum):
    return {"result": nums.num1 + nums.num2}

#uvicorn Lesson_2_1_hard:app --reload