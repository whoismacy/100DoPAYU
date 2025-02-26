from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

class Base(DeclarativeBase):
    pass

class User(Base, UserMixin):
    __tablename__ = "user_data"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

# Creating engine and session
engine = create_engine("sqlite:///instance/user-db.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker()
session = Session(bind=engine)

def add_user(email, password, name):
    try:
        user = User(email, generate_password_hash(password, method='scrypt', salt_length=16), name)
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(f"Failed adding user {e}")
        return False

def check_user(email, password):
    response = session.query(User).filter_by(email = email).first()
    if response:
        if check_password_hash(response.password, password):
            return response
    return None

def user_exists(id):
    for r in session.query(User).all():
        if r.id == id:
            return r
    return None

def email_exists(email):
    for r in session.query(User).all():
        if r.email == email:
            return True
    return False
# print(check_user("cheekssandy@gmail.com", ";m)D7L2gqPe.2Mi"))