#криптор файла.txt (текст внутри блокнота)


from cryptography.fernet import Fernet

#декодирование файла
def decode():
# Загружаем ключ из файла или генерируем новый
    try:
        with open('key.key', 'rb') as file:
            key = file.read()
    except FileNotFoundError:
        # Если ключ не найден, генерируем новый
        key = Fernet.generate_key()
        with open('key.key', 'wb') as file:
            file.write(key)

    # Создаем объект дешифрования
    cipher = Fernet(key)

    # Дешифрование файла
    with open(putfilezak, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)

    # Сохранение расшифрованных данных в новый файл
    with open('декодированый_файл.txt', 'wb') as file:
        file.write(decrypted_data)

    print("Файл успешно расшифрован!")


#шифрование файла
def encrypt():
        # Генерация ключа
    key = Fernet.generate_key()

    # Сохранение ключа в файл
    with open('key.key', 'wb') as file:
        file.write(key)

    # Создание объекта шифрования
    cipher = Fernet(key)
        
    # Шифрование файла
    with open (putfiledec, 'rb') as file:
        data = file.read()
        encrypted_data = cipher.encrypt(data)

    # Сохранение зашифрованных данных в новый файл
    with open('зашифрованный_файл.txt', 'wb') as file:
        file.write(encrypted_data)

    print("Файл успешно зашифрован!")



if __name__ == "__main__":
    while True:
        option = input("Выберите вариант (1 - Декодировать, 2 - Закодировать, Enter - Выйти): ")
        if option == "1":
            putfilezak = input("Введите путь к зашифрованному файлу: ")
            decode()
            print("Декодированный файл: декодированый_файл.txt")
        elif option == "2":
            putfiledec = input("Введите путь к файлу: ")
            encrypt()
            print("Закодированный файл: зашифрованный_файл.txt")
        else:
            break
        