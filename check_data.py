class GenDict(dict):
    def __init__(self):
        self = dict()

    def add_key_value(self, key, value):
        self[key] = value


data = GenDict()
data.add_key_value('students', [])


def create_dict(_name, _surname, _username, _telefon, _email, _password):
    inner_dict = GenDict()
    inner_dict.add_key_value('ad', _name)
    inner_dict.add_key_value('soyad', _surname)
    inner_dict.add_key_value('istifadeci', _username)
    inner_dict.add_key_value('telefon', _telefon)
    inner_dict.add_key_value('email', _email)
    inner_dict.add_key_value('password', _password)
    return create_dict()
