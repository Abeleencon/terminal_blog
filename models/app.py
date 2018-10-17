from database import Database
from menu import Menu
#from models.blog import Blog
#from models.post import Post

__author__ = 'Abiodun'

Database.initialize()

menu = Menu()

menu.run_menu()
'''blog = Blog(title="The Act",
            author="Johnny Bravo",
            description="The Act of doing right")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.get_from_mongo(id)

post2 = Post(blog_id="1234",
             title="Things Fall Apart",
             author="Chinua Achebe",
             content="Nobel prize book")

print(blog.get_post())

blog.save_to_mongo()
'''


