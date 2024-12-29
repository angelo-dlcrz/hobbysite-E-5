# Hobbysite with Django

This is a group project for my Software Tools and Development Frameworks class where we created a simple tech hobbysite using Django.

## How to Run

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository into your working machine.
2. Make sure that you have [Python](https://www.python.org/downloads/) installed in your machine. It is recommended to use Python 3.
3. [Install Django](https://www.geeksforgeeks.org/djnago-installation-and-setup/) if you haven't yet. Follow only up until Step 5 of `How to Install Django?`.
4. Open a command line in your working folder where `manage.py` is. Run the following command to install the needed dependencies.

```console
$ pip install -r requirements.txt
```

5. Create a `.env` file in your working directory.
6. Generate a `SECRET_KEY` by running this command in the command line.

```console
$ python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

7. Put this generated `SECRET_KEY` into your `.env` file. Save it afterwards.

```console
SECRET_KEY = '[YOUR_SECRET_KEY_HERE]'
```

8. On your command line, run the following commands to initialize the database and run the server

```console
$ py manage.py makemigrations
$ py manage.py migrate
$ py manage.py runserver
```

9. [Create a superuser](https://www.geeksforgeeks.org/how-to-create-superuser-in-django/) in Django. Afterwards, login to `http://127.0.0.1:8000/admin/`.
10. Populate the Wiki with at least one article on any article category using the admin tools.

After doing so, we're done!

## How to Use

1. Go to `http://127.0.0.1:8000/home/`
2. If you don't have an account yet, click `Sign Up` on the navigation bar and sign up for an account.
3. Log in to your account.
4. In the Merchandise tab, you can add tech products as you like.
5. In the Wiki tab, you can create tech articles as you like.
6. In the Forum tab, you can add tech threads like Reddit.
7. In the Commissions tab, you can add a new tech commission.
8. Click on your username on the navigation bar to view your profile's dashboard.
9. In the Profile tab, you can update your profile.
10. Finally, click the `Log Out` button to log out of the website whenever you want.

Enjoy!

## Credits

Thanks to my groupmates [James](https://github.com/kintengg), [Aster](https://github.com/astermangabat25), and [Dustin](https://github.com/DustinAgner27) for making this with me!