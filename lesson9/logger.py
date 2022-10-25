def log_read():
    f = open('file.txt', 'r', encoding="utf-8")
    listFilter = list(filter(lambda x: x != "", f.read().split("//")))
    f.close()
    return listFilter


def log_change(full_list):
    f = open('file.txt', 'w', encoding="utf-8")
    f.write(f"{full_list[0]}//{full_list[1]}//{full_list[2]}")
    f.close()

def log_clear():
    f = open('file.txt', 'w', encoding="utf-8")
    f.write(f"")
    f.close()
