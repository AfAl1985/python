print("Задача 3. Микроволновка")
# Что нужно сделать
# Мы разрабатываем микропрограмму — таймер обратного отсчета для микроволновых печей.
# Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране.
# В нашем случае будем выводить в консоль сообщение с обратным отсчетом в секундах от “reverse_timer”
# до момента готовности, то есть «0» секунд, и спрашивать пользователя, готов ли он забрать еду.
# Пользователь в любой момент может прервать режим разогрева,
# введя «1» (то есть ответить «Да, еда готова»), 
# тогда программа выводит на экран сообщение «Ваша еда готова, можете забрать» и показывает,
# на какой секунде был прерван таймер.
# Если пользователь отвечает «0», что равноценно «Нет», то таймер уменьшается. Когда он достигнет «0» секунд,
# выводим сообщение «Ваша еда готова, осторожно горячo!»
# В данном задании используем цикл for.
# “reverse_timer” – переменная счетчик, значение которой запрашиваем у пользователя через функцию ввода input.
# Задайте время до обнуления таймера.
# Используйте цикл for.
# На каждой итерации задавайте персонажу вопрос, хочет ли он сейчас остановить разогрев или нет.

reverse_timer = int(input("How much time do you need to warm up the food?: "))

for time in range(reverse_timer, -1, -1):
    if time == 0:
        print("The food is hot, take care")
    print(time)
    user = int(input("Take out the food? 1 - yes 0 - no "))
    if user == 1:
        print("The food is ready")
        print(time)
        break
    else:
        print("Continue")
print("The food is hot, take care")





