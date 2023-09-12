from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.message import messageEntity, messagesEntity
from models.message import Message
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

route = APIRouter()

@route.get('/messages' , tags=["Messages"])
def get_messages():
    return messagesEntity(conn.local.message.find())

@route.post('/messages', tags=["Messages"])
def create_messages(message:Message):
    new_message = dict(message)
    id = conn.local.message.insert_one(new_message).inserted_id
    message = conn.local.message.find_one({"_id":id})
    return messageEntity(message)  

@route.get('/messages/{id}', tags=["Messages"])
def find_message(id:str):
    message = conn.local.message.find_one({"_id":ObjectId(id)})
    return messageEntity(message)

@route.put('/messages/{id}', tags=["Messages"])
def update_message(id:str, message:Message):
    conn.local.message.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(message)})
    return messageEntity(conn.local.message.find_one({"_id":ObjectId(id)}))

@route.delete('/messages/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Messages"])
def delete_message(id:str):
    messageEntity(conn.local.message.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)