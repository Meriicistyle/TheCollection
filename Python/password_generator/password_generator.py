import string
import random

while True:
    print("""        
        --> Welcome to the Password
            generator. Just give
            your password length and
            check the output. Parameters
            will be added in the future.
        """)

    def password_generator(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	    return ''.join(random.choice(chars) for _ in range(size))

    print(password_generator(int(input('How long will your password be?: '))))