# криптор текста на русском из cmd

def decode(s):
    zac = 'абсвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    dec = 'Λß↻Ð☰∲ç╫¡¿├↑ღ∏☐þ¶┏§⊥üƴ₪✕¥ᶾ '
    
    ans = ''
    for c in s:
        try:
            ans += zac[dec.index(c)]
        except ValueError:
            ans += c
    
    return ans

def encode(s):
    zac = 'абсвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    dec = 'Λß↻Ð☰∲ç╫¡¿├↑ღ∏☐þ¶┏§⊥üƴ₪✕¥ᶾ '
    
    ans = ''
    for c in s:
        try:
            ans += dec[zac.index(c)]
        except ValueError:
            ans += c
    
    return ans

if __name__ == "__main__":
    while True:
        option = input("Выберите вариант (1 - Декодировать, 2 - Закодировать, Enter - Выйти): ")
        if option == "1":
            encoded_string = input("Закодированная строка: ")
            print("Декодированная строка:", decode(encoded_string))
        elif option == "2":
            plain_string = input("Обычное слово: ")
            print("Закодированная строка:", encode(plain_string))
        else:
            break
        
