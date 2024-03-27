import re
 regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 def check(email):
    if(re.fullmatch(regex, email)):

        print("Valid Email")
    else:
    print("Invalid Email")
 if _name_ == '_main_':
    email = "Sangmeshwar567@gmail.com"
    check(email)
    email = "my.ownsite@our-earth.org"
    check(email)
    email = "Sangmeshwar567.com"
    check(email)