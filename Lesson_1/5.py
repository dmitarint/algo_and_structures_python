#5.	Пользователь вводит две буквы. Определить, на каких местах
# # алфавита они стоят, и сколько между ними находится букв.
x1=ord(input('введите первую букву: '))
x2=ord(input('введите первую букву: '))
print('Первая буква находится на %d месте алфавита'% (x1-96))
print('Вторая буква находится на %d месте алфавита'% (x2-96))
print('Между буквами находится %d символов'%int(abs(x2-x1)))
