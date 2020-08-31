# Səhvliyi yoxlayan funksiyalar (ad, soyad, email, telefon, şifrə) ==> (başlanğıc)


def check_name(name):  # ?
    global _name
    while not name.isalpha():
        print("\"Adınızda yalnız əlifbadan istifadə edə bilərsiniz!\"")
        name = input("Yenidən adınızı yenidən daxil edin : ")
    _name = name


# Səhvliyi yoxlayan funksiyalar (ad, soyad, email, telefon, şifrə) ==> (başlanğıc)
def check_surname(surname):  # ?
    global _surname
    while not surname.isalpha():
        print("\"Yalnız əlifbadan istifadə edə bilərsiniz!\"")
        surname = input("Yenidən soyadınızı yenidən daxil edin : ")
    _surname = surname


def check_telefon(telefon):
    global _telefon
    while not len(telefon) == 9 or not telefon.isdigit():
        print("\"Səhvlik! +994 əlavə etməyin, yaxud yalnız rəqəmlərdən istifadə edin!\"")
        telefon = input("Yenidən telefon nömrənizi daxil edin : ")
    _telefon = telefon


def check_email(email):
    global _email
    while "@" not in email:
        print("\"E-mailinizdə \"@\" işarəsi mövcud deyil!\"")
        email = input("Yenidən e-mailinizi daxil edin : ")
    _email = email


def check_password(password):
    global _password
    while len(password) != 3 or not password.isdigit():
        print("\"Şifrə 3 rəqəmli olmalıdır!\"")
        password = input("Şifrənizi yenidən daxil edin : ")
    _password = password

# Səhvliyi yoxlayan funksiyalar (ad, soyad, email, telefon, şifrə) ==> (son)
