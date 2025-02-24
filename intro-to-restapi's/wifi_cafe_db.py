import random
from flask import Flask, jsonify, render_template, request
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, DeclarativeBase
from sqlalchemy import Integer, String, Boolean, create_engine

# Defining the Base
class Base(DeclarativeBase):
    pass


# Cafe TABLE Configuration
class Cafe(Base):
    __tablename__ = "wifi_cafe_db"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def __init__(self, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
        self.name = name 
        self.map_url = map_url 
        self.img_url = img_url 
        self.location = location 
        self.seats = seats 
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi 
        self.has_sockets = has_sockets 
        self.can_take_calls = can_take_calls 
        self.coffee_price = coffee_price 


# Creating the db
engine = create_engine("sqlite:///wifi_db.db", echo=True)
# Creating the tables
Base.metadata.create_all(bind=engine)

# Creating a session
Session = sessionmaker()
session = Session(bind=engine)

def add_restaurant(name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
    """Adds a new restaurant to the database"""
    try:
        cafe = Cafe(name.title(), map_url, img_url, location, seats, bool(has_toilet), bool(has_wifi), bool(has_sockets), bool(can_take_calls), coffee_price)
        session.add(cafe)
        session.commit()
        return {"response":{"success": "Successfully added the new cafe."}}
    except Exception as e:
        xc = e
        return {"error":{"Post Error":"error in processing data ensure keyed in data is unique from previous sent data"}}

def render_cafe(cafe_object):
    return {key: value for key, value in vars(cafe_object).items() if key != '_sa_instance_state'}

def return_rand_cafe():
    """returns a random cafe from the database"""
    query_response = session.query(Cafe).all()
    return render_cafe(query_response[random.randint(0, len(query_response) -1)])

def return_all_cafes():
    return [render_cafe(cafe) for cafe in session.query(Cafe).all()]

def find_by_location(loc):
    loc = loc.title()
    query = session.query(Cafe).filter_by( location = loc).all()
    if query:
        return [render_cafe(q) for q in query]
    else:
        return {"error":{"Not Found":"Sorry, we don't have a cafe at that location."}}

def update_price(cafe_id, new_price):
    all_ids = [r.id for r in session.query(Cafe).all()]
    if cafe_id in all_ids:
        query = session.query(Cafe).filter_by( id = cafe_id ).first()
        if query and new_price:
            query.coffee_price = str(new_price)
            session.commit()
            return jsonify({"success":"price updated"}), 200
        else:
            return jsonify({"error": "failed to update price"}), 500
    else:
         return jsonify({"error":{"not found": "sorry a cafe with such an id was not found."}}), 400


def drop_cafe(cafe_id):
    for res in session.query(Cafe).all():
        if cafe_id:
            if res.id == int(cafe_id):
                session.delete(res)
                session.commit()
                return True
    return False
