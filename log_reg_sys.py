istifadeci_bazasi = []


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


def check_name(name):  # ?
    while not name.isalpha():
        print("\"Adınızda yalnız əlifbadan istifadə edə bilərsiniz!\"")
        name = input("Yenidən adınızı yenidən daxil edin : ")


# Səhvliyi yoxlayan funksiyalar (ad, soyad, email, telefon, şifrə) ==> (başlanğıc)
def check_surname(surname):  # ?
    while not surname.isalpha():
        print("\"Yalnız əlifbadan istifadə edə bilərsiniz!\"")
        surname = input("Yenidən soyadınızı yenidən daxil edin : ")


def check_telefon(telefon):
    while not len(telefon) == 9 or not telefon.isdigit():
        print("\"Səhvlik! +994 əlavə etməyin, yaxud yalnız rəqəmlərdən istifadə edin!\"")
        telefon = input("Yenidən telefon nömrənizi daxil edin : ")


def check_email(email):
    while "@" in email == False:
        print("\"E-mailinizdə \"@\" işarəsi mövcud deyil!\"")
        email = input("Yenidən e-mailinizi daxil edin : ")


def check_password(password):
    while len(password) != 3 or not password.isdigit():
        print("\"Şifrə 3 rəqəmli olmalıdır!\"")
        password = input("Şifrənizi yenidən daxil edin : ")


# Səhvliyi yoxlayan funksiyalar (ad, soyad, email, telefon, şifrə) ==> (son)

# İstifadəçi əlavə etmək üçün funksiya (başlanğıc)
def user_add():
    i = 0
    user_count = int(input("Neçə istifadəçi daxil etmək istəyirsiniz? (rəqəm daxil edin) : "))
    while i < user_count:
        input_name = input("Adınızı daxil edin : ")
        check_name(input_name)
        input_surname = input("Soyadınızı daxil edin : ")
        check_surname(input_surname)
        input_username = input("İstifadəçi adınızı daxil edin : ")  ##
        input_telefon = input("Telefon nömrənizi daxil edin (51, 051 yox) : ")
        check_telefon(input_telefon)
        input_email = input("E-mailinizi daxil edin : ")
        check_email(input_email)
        input_password = input("Yeni şifrənizi daxil edin : ")
        check_password(input_password)
        i += 1
        istifadeci_bazasi.append(
            User(input_name, input_surname, input_username, input_telefon, input_email, input_password))


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
# İstifadəçi məlumatlarını koda görə dəyiş (son)
