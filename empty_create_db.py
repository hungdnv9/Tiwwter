from app import create_app, db


#creating app to access databse without starting the server
app = create_all()
ctx = app.app_context()
ctx.push()

#db_manipulation goes here
db.drop_all()
db.create_all()

#closing the app
ctx.pop()
