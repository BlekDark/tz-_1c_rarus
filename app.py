from fastapi import FastAPI, HTTPException, Depends
from models import TaskCreate, TaskUpdate, TaskOut
from task_manager import add_task, get_tasks, update_task, delete_task

app = FastAPI()

@app.on_event("startup")
async def startup():
    from database import init_db
    await init_db()

@app.post("/tasks", response_model=TaskOut)
async def create_task(task_data: TaskCreate):
    task = await add_task(task_data)
    return task

@app.get("/tasks", response_model=list[TaskOut])
async def read_tasks(status: str = None):
    tasks = await get_tasks(status)
    return tasks

@app.put("/tasks/{task_id}", response_model=TaskOut)
async def update_task_endpoint(task_id: int, task_data: TaskUpdate):
    task = await update_task(task_id, task_data)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task_endpoint(task_id: int):
    task = await delete_task(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
