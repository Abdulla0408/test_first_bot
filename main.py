# from collections import namedtuple
# User = namedtuple('User', 'id name lastname age email')
#
# users = [
#     (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com')
#     (2, 'Sobir', 'Toxirov', 18, 'sobir@gmail.com')
#     (3, 'Toxir', 'Sobirov', 35, 'toxir@gmail.com')
# ]
#
# for user in users:
#     us = User(*user)
#     print(us.id, us.name, us.lastname, us.age, us.email)


from collections import namedtuple
Car = namedtuple('Car', "name color speed price space rules")
cars = [
    ('EQUINOX', 'black', '320 km/h', 300000, 5, 'avto'),
    ('ONIX', 'black', '230 km/h', 25000, 4, 'avto'),
    ('DAMAS', 'white', '140 km/h', 7500, 6, 'avto'),

]
for i in cars:
    c = Car(*i)
    print(c.name, c.color, c.speed, c.price, c.space, c.rules)