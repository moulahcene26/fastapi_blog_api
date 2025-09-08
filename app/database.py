import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://localhost:27017'
)
db = client["blorf_blog"]



