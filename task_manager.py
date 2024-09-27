from database import get_db
from models import TaskCreate, TaskUpdate
from typing import Optional

async def add_task(task_data: TaskCreate):
    db = await get_db()
    async with db.execute(
        "INSERT INTO tasks (title, priority) VALUES (?, ?)",
        (task_data.title, task_data.priority)
    ) as cursor:
        await db.commit()
        task_id = cursor.lastrowid
    return {"id": task_id, "title": task_data.title, "priority": task_data.priority, "status": "pending"}

async def get_tasks(status: Optional[str] = None):
    db = await get_db()
    if status:
        query = "SELECT * FROM tasks WHERE status = ?"
        args = (status,)
    else:
        query = "SELECT * FROM tasks"
        args = ()
    async with db.execute(query, args) as cursor:
        tasks = await cursor.fetchall()
        return [dict(task) for task in tasks]

async def update_task(task_id: int, task_data: TaskUpdate):
    db = await get_db()
    query = "UPDATE tasks SET title = ?, priority = ?, status = ? WHERE id = ?"
    async with db.execute(query, (task_data.title, task_data.priority, task_data.status, task_id)):
        await db.commit()
    return await get_task_by_id(task_id)

async def delete_task(task_id: int):
    db = await get_db()
    async with db.execute("DELETE FROM tasks WHERE id = ?", (task_id,)):
        await db.commit()
    return {"message": "Task deleted"}

async def get_task_by_id(task_id: int):
    db = await get_db()
    async with db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)) as cursor:
        task = await cursor.fetchone()
        return dict(task) if task else None
