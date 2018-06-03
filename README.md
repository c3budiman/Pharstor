# Pharstor
A simple e-commerce for pharmacy store. made with django python


to install this :
1. Make sure u has python3.5, pip, setup-tools installed in your machine.
2. git clone https://github.com/c3budiman/Pharstor.git
3. cd Pharstor/
4. virtualenv .
5. . bin/activate
6. pip install -r requirement.txt
7. create database named 'pharstor' in your phpmyadmin or mysql.
8. specify database information in myshop/settings.py
it should look like this if u are running xampp :
<br>DATABASES = {
<br>    'default': {
<br>        'NAME': 'pharstor',
<br>        'ENGINE': 'django.db.backends.mysql',
<br>        'USER': 'root',
<br>        'PASSWORD': '',
<br>        'HOST': '127.0.0.1',
<br>        'PORT': '3306',
<br>    }
<br>}
9. python manage.py migrate
10. python manage.py runserver
11. done!
