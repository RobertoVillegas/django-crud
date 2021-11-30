# DJANGO CRUD

Django CRUD for managing beer brands, containers and products.

## Features

- CRUD Application
- Ajax CRUD Application
- Form Validation
- Modals

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_NAME=`

`DATABASE_USER=`

`DATABASE_PASS=`

## Deployment

To deploy this project, do the following:

1. If you don't already have it, install [Python](https://www.python.org/).

2. I recommend using a virtual environment to run this example, but it's not mandatory. To initialize a virtual environment:

```bash
pip install virtualenv
virtualenv env
source env/bin/activate
```

3. Clone this repository and navigate into it.

```
git clone https://github.com/RobertoVillegas/django-crud.git
cd django-crud
```

4. Install all required libraries within the virtual environment.

```
pip install -r requirements
```

5. Create a MySQL database. [Here's a tutorial using the CLI.](https://www.inmotionhosting.com/support/server/databases/create-a-mysql-database/)

6. Add the environment variables of your database to your .env file.

```
DATABASE_NAME=database-name
DATABASE_USER=username
DATABASE_PASS=password
```

7. Migrate the models to the database.

```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

8. Run the application.

```
python manage.py runserver
```

9. Open <http://127.0.0.1:8000>

10. Create a superuser for the admin panel.

```
python manage.py createsuperuser (enter username, email, password)
```

11. Login to <http://127.0.0.1:8000/admin>

## License

[MIT](https://choosealicense.com/licenses/mit/)
