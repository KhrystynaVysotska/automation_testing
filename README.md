<details>
<summary>Опис лабораторної роботи №1</summary>

# Лабораторна №1
## Завдання (основне)

Реалізувати скрипт для автоматизації наступних дій:

    a. Відкрити сторінку http://suninjuly.github.io/math.html
    b. Прочитати значення змінної x
    c. Обчислити математичну функцию від x: f(x) = ln(abs(12*sin(x))). Використовувати модуль math
    d. Ввести відповідь в текстове поле
    e. Вибрати checkbox "I'm the robot"
    f. Вибрати radiobutton "Robots rule!"
    g. Натиснути кнопку Submit

## Завдання (додаткове)

Написати скрипт реєстрації на сторінці селекторами, за XPath-селекторами:

http://demo-store.seleniumacademy.com/customer/account/create/

## Запуск

1. Установіть **selenium** клієнт для Python:
```
pip install selenium
```
2. Склонуйте проект:
```
git clone https://github.com/KhrystynaVysotska/automation_testing.git
```
3. Перейдіть у папку **lab_1**:
```
cd lab_1
```
4. Запустіть скрипт основного завдання:
```
py main_task.py
```
![image](https://user-images.githubusercontent.com/56559854/202797234-726d894c-b45a-44d4-a6d1-bbff352513e5.png)

5. Запустіть скрипт додаткового завдання:
```
py additional_task.py
```
![image](https://user-images.githubusercontent.com/56559854/202797365-e08886ba-9bac-4b7c-baec-66fe8bc63157.png)
</details>


<details>
<summary>Опис лабораторної роботи №2</summary>

# Лабораторна №2
## Завдання

Реалізувати скрипт для автоматизації наступних дій:

    a. Відкрити сторінку http://suninjuly.github.io/explicit_wait2.html 
    b. Дочекатись, коли ціна зменшиться до $100
    c. Натиснути кнопку "Book"
    d. Розв’язати математичну капчу та відправити розв’язок (завдання 1 лабораторної роботи №1)

## Запуск

1. Установіть **selenium** клієнт для Python:
```
pip install selenium
```
2. Склонуйте проект:
```
git clone https://github.com/KhrystynaVysotska/automation_testing.git
```
3. Перейдіть у папку **lab_2**:
```
cd lab_2
```
4. Запустіть скрипт завдання:
```
py waits.py
```
![image](https://user-images.githubusercontent.com/56559854/202799746-f6fcb704-f39a-444b-b7ba-340e614bd1ab.png)
</details>

<details>
<summary>Опис лабораторної роботи №3</summary>

# Лабораторна №3
## Завдання

Реалізувати unittest скрипт тестування наступного функціоналу ресурсу http://demo-store.seleniumacademy.com:

    a. Пошук різних груп товарів
    b. Реєстрації нового користувача та логін
    c. Довільний функціонал за вибором студента

## Запуск

1. Установіть **selenium** клієнт для Python:
```
pip install selenium
```
2. Склонуйте проект:
```
git clone https://github.com/KhrystynaVysotska/automation_testing.git
```
3. Перейдіть у папку **lab_3**:
```
cd lab_3
```
4. Щоб запустити всі тести, виконайте команду:
```
py launcher.py
```
5. Щоб запустити тести на функціонал **пошуку різних груп товарів**:

- _відкрийте у редакторі `launcher.py`_
- _у лінійці 7 змініть патерн пошуку тестових файлів з `test_*.py` на `test_categories.py`:_

    _From_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_*.py")
    ```
    _To_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_categories.py")
    ```
- _збережіть зміни та виконайте команду:_
    ```
    py launcher.py
    ```
6. Щоб запустити тести на функціонал **реєстрації нового користувача**:

- _відкрийте у редакторі `launcher.py`_
- _у лінійці 7 змініть патерн пошуку тестових файлів з `test_*.py` на `test_registration.py`:_

    _From_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_*.py")
    ```
    _To_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_registration.py")
    ```
- _збережіть зміни та виконайте команду:_
    ```
    py launcher.py
    ```
7. Щоб запустити тести на функціонал **логін користувача**:

- _відкрийте у редакторі `launcher.py`_
- _у лінійці 7 змініть патерн пошуку тестових файлів з `test_*.py` на `test_login.py`:_

    _From_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_*.py")
    ```
    _To_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_login.py")
    ```
- _збережіть зміни та виконайте команду:_
    ```
    py launcher.py
    ```
8. Щоб запустити тести на функціонал за довільним вибором студента (**функціонал корзини**):

- _відкрийте у редакторі `launcher.py`_
- _у лінійці 7 змініть патерн пошуку тестових файлів з `test_*.py` на `test_cart_*.py`:_

    _From_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_*.py")
    ```
    _To_
    ```
    package_tests = loader.discover(start_dir=folder_name, pattern="test_cart_*.py")
    ```
- _збережіть зміни та виконайте команду:_
    ```
    py launcher.py
    ```
</details>
