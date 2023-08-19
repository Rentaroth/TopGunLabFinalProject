import asyncio
import motor.motor_asyncio as motor
from umongo.frameworks.motor_asyncio import MotorAsyncIOInstance

from django.conf import settings

connection = motor.AsyncIOMotorClient(settings.MONGO_URI)
db = connection['TGLBlog']
instance = MotorAsyncIOInstance(db)

async def connect():
  try:
    # Intentar realizar una operación sencilla para verificar la conexión
    result = await db.command("ping")
    print("Database is reachable:", result.get("ok") == 1)
  except Exception as e:
    print("Database connection error:", e)

if __name__ != '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(connect())