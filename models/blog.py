import datetime
import uuid

from database import Database
from models.post import Post

__author__ = 'Abiodun'


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter title of post: ")
        content = input("Enter content of post: ")
        date = input("Enter post date, or leave blank(in format DDMMYYYY: ")
        post = Post(blog_id=self.id,
                    title=title,
                    author=self.author,
                    content=content,
                    date=datetime.datetime.strptime(date, "%d%m%Y"))

        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])