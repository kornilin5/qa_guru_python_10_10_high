import dataclasses


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    day: str
    moth: str
    year: str
    subjects: str
    hobbies: str
    photo: str
    current_address: str
    state: str
    city: str
    date_of_birth: str


user = Users(first_name='ИМЯ',
             last_name='ФАМИЛИЯ',
             email='EMAIL@mail.ru',
             gender='Male',
             phone='2381491357',
             day='17',
             moth='March',
             year='1999',
             subjects='English',
             hobbies='Reading',
             photo='ZnugKfP5UJk.jpg',
             current_address='ТУТ АДРЕСС',
             state='Haryana',
             city='Panipat',
             date_of_birth='17 March,1999')
