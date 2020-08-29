class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password

    def show(self):
        return f"<Sizin adınız {self.name}, soyadınız isə {self.surname}>"


istifadeci_bazasi = []


# İstifadəçi əlavə etmək üçün funksiya (başlanğıc)
def user_add():
    i = 0
    user_count = int(input("Neçə istifadəçi daxil etmək istəyirsiniz? (rəqəm daxil edin) : "))
    while i < user_count:
        input_name = input("Adınızı daxil edin : ")
        input_surname = input("Soyadınızı daxil edin : ")
        input_username = input("İstifadəçi adınızı daxil edin : ")
        input_password = input("Şifrənizi daxil edin : ")
        i += 1
        istifadeci_bazasi.append(User(input_name, input_surname, input_username, input_password))


user_add()


# İstifadəçi əlavə etmək üçün funksiya (son)


# İstifadəçi məlumatlarını göstər (başlanğıc)
def data_show():
    data = istifadeci_bazasi
    print(data)


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


delete_user_by_password()
# İstifadəçi məlumatlarını koda görə sil (son)
