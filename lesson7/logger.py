def log_answ(name, phone):
    with open('./lesson7/file.txt', 'a', encoding="utf-8") as f:
        f.write(f'{name} || {phone}\n')
        return "Новый контакт создан"
