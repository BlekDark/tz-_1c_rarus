import aiosqlite

DATABASE_URL = "sqlite+aiosqlite:///./tasks.db"

async def init_db():
    async with aiosqlite.connect('tasks.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT DEFAULT 'pending'
            );
        ''')
        await db.commit()

async def get_db():
    db = await aiosqlite.connect('tasks.db')
    db.row_factory = aiosqlite.Row
    return db
