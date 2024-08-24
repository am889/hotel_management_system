from pydantic import BaseModel,Field
from typing import Optional

class Room:
    id: int
    room_number:str
    floor :str
    room_type:str
    room_size:int
    room_price:float
    room_status:str
    room_view:str
    

    def __init__(self,id,room_number,floor,room_type,room_size,room_price,room_status,room_view):
        self.id = id
        self.room_number = room_number
        self.room_type = room_type
        self.room_price = room_price
        self.room_status = room_status
        self.room_view = room_view
        self.floor = floor
        self.room_size = room_size


class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email:str
    password:str 
    is_super:bool =Field(default=False)

class GuestRequest(BaseModel):
    first_name:str
    middle_name:str
    last_name:str
    arabic_name:str
    nationality:str
    id_number:str 
    id_copy :str 
    age:int
    gender:str
    phone_number:str
    email :str
    emergency_name:str
    emergency_phone:str
    emergency_relation:str

class Token(BaseModel):
    access_token: str
    token_type:str

class RoomRequest(BaseModel):
    id: Optional[int]=Field(description="This is optional",default=None)
    room_number:str=Field(max_length=3)
    floor :str=Field(max_length=2)
    room_type:str=Field(max_length=6)
    room_size:int
    room_price:float
    room_status:str=Field()
    room_view:str