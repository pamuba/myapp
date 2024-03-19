# from flask_bcrypt  import Bcrypt

# bcrypt = Bcrypt()

# password = 'supersecretpassword'

# hashed_password = bcrypt.generate_password_hash(password=password)
# # print(hashed_password)


# result  = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')
# print(result)

from werkzeug.security import generate_password_hash, check_password_hash

password = 'supersecretpassword'

hashed_password = generate_password_hash(password=password)
print(hashed_password)


result  = check_password_hash(hashed_password, 'supersecretpassword')
print(result)