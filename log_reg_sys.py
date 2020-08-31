import check_functions
import json
from check_data import data
import check_data

istifadeci_bazasi = []


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
    return inner_dict


class User:
    def __init__(self, _name, _surname, _username, _telefon, _email, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.telefon = _telefon
        self.email = _email
        self.password = _password

    def show(self):
        return f"<Sizin adınız {self.name}, soyadınız isə {self.surname}>"


# İstifadəçi əlavə etmək üçün funksiya (başlanğıc)
def _name(args):
    pass


def user_add():
    i = 0
    user_count = int(input("Neçə istifadəçi daxil etmək istəyirsiniz? (rəqəm daxil edin) : "))
    while i < user_count:
        input_name = input("Adınızı daxil edin : ")
        check_functions.check_name(input_name)
        input_surname = input("Soyadınızı daxil edin : ")
        check_functions.check_surname(input_surname)
        input_username = input("İstifadəçi adınızı daxil edin : ")  ##
        input_telefon = input("Telefon nömrənizi daxil edin (51, 051 yox) : +994")
        check_functions.check_telefon(input_telefon)
        input_email = input("E-mailinizi daxil edin : ")
        check_functions.check_email(input_email)
        input_password = input("Şifrənizi daxil edin : ")
        check_functions.check_password(input_password)
        i += 1
        data['students'].append(
            create_dict(check_functions._name, check_functions._surname, check_functions._username,
                        check_functions.check_telefon,
                        check_functions.email, check_functions.password))

        user_add()
        with open('user_db.json', 'w') as databaza:
            json.dump(data, databaza)

# İstifadəçi əlavə etmək üçün funksiya (son)


# İstifadəçi məlumatlarını göstər (başlanğıc)
def data_show():
    i = 1
    for user in data['student']:
        print(f'student => {i}')
        print(user['ad'])
        print(user['soyad'])
        print(user['istifadeci'])
        print(user['telefon'])
        print(user['istifadeci'])
        print(user['password'])
        i += 1
# İstifadəçi məlumatlarını göstər (son)


# İstifadəçi məlumatlarını koda görə sil (başlanğıc)
def delete_user_by_password():
    delete_by_password = int(input("Məlumatları silmək üçün istifadəçi şifrəsini daxil edin : "))
    for user in istifadeci_bazasi:
        if delete_by_password == user.password:
            print(f"Təyin olunan istifadəçi ({user.name}) məlumatları silindi!")
            istifadeci_bazasi.remove(user)
            break
    else:
        print("Bu şifrədə istifadəçi tapılmadı!")


# İstifadəçi məlumatlarını koda görə sil (son)

# İstifadəçi məlumatlarını koda görə dəyiş (başlanğıc)
def change_data_by_password():
    change_by_password = input("Məlumat(lar)ı dəyişmək üçün istifadəçi şifrəsi daxil edin : ")
    for user in istifadeci_bazasi:
        if change_by_password == user.password:
            user.name = input("Yeni adınızı daxil edin : ")
            user.surname = input("Yeni soyadınızı daxil edin : ")
            user.username = input("Yeni istifadəçi adınızı daxil edin : ")
            user.telefon = input("Yeni telefon nömrənizi daxil edin : ")
            user.email = input("Yeni e-mailinizi daxil edin : ")
            istifadeci_bazasi.append(
                User(user.name, user.surname, user.username, user.telefon, user.email, user.password))
            print(f"{user.name} / {user.surname} / {user.username} / {user.password}")
        else:
            print("Bu şifrədə istifadəçi tapılmadı!")


def find_data_by_name():
    find_by_name = input("Məlumatı tapmaq üçün tələbə adını daxil edin : ")
    for user in istifadeci_bazasi:
        if find_by_name == user.name:
            print(
                f"{user.name} / {user.surname} / {user.username} / {user.telefon} / {user.email} / {user.password}")


find_data_by_name()
# İstifadəçi məlumatlarını koda görə dəyiş (son)


### not: is-le == in ferqi ###
