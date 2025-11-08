def obfuscator(func):
    def wrapper():
        results = func()

        # Обрабатываем имя: оставляем первый и последний символ, остальные заменяем на *
        if "name" in results and results["name"]:
            name = results["name"]
            if len(name) > 2:
                results["name"] = name[0] + "*" * (len(name) - 2) + name[-1]
            elif len(name) == 2:
                results["name"] = name[0] + "*"
            else:
                results["name"] = name  # для строк из 1 символа

        # Обрабатываем пароль: все символы заменяем на *
        if "password" in results and results["password"]:
            results["password"] = "*" * len(results["password"])

        return results

    return wrapper


@obfuscator
def get_credentials():
    return {"name": "StasBasov", "password": "iamthebest"}


print(get_credentials())
