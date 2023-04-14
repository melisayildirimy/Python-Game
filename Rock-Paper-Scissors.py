import random

def get_user_choice():
    """Kullanıcıdan seçimini alır ve geçerli bir seçim yapılıncaya kadar tekrar eder."""
    while True:
        user_choice = input("Taş, Kağıt ya da Makas? ").lower()
        if user_choice in ['taş', 'kağıt', 'makas']:
            return user_choice
        else:
            print("Geçersiz seçim. Lütfen 'taş', 'kağıt' ya da 'makas' arasından birini seçin.")

def get_computer_choice():
    """Bilgisayarın seçimini yapar."""
    choices = ['taş', 'kağıt', 'makas']
    # Yapay zeka: Bilgisayarın seçimini rastgele yapmak yerine daha akıllıca bir strateji uygularız.
    # Örneğin, bilgisayar daha önceki seçimlere göre bir tercih yapabilir.
    # Aşağıdaki örnekte, bilgisayarın son 3 seçimine göre strateji uygulanmıştır.
    if len(computer_choices) >= 3:
        last_three_choices = computer_choices[-3:]
        if last_three_choices.count('taş') >= 2:
            return 'makas'
        elif last_three_choices.count('kağıt') >= 2:
            return 'taş'
        elif last_three_choices.count('makas') >= 2:
            return 'kağıt'
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Kullanıcının seçimine ve bilgisayarın seçimine göre kazananı belirler."""
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == 'taş' and computer_choice == 'makas') or \
         (user_choice == 'kağıt' and computer_choice == 'taş') or \
         (user_choice == 'makas' and computer_choice == 'kağıt'):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def play_again():
    """Kullanıcının tekrar oynamak isteyip istemediğini kontrol eder."""
    play_again = input("Tekrar oynamak istiyor musunuz? (E/H) ").lower()
    return play_again == 'e'

def main():
    """Taş-kağıt-makas oyununu başlatır."""
    print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        computer_choices.append(computer_choice) # Bilgisayarın seçimini kaydediyoruz
        print(f"Siz: {user_choice}")
        print(f"Bilgisayar: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        if not play_again():
            break
if __name__ == '__main__':
    computer_choices = [] # Bilgisayarın seçimlerini kaydedeceğimiz bir liste oluşturuyoruz
    main()
