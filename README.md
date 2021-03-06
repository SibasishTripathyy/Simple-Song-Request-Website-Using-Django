# Simple-Song-Request-Website-Using-Django

## Demo
![demo-gif](demo.gif)

## Overview

This is a simple django based website which takes song requests via a form. After storing it into a table, it retrives the three most recent requests and displays them on the screen.

## Steps To Run Locally

First, clone this repository to your local machine using:

```
git clone https://github.com/SibasishTripathyy/Simple-Song-Request-Website-Using-Django
```

Then install all the requirements using:

```
pip install -r requirements.txt
```


Now the SECRET KEY portion isn't available. You can go to this [Stack Overflow](https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys/16630719#16630719) page to generate a random SECRET KEY.
After doing that, go to the settings.py file in the "DjangoProject1" directory. There you have to insert the newly generated random SECRET KEY by replacing one line of code in this portion of the settings file like this:

```
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Update secret key
# Insert your newly generated SECRET KEY here by replacing os.environ line with the key.
SECRET_KEY = "...insert your generated key here...keep the key inside quotes"
```

Apply all the migrations:

```
python manage.py migrate
```

Finally, run the server using the command:

```
python manage.py runserver
```

**Usually the server runs with "localhost:8000" port no. If not, then check the command prompt to find out the port no.**
