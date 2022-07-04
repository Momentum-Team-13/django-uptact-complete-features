# Uptact

This is your first Django project. For this project, functionality has already been added to this sample Django application. You will add new functionality throughout the project in order to better understand how all the pieces of Django work together.

## Getting this project set up

You must have [Poetry](https://python-poetry.org/) installed. This will allow you to get all dependencies of this project installed on your computer. You should already have Poetry installed, but if not, run the following command:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Once you ensure you have Poetry installed, run the following command inside this project's directory:

```
poetry install
```

Poetry uses a concept called a "virtualenv" in order to isolate the dependencies of this project from any other project. This requires you to run a command when you want to start working on this project. Before working on the project, run:

```
poetry shell
```

This will change your terminal to use the virtualenv for this project. *You must run this command in any new terminal you open.* You will know if you are in the virtualenv because your prompt will change to show you. You should have the name of the virtualenv on your prompt, like the following:

```
django--uptact is 📦 v0.1.0 via 🐍 v3.7.7 (uptact-fsCrKkW6-py3.7)
❯
```

Note `(uptact-fsCrKkW6-py3.7)` at the end -- that's the virtualenv. If you need to exit the virtualenv, simply close your terminal window or run `exit`.

If you get a `SECRET_KEY` error when you run your django server, you'll need to make sure Django can find that variable, which it is looking for in a `.env` file in the `uptact` project directory (see `django-environ` below). This repo provides a `.env.sample` so you can rename or copy that file so that is is named `.env`.
```
$ cp uptact/.env.sample uptact/.env
```

## First assignment

For the first assignment, spend time familiarizing yourself with Django. Look at the `uptact` directory (the _project directory_) and the `contacts` directory (an _app directory_). Answer the following questions for yourself:

* If I wanted to add a new URL to this project, what two files would I edit?
* If I wanted to add a birthday to each contact, what file would I edit?

Then do the following steps:

1. Add a birthday field to the `Contact` model. This field should be of type `DateField` and should be allowed to be null and empty.
2. Make sure you can edit the birthday by changing the `ContactForm`.
3. Add the ability to display the birthday on the list of contacts. You will have to edit `templates/contacts/list_contacts.html`.

When you get through that, add a birthday to one of your contacts to test out your code.

## Second assignment

With this assignment, we are going to explore relationships between models, and how URLs and views work.

Answer the following questions:

* If I wanted to add a new model, where would I do that?
* If I wanted to connect the new model to the `Contact` model, how would I do that?

Then do the following steps:

1. Add a new model, `Note`, to the `contacts` app. This model should contain text for the note and the date/time of the note. Look at the `auto_now_add` option for the `DateTimeField` to have the date/time automatically populated.
2. Connect the `Note` model to the `Contact` model using a `ForeignKey`.
3. Use the Django console to add a note to one of your contacts.
4. Make a new view and template to see an individual contact. The URL for this view should be `contacts/<int:pk>/`. Show the notes for that contact on this individual view. Otherwise, this page can look like an individual contact on the contacts list page.

## Third assignment

With this assignment, we are going to explore forms.

Previously, you added a `Note` model, but had no ability to create new notes through your Django application. Now do the following steps:

1. Add a new form called `NoteForm`. This form should let you edit only one field, the text of the note.
2. Add a new view to accept this form via `POST` request and add a new note to a specific user. The user will be specified via the URL, which should be `contacts/<int:pk>/notes/`.
3. On the individual contact view that you previously added, add a form to create new notes. When the note is created, redirect back to the contact view.

Test this by adding some notes to individual contacts.



## About this project

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- There is a custom user model defined in `users.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Poetry](https://python-poetry.org/) is used to manage dependencies.
