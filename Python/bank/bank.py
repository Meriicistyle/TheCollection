# Known not working issues: Can't synchronize money between sections.


password = input("Şifrenizi oluşturunuz (4 haneli): ")
pasw = password
while True:
    para = 0
    pasw = input("Oluşturduğunuz şifreyi giriniz: ")
    if (pasw == password):
        print(
            """
            Hoş geldiniz, ne yapmak istersiniz?

            1. Para Yatır
            2. Para Çek
            3. Para Gönder
            4. Bakiye Görüntüle
            5. Şifreyi değiştir
            q. Çıkış
            """
        )

        istek = input("Isteğiniz: ")

        if (istek == "q"):
            break
        elif (istek == "1"):
            yat = int(input("Yatıracağınız Miktar: "))
            para += yat
            print(str(para) + " TL bakiyenizdir.")
        elif (istek == "2"):
            yat = int(input("Çekeceğiniz Miktar: "))
            para -= yat
            print(str(para) + " TL bakiyenizdir.")
        elif (istek == "3"):
            person = str(input("Göndereceğiniz kişinin adı: "))
            yat = int(input("Göndereceğiniz miktar: "))
            para -= yat
            print(person + " kişisine " + str(para * -1) + " TL gönderdiniz. Yeni bakiyeniz " + str(para) + " TL'dir.")
        elif (istek == "4"):
            print(str(para) + " TL bakiyenizdir.")
        elif (istek == "5"):
            print("Burayı henüz programlamadık")

        else:
            print("İsteğiniz hatalıdır, tekrar deneyiniz.")


    else:
        print("Şifreniz Yanlış!")
        break
