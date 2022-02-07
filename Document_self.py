documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

# 1 функция p
def get_name(usernumber):
  for d in documents:
    if usernumber == d['number']:
      return d['name']
  return 'Документ введен неверно'

# 2 функция s
def get_shelf_number(usernumber):
  for directkey, directvalue in directories.items():
    if usernumber in directvalue:
      doc_num_res = 'Документ находится на полке № : ' + directkey
      return doc_num_res
  return 'Данный документ не найден'

# 3 функция l
def all_list():
  for l in documents:
    print (l ['type'], l['number'], l ['name'])

# 4 функция a
def set_doc(doc_number,doc_type,doc_name,doc_shelf):
  if doc_shelf in directories.keys():
    new_doc = {"type": doc_type,"number": doc_number,"name": doc_name}
    documents.append(new_doc)
    directories[doc_shelf].append(doc_number)
    return 'Документ добавлен'
  else:
    return 'Нет выбранной полки'

# 5 функция d
def delete_doc(del_doc):
  for z in documents:
    if del_doc == z['number']:
      documents.remove(z)
      break
  else:
    return 'Документ введен неверно'

  for directvalue in directories.values():
    if del_doc in directvalue:
      directvalue.remove(del_doc)
      return 'Документ удален'

# 7 функция as
def new_shelf (add_shelf):
  if add_shelf in directories.keys():
    return 'Данная полка уже существует!'
  directories.update({add_shelf:[]})
  return 'Создана новая полка'

#  6  функция m
def purpose_self (usernumber , make_shelf):
  if make_shelf in directories.keys():
    for directvalue in directories.values():
      if usernumber in directvalue:
        directvalue.remove(usernumber)
        directories[make_shelf].append(usernumber)
        break
    else:
      print ('Документ не найден')
  else:
    print ('Данной полки не существует!')


if __name__ == '__main__':
  print ('Список существующих команд:')
  print ('p - Имя человека по номеру документа')
  print ('s - Номер полки по номеру документа')
  print ('l - Список всех документов')
  print ('a - Добавление нового документа')
  print ('as - Создание новой полки')
  print ('m - Перемещение документа')
  print ('d - Удаление документа')

  command = input ('Введите команду : ')
  if command == 'p':
    usernumber = input ('Введите номер документа : ')
    print (get_name(usernumber))
  elif command == 's':
    usernumber = input ('Введите номер документа : ')
    print (get_shelf_number(usernumber))
  elif command == 'l':
    all_list()
  elif command == 'a':
    doc_number = input('Введите номер документа : ')
    doc_type =input('Введите тип документа : ')
    doc_name =input('Введите Имя и Фамилию : ')
    doc_shelf =input('Введите № полки для документов : ')
    print (set_doc(doc_number,doc_type,doc_name,doc_shelf))
  elif command == 'as':
    add_shelf = input('Введите номер полки :  ')
    print(new_shelf(add_shelf))
  elif command == 'm':
    usernumber = input('Введите номер документа :  ')
    make_shelf = input('Введите полку куда переложить документ :  ')
    purpose_self(usernumber , make_shelf )
  elif command == 'd':
    del_doc = input('Введите номер документа :  ')
    print (delete_doc(del_doc))
  else:
    print('Вы ввели неверную команду')




  
   

