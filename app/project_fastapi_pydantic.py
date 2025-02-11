from email.policy import default

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, List
from fastapi.openapi.utils import status_code_ranges

#rename file - uvicorn project_fastapi_pydantic:app --reload

# http://127.0.0.1:8000/

class Task(BaseModel):
    id: int
    description: str
    is_completed: bool

class TaskCreate(BaseModel):
    description: str = Field(...,
                             min_length=5,
                             max_length=100,
                             description="Task description")
    is_completed: bool=False


app = FastAPI()

tasks: List[Task] = [
    Task(id = 1, description = "Task 1", is_completed = False),
    Task(id = 2, description = "Task 2", is_completed = False),
    Task(id = "3", description = "Task 3", is_completed = False) # Swagger покажет 3, т.к. Pydantic автоматом приведет данные к модели
]



@app.get("/tasks", response_model=List[Task])
async def get_all_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate):
    new_index = max((task.id for task in tasks), default = 0) + 1
    new_task = Task(id = new_index, description = task.description, is_completed=task.is_completed)
    tasks.append(new_task)
    return f"New {new_task} task created"

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate):
    for t in tasks:
        if t.id == task_id:
            t.description = task.description
            return f"Task {task_id} updated"
    raise HTTPException(status_code=404, detail="Task not find")

@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return f"Task with {task_id} was deleted."
    raise HTTPException(status_code=404, detail="Task not find")