# Schools-Management-System
## How to run the backend server
1. Open SMS Project in Vs Code
2. Go to the terminal and run "cd Backend"
3. "cd SMSBack"
4. run "pip install -r requirements.txt"
5. run "python manage.py runserver"

## Endpoints
> POST - login - 'http://127.0.0.1:8000/api/users/login' : {username, password}
>> {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjg0NDQ4NywiaWF0IjoxNzE2NzU4MDg3LCJqdGkiOiIxODA1ZGM3MzA2MmY0MjVkYTk1NmVkOTYwYWRjZGMyZiIsInVzZXJfaWQiOjJ9.LAbe-TLGh8B6HRchEiiZCG4-CDGml9nVGe-egMkqYrI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzUwMDg3LCJpYXQiOjE3MTY3NTgwODcsImp0aSI6ImY4YTcwMGZlNzE5ZTQxZGJhNjM2OTA3YTFhOWFmNDk1IiwidXNlcl9pZCI6Mn0.CuKLdCoHRYI9bC0zbUSrWnR1wubGBud21lWAD8j5qzM",
    "id": 2,
    "_id": 2,
    "username": "emma",
    "email": "emma@gmail.com",
    "name": "emma",
    "role": "super_admin",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzUwMDg3LCJpYXQiOjE3MTY3NTgwODcsImp0aSI6ImZhZTQyNjVhNDgyMzQ3NDliNjQ2NTAxZWFiODUwMjE4IiwidXNlcl9pZCI6Mn0.N7y0X3a5qkMpoMb9CJr8blgklQkfHaHwjO7QXdJbrYk"
}

> POST - creating a school - http://127.0.0.1:8000/api/schools/create : {
        name, 
        address, 
        phone, 
        school_type =   [
                    ('preschool', 'Preschool'),
                    ('primary', 'Primary School'),
                    ('jhs', 'Junior High School'),
                    ('shs', 'Senior High School'),
                    ('university', 'University'),
                ]
        admin_username,
        admin_password,
    }
>> {
    "school": {
        "name": "st Peters",
        "school_type": "shs",
        "address": "Eastern Region",
        "phone": "0200817325",
        "admin": 8,
        "admin_username": "Uba"
    }
}

> POST - creating a class - http://127.0.0.1:8000/api/classes/add : {name}
>> {
    "_id": 8,
    "school": "Presec Boys School",
    "name": "3Science8"
}

> GET - getting list of all users - http://127.0.0.1:8000/api/users 
>> [
    {
        "id": 1,
        "_id": 1,
        "username": "admin@gmail.com",
        "email": "admin@gmail.com",
        "name": "admin@gmail.com",
        "role": "school_admin",
        "school_id": 1,
        "profile": "/images/placeholder.png"
    },
    {
        "id": 2,
        "_id": 2,
        "username": "emma",
        "email": "emma@gmail.com",
        "name": "emma",
        "role": "super_admin",
        "school_id": null,
        "profile": "/images/placeholder.png"
    }
]

> GET - get logged in user details - http://127.0.0.1:8000/api/users/profile
>> {
        "id": 1,
        "_id": 1,
        "username": "admin@gmail.com",
        "email": "admin@gmail.com",
        "name": "admin@gmail.com",
        "role": "school_admin",
        "school_id": 1,
        "profile": "/images/placeholder.png"
    }

> GET - get user by id - http://127.0.0.1:8000/api/users/id 
>> {
        "id": 1,
        "_id": 1,
        "username": "admin@gmail.com",
        "email": "admin@gmail.com",
        "name": "admin@gmail.com",
        "role": "school_admin",
        "school_id": 1,
        "profile": "/images/placeholder.png"
    }

> GET - get teachers of a school - http://127.0.0.1:8000/api/schools/id/teachers 
>> [
    {
        "_id": 1,
        "name": "Ub",
        "subjects": [
            {
                "name": "Mathematics",
                "code": "1"
            },
            {
                "name": "Chemistry",
                "code": "2"
            }
        ]
    },
    {
        "_id": 2,
        "name": "Michael",
        "subjects": [
            {
                "name": "Chemistry",
                "code": "2"
            },
            {
                "name": "Mathematics",
                "code": "1"
            }
        ]
    }
]

> GET - get all teachers - http://127.0.0.1:8000/api/teachers
>> [
    {
        "_id": 1,
        "name": "Ub",
        "subjects": [
            {
                "name": "Mathematics",
                "code": "1"
            },
            {
                "name": "Chemistry",
                "code": "2"
            }
        ]
    },
    {
        "_id": 2,
        "name": "Michael",
        "subjects": [
            {
                "name": "Chemistry",
                "code": "2"
            },
            {
                "name": "Mathematics",
                "code": "1"
            }
        ]
    }
]

> GET - get a teacher (super admin) - http://127.0.0.1:8000/api/teachers/id
>> {
        "_id": 1,
        "name": "Ub",
        "subjects": [
            {
                "name": "Mathematics",
                "code": "1"
            },
            {
                "name": "Chemistry",
                "code": "2"
            }
        ]
    }

> GET - get teacher of a school - http://127.0.0.1:8000/api/schools/teacher
>>  {
        "_id": 1,
        "name": "Ub",
        "subjects": [
            {
                "name": "Mathematics",
                "code": "1"
            },
            {
                "name": "Chemistry",
                "code": "2"
            }
        ]
    }