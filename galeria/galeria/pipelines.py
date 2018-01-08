from sqlalchemy.orm import sessionmaker
from .models import Rest_Posts, db_connect, create_posts_table


class GaleriaPipeline(object):
   """Galeria pipeline for storing scraped items in the database"""
   def __init__(self):
       """
       Initializes database connection and sessionmaker.
       Creates table.
       """
       engine = db_connect()
       create_posts_table(engine)
       self.Session = sessionmaker(bind=engine)

   def process_item(self, item, spider):
       """Save posts in the database.
       This method is called for every item pipeline component.
       """
       session = self.Session()
       post = Rest_Posts(**item)

       try:
           session.add(post)
           session.commit()
       except:
           session.rollback()
           raise
       finally:
           session.close()

       return item
