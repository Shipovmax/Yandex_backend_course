class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def process_text(self, text, shift, is_encrypt):
        """Универсальный метод для шифрования/дешифрования"""
        result = []
        text = text.lower()

        # Если это дешифрование, меняем направление сдвига
        if not is_encrypt:
            shift = -shift

        for char in text:
            if char in self.alphabet:
                # Находим текущую позицию символа
                current_index = self.alphabet.index(char)
                # Вычисляем новую позицию с учетом сдвига и цикличности
                new_index = (current_index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                # Оставляем символы не из алфавита без изменений
                result.append(char)

        return "".join(result)


# Проверка:
cipher_master = CipherMaster()
print(
    cipher_master.process_text(
        text="Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь",
        shift=2,
        is_encrypt=True,
    )
)
print(
    cipher_master.process_text(
        text="Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ",
        shift=-3,
        is_encrypt=False,
    )
)
