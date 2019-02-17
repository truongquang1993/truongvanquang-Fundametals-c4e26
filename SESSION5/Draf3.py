# p0 = {
#     "name": "H.Duc",
#     "age": 24,
#     "location": "Hai Phong",
#     "status": False,
#     "favs": ["books", "movies"]
# }

# p1 = {
#     "name": "Quang",
#     "age": 26,
#     "location": "Nam Dinh",
#     "status": True,
#     "favs": ["books", "movies", "sleep"]
# }

# p2 = {
#     "name": "Huy",
#     "age": 30,
#     "location": "Ha Noi",
#     "status": False,
#     "favs": ["books", "movies", "sleep"]
# }

p_list = [
    {
    "name": "H.Duc",
    "age": 24,
    "location": "Hai Phong",
    "status": False,
    "favs": ["books", "movies"]
    },
    {
    "name": "Huy",
    "age": 30,
    "location": "Ha Noi",
    "status": False,
    "favs": ["books", "movies", "sleep"]
    },
    {
    "name": "Huy",
    "age": 30,
    "location": "Ha Noi",
    "status": False,
    "favs": ["books", "movies", "sleep"]
    }
]

# for i in range(2):
#     p_list.append(i)



# p_list.append(p0)
# p_list.append(p1)
# p_list.append(p2)

# p = p_list[1]
# print(p_list[1]["status"])

print(p_list)

for i in p_list:
    print(i["name"], i["age"], sep=": ")

print(p_list[0]["location"])

