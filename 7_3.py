class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def _process_text(self, text, shift):
        """Вспомогательный метод для шифрования/дешифрования"""
        result = []
        text = text.lower()

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

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        return self._process_text(original_text, shift)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        return self._process_text(cipher_text, -shift)


cipher_master = CipherMaster()
print(
    cipher_master.cipher(
        original_text="Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь",
        shift=2,
    )
)
print(
    cipher_master.decipher(
        cipher_text="Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ",
        shift=-3,
    )
)
