import check_functions
import json

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
    for user in data['students']:
        if delete_by_password is user['password']:
            print(f"Təyin olunan istifadəçi ({user['name']}) məlumatları silindi!")
            data['students'].remove(user)
            with open('user_db.json', 'w') as connect:
                json.dump(data, connect)
            break  #
        else:
            print("Bu şifrədə istifadəçi tapılmadı!")


# İstifadəçi məlumatlarını koda görə sil (son)

# İstifadəçi məlumatlarını koda görə dəyiş (başlanğıc)
def change_data_by_password():
    change_by_password = input("Məlumat(lar)ı dəyişmək üçün istifadəçi şifrəsi daxil edin : ")
    for user in data['students']:
        if change_by_password is user['password']:
            new_name = input("Adınızı daxil edin!")
            while not new_name.isalpha():
                print("\"Adınızda yalnız əlifbadan istifadə edə bilərsiniz!\"")
                new_name = input("Yenidən adınızı yenidən daxil edin : ")
            user['ad'] = new_name
            new_surname = input("Soyadınızı daxil edin!")
            while not new_surname.isalpha():
                print("\"Yalnız əlifbadan istifadə edə bilərsiniz!\"")
                new_surname = input("Yenidən soyadınızı yenidən daxil edin : ")
            user['surname'] = new_surname
            new_telefon = input('Telefon nömrənizi daxil edin : ')
            while not len(new_telefon) == 9 or not new_telefon.isdigit():
                print("\"Səhvlik! +994 əlavə etməyin, yaxud yalnız rəqəmlərdən istifadə edin!\"")
                new_telefon = input("Yenidən telefon nömrənizi daxil edin : ")
            user['telefon'] = new_telefon
            new_email = input('E-mailinizi daxil edin : ')
            while "@" not in new_email:
                print("\"E-mailinizdə \"@\" işarəsi mövcud deyil!\"")
                new_email = input("Yenidən e-mailinizi daxil edin : ")
            user['email'] = new_email
            new_password = input('Şifrənizi daxil edin : ')
            while len(new_password) != 3 or not new_password.isdigit():
                print("\"Şifrə 3 rəqəmli olmalıdır!\"")
                new_password = input("Yenidən şifrənizi daxil edin : ")
            user['password'] = new_password
            with open('user_db.json', 'w') as connect:
                json.dump(data, connect)
                break

# İstifadəçi məlumatlarını koda görə dəyiş (son)


### not: is-le == in ferqi ###
