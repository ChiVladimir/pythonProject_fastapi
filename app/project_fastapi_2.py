#from http.client import HTTPException

from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

from fastapi.openapi.utils import status_code_ranges

#rename file - uvicorn project_fastapi:app --reload

# http://127.0.0.1:8000/

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

tasks = [
    {"id": 1, "description": "Task 1"},
    {"id": 2, "description": "Task 2"},
    {"id": 3, "description": "Task 3"}
]



@app.get("/")
async def get_all_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int) -> str:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not find")

@app.post("/tasks")
async def create_task(description:str) -> str:
    new_index = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {"id":new_index, "description": description}
    tasks.append(new_task)
    return f"New {new_task} task created"

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, description: str) -> str:
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            return f"Task {task} updated"
    raise HTTPException(status_code=404, detail="Task not find")

@app.patch("/tasks/{task_id}")
async def patch_task(task_id: int, description: str = None) -> str:
    for task in tasks:
        if task["id"] == task_id:
            if description:
                task["description"] = description
                return task
    raise HTTPException(status_code=404, detail="Task not find")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int) -> str:
    for i, task in enumerate(tasks):
        if task ["id"] == task_id:
            del tasks[i]
            return f"Task with {task_id} was deleted."
    raise HTTPException(status_code=404, detail="Task not find")

@app.delete("/")
async def delete_all_tasks():
    tasks.clear()
    return "All tasks were deleted"
