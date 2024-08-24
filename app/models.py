from database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey,Float,Date

class Users(Base):
    
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True,index=True)
    first_name= Column(String)
    last_name= Column(String)
    email= Column(String)
    password= Column(String)
    is_super= Column(Boolean)


class Guests(Base):

    __tablename__ = 'guests'
    id=Column(Integer,primary_key=True,index=True)
    admin_id =Column(Integer,ForeignKey('users.id'))
    first_name= Column(String)
    middle_name = Column(String)
    last_name= Column(String)
    arabic_name=Column(String)
    nationality=Column(String)
    id_number = Column(String)
    id_copy = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    emergency_name=Column(String)
    emergency_phone =Column(String)
    emergency_relation = Column(String)


class Finance(Base):
    __tablename__ = 'finance'
    id=Column(Integer,primary_key=True,index=True)
    guest_id = Column(Integer,ForeignKey('guests.id'))
    amount = Column(Float)
    paid_amount =Column(Float)
    unpaid_amount = Column(Float)
    payment_method = Column(String,nullable=True)
    payment_date = Column(Date,nullable=True)
    is_paid= Column(Boolean,default=False)

class Reservation(Base):
    __tablename__ = 'reservation'
    id=Column(Integer,primary_key=True,index=True)
    guest_id = Column(Integer,ForeignKey('guests.id'))
    room_id = Column(Integer,ForeignKey('rooms.id'))
    check_in = Column(Date)
    check_out = Column(Date)

class Rooms(Base):
    __tablename__ = 'rooms'
    id=Column(Integer,primary_key=True,index=True)
    room_number = Column(Integer)
    room_type = Column(String)
    room_price = Column(Float)
    room_view = Column(String)

class Accounting(Base):
    __tablename__ = 'accounting'
    id=Column(Integer,primary_key=True,index=True)
    guest_id = Column(Integer,ForeignKey('guests.id'))
    room_id = Column(Integer,ForeignKey('rooms.id'))
    service =Column(String)
    amount = Column(Float)
    is_paid=Column(Boolean)

class Resturant():
    __tablename__ = 'resturant'
    id=Column(Integer,primary_key=True,index=True)
    guest_id = Column(Integer,ForeignKey('guests.id'))
    room_id = Column(Integer,ForeignKey('rooms.id'))
    food = Column(String)
    amount = Column(Float)
    is_paid= Column(Boolean)


class Trips():
    __tablename__ = 'trips'
    id=Column(Integer,primary_key=True,index=True)
    guest_id = Column(Integer,ForeignKey('guests.id'))
    room_id = Column(Integer,ForeignKey('rooms.id'))
    trip = Column(String)
    amount = Column(Float)
    is_paid= Column(Boolean)


class Extras():
    __tablename__ = 'extras'
    id=Column(Integer,primary_key=True,index=True)
    guest_id = Column(Integer,ForeignKey('guests.id'))
    room_id = Column(Integer,ForeignKey('rooms.id'))
    extra = Column(String)
    amount = Column(Float)
    is_paid= Column(Boolean)




