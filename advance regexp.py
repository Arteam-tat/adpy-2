from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
from pprint import pprint
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
phone_pattern = (
    r"(\+7|8)(\s*)(\(*)(\d{3})(\-*)(\)*)(\s*)(\d{3})(\-*)"
    r"(\s*)(\d{2})(\-*)(\s*)(\d{2})(\s*)(\(*)(доб\.)*(\s*)(\d+)*(\)*)"
)

phone_replace = r"+7(\4)\8-\11-\14\15\17\19"


contacts_list_new = list()
final_list = list()
for contacts in contacts_list:
    fio_list = " ".join(contacts[0:3]).split()
    if len(fio_list) != 3:
        fio_list.append("")
    full_fio_list = fio_list + contacts[3:]
    contact_string = ",".join(full_fio_list)
    contact_edit = re.sub(phone_pattern, phone_replace, contact_string)
    contact = contact_edit.split(",")
    contacts_list_new.append(contact)
    for c in contacts_list_new:
        for contact_in_final_list in final_list:
            if contact_in_final_list[:1] == c[:1]:
                final_list.remove(contact_in_final_list)
                c = [x if x != "" else y for x, y in zip(contact_in_final_list, c)]
        final_list.append(c)
## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_list)

