
## OpenWeather API

This project is about an api which receives a request width a slug as city name and sends a<br />
request for OpenWeather web service , after getting back the result it saves its into database.<br />
####The project has decided into three parts
* openweatherapi which sends request to the OpenWeather
* wather Django app which parse re sponses and savethem in the database.
* Test section which does unittest different parts of project.
<br>



#### Installation:
1. If you os is Ubuntu there is a virtualenv ready which you can activate it by following command:
>source venv/bin/activate

otherwise it's better to create your own virtualenv
2. Setup project with bellow command:
>python3 setup.py install
3. got to the root project directory
>cd mysite
4. Run Django  
>python manage.py runserver

####How to use:
1.You can send request to the following list :<br>
http://localhost:8000/weather/{cityName}
<br>
Example: <br>
http://localhost:8000/weather/berlin



####Test:
For test i decided to use pytest.For unittest use following commands to run different
tests.<br>
Please got to mysite/tests folder
1.Testing OpenWaather webservice connection:
>python -m pytest openapi_test.py

2.Testing wather Django api :
>python -m pytest weather_api_test.py 

3.Testing data entry to database:
>python3 -m pytest database_test.py 

####Credencials:
<br>
For Login to Django Admin Panel
<bir>
http://localhost/admin
<br>
Username: "Amir"
<br>
Password: "Eddy@747" (Eddy is my lovely dog)

####Used technologies:
* Django(a high-level Python web framework that encourages rapid development and clean, pragmatic design.)
* Python Programming Language
* Django Rest Framework for designing a restful application
* Numpy library to create a uniform array for get temperature

####Next Stage
Dockerized the project and create two containers for database and 
rest of project and also I like to use my favourite database Postgres
instead of sqlite.




