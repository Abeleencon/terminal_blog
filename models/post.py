import uuid

from database import Database

import datetime

__author__ = 'Abiodun'

class Post(object):

    def __init__(self, blog_id, title, author, content, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.author = author
        self.content = content
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date,

        }

    @staticmethod
    def from_mongo(id):
        return Database.find(collection='posts', query={'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]

