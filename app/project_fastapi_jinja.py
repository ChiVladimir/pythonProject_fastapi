from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

#rename file - uvicorn project_fastapi_jinja:app --reload

# http://127.0.0.1:8000/

class Task(BaseModel):
    id: int
    description: str
    is_completed: bool = False


# class TaskCreate(BaseModel):
#     description: str = Field(...,
#                              min_length=5,
#                              max_length=100,
#                              description="Task description")
#     is_completed: bool = False


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
#app = FastAPI()

templates = Jinja2Templates(directory="templates")

tasks: List[Task] = [
    Task(id=1, description="Task 1", is_completed=True),
    Task(id=2, description="Task 2", is_completed=False),
    Task(id=3, description="Task 3", is_completed=False)
]


@app.get("/", response_model=List[Task], response_class=HTMLResponse)
async def get_all_tasks(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.get("/task/{task_id}", response_model=Task, response_class=HTMLResponse)
async def get_task(request: Request, task_id: Annotated[int, Path(ge=1)]):
    for task in tasks:
        if task.id == task_id:
            task.description = task.description
            return templates.TemplateResponse("task_detail.html", {"request": request, "task": task})
    raise HTTPException(status_code=404, detail="Task not find")

@app.post("/task", response_model=Task, response_class=HTMLResponse)
async def create_task(
        # request: Request,
        # description: Annotated[str, Path(min_length=3, max_length=100)],
        # is_completed: Annotated[bool, Path()]):
        request: Request,
        description: str,
        is_completed: bool):
    new_index = max((task.id for task in tasks), default = 0) + 1
    new_task = Task(id = new_index, description = description, is_completed=is_completed)
    tasks.append(new_task)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/task/{task_id}/{description}/{is_completed}", response_model=Task, response_class=HTMLResponse)
async def update_task(
        request: Request,
        task_id:int,
        description: str,
        is_completed: bool):
    for task in tasks:
        if task.id == task_id:
            task.description = description
            task.is_completed = is_completed
            return templates.TemplateResponse("task_detail.html", {"request": request, "task": task})
    raise HTTPException(status_code=404, detail="Task not find")

@app.delete("/task/{task_id}", response_model=Task, response_class=HTMLResponse)
async def delete_task(request: Request, task_id: Annotated[int, Path(ge=1)]):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})
    raise HTTPException(status_code=404, detail="Task not find")
