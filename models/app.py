from database import Database
from models.post import Post

__author__ = 'Abiodun'

Database.initialize()

post1 = Post(blog_id="1233",
             title="The Act",
             author="Johnny Bravo",
             content="The Act of doing right")

'''post2 = Post(blog_id="1234",
             title="Things Fall Apart",
             author="Chinua Achebe",
             content="Nobel prize book")
'''

print(post1.content)

post1.save_to_mongo()


