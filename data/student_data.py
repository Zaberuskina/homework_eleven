from dataclasses import dataclass

@dataclass
class Student:
    first_name: str = 'John'
    last_name: str = 'Doe'
    email: str = 'john.doe@example.com'
    gender: str = 'Male'
    phone: str = '1234567890'
    birth_day: str = '10'
    birth_month: str = 'May'
    birth_year: str = '1990'
    subject: str = 'Maths'
    hobbies: str = 'Sports, Music'
    picture: str = 'test_image.jpg'
    address: str = '123 Elm Street'
    state: str = 'NCR'
    city: str = 'Delhi'
