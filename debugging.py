from data import db_session
from data.games import Games
from data.users import User
db_session.global_init("db/digitalmarket.db")
db_sess = db_session.create_session()
games = db_sess.query(Games).all()
for el in games:
    print(el)
