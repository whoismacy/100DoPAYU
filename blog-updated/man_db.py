from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, Text, create_engine
from datetime import datetime as dt

class Base(DeclarativeBase):
    pass

class BlogPost(Base):
    __tablename__ = "blog_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, title, subtitle, date, body, author, img_url):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.body = body
        self.author = author
        self.img_url = img_url

# Create engine
engine = create_engine("sqlite:///instance/posts.db", echo=True)
Base.metadata.create_all(bind=engine)

# Create session
Session = sessionmaker()
session = Session(bind=engine)

def render_blog(blog_object):
   return {key: value for key, value in vars(blog_object).items() if key != '_sa_instance_state'}

def return_all():
    """returns all the contents of the database in a json format"""
    return [render_blog(blog) for blog in session.query(BlogPost).all()]

def fetch_post(post_id):
    post_id = int(post_id)
    for blog in session.query(BlogPost).all():
        if blog.id == post_id:
            return render_blog(blog)

def add_to_db(title, subtitle, author, img_url, body):
    date = dt.today().strftime("%B %d, %Y")
    try:
        blog = BlogPost(title, subtitle, date, body, author.title(), img_url)
        session.add(blog)
        session.commit()
        return True
    except Exception:
        return False

def drop_blog(blog_id):
    blog_id = int(blog_id)
    for blog in session.query(BlogPost).all():
        if blog.id == blog_id:
            session.delete(blog)
            session.commit()
            return True
    return False

def edit_blog(blog_id, title, subtitle, author, body):
    query_response = session.query(BlogPost).filter_by( id = blog_id).first()
    if query_response:
        query_response.title = title
        query_response.subtitle = subtitle
        query_response.author = author
        query_response.body = body
        session.commit()
        return True
    else:

        return False