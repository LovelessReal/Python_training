print ('Введите свое имя')
user_name = input ('Меня зовут ')
print('Привет' + ' ' + user_name)

print ('Введите свой возраст числом')
user_age = input ()
user_age = int(user_age) #преобразовываем строку в числовой тип данных
if user_age < 18:
     print ('Да ты еще совсем молод!')
else:
    print('Да ты жизнь повидавший')
     