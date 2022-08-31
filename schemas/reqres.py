from voluptuous import ALLOW_EXTRA
from voluptuous import Schema

single_user = Schema({
    "data": {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    "support": {
        "url": str,
        "text": str
    }
})

register = Schema({
    "id": int,
    "token": str
})

create = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})

update = Schema({
    "name": str,
    "job": str,
    "updatedAt": str
})


