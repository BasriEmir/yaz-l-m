import string
import random

def generate_pin():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(4))

def verify_pin(pin, correct_pin):
    return pin == correct_pin

def main():
    pin = generate_pin()
    attempts = 0

    while attempts < 3:
        entered_pin = input("Lütfen pin kodunuzu giriniz: ")

        if verify_pin(entered_pin, pin):
            print("Giriş Başarılı")
            break
        else:
            attempts += 1
            if attempts == 3:
                print("Hata: 3 denemeden fazla yanlış giriş yaptınız.")
            else:
                print("Hata: Pin kodu yanlış. Tekrar deneyiniz.")

if __name__ == "__main__":
    main()