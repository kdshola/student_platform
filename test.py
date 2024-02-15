from models.user import User

model = User(password='hello')
print(model.__dict__)
print(model.check_password('hello'))
print(model.check_password('newpass'))
print(type(model))
print(type(model.password))
