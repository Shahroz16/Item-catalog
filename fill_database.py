from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, CategoryItem, User

engine = create_engine('postgresql://postgres:postgres@localhost:5432/itemcatalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user1 = User(username="Shahroz", email="shahroz@email.com",
             picture="/static/dummy.jpg")
session.add(user1)
session.commit()

user2 = User(username="Ali", email="ali@email.com",
             picture="/static/dummy.jpg")
session.add(user2)
session.commit()

category1 = Category(name="Fruits", user_id=1)
session.add(category1)
session.commit()

category2 = Category(name="Vagetables", user_id=1)
session.add(category2)
session.commit()

category3 = Category(name="Office", user_id=2)
session.add(category3)
session.commit()

categoryItem1 = CategoryItem(name="Apples", description="Red fruit",
                             category_id=1, user_id=1)
session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Oranges", description="Orange fruit",
                             category_id=1, user_id=1)
session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Potato", description="Rymes with tomato",
                             category_id=2, user_id=1)
session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(name="Chair", description="Item to sit on ",
                             category_id=3, user_id=2)
session.add(categoryItem4)
session.commit()

print "dummy data added!"
