book = {}

book["апельсин"] = 0.67
book["молоко"] = 1.49
book["авокадо"] = 1.49

print(book)
print(book["авокадо"])

phone_book = {}

phone_book["Дженни"] = 8675309
phone_book["служба спасения"] = 911

print(phone_book["Дженни"])

voted = {}
value = voted.get("Том")

def check_voter(name):
    if voted.get(name):
        print("Выгнать его!")
    else:
        voted[name] = True
        print("Допустить к голосованию!")

check_voter("Том")
check_voter("Майк")
check_voter("Майк")

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data