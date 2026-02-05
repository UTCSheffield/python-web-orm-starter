# Python Web ORM Starter App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![Render](https://img.shields.io/badge/Deploy-Render-purple)

A simple Python Todo Web App and a stripped-down version of
https://github.com/UTCSheffield/python-web-oauth-orm-rest-starter. This version
removes auth, admin, and API layers so you can concentrate on data classes and
page routes.

---

## Features

### Flask

- [Flask](https://flask.palletsprojects.com/en/stable/) based Python Webserver with routing (a function for each url endpoint users can visit)
- HTML / [Jinja templates](https://jinja.palletsprojects.com/en/stable/templates/) for looping though and outputting data.
- todo.py contains the endpoints for the Todo app

---

### SQLAlchemy & SQLite / PostgreSQL

- SQL Databases the modern way
- Managed by [SQLAlchemy](https://www.sqlalchemy.org/) an ORM /  [Object Relationship Mapper](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) which allows you to write classes that define the data and provides the storage & [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) for you.

---

###  [Object Relationship Mapper](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)

- ORMs build the database for you from your classes so you define what you want to store how it connects together and any extras calculations / functions you need .
- Start with SQLite but you can move to proffesional systems like PostgreSQL or others when you are ready.
- todo.py includes the Todo class that provdes all you need for the building of the database and all the [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete).

---

### Render & Github Actions

- Ready for [Render](https://render.com/)  deployment so you can publish and use the site online for free (there are some speed limitations)
- GitHub Actions CI/CD to build the site when you commit a working version
- Can be upgraded to use a free PostgreSQL database server (but there are some other steps)

---

## Setup

### Start from the Template

1. Login to [github.com](https://github.com/)
2. Go to the github repository [https://github.com/UTCSheffield/python-web-orm-starter](https://github.com/UTCSheffield/python-web-orm-starter)
3. Click the green "Use this template" button at the top of the page
4. Select "Create a new repository"
5. Fill in your new repository details:
   - Choose a repository name
   - Add a description (optional)
   - Choose Public or Private visibility
6. Click "Create repository from template"
7. Your new repository will be created with all the template files

---

### Clone your Repository locally

**Using GitHub Desktop:**

1. On the GitHub page for your new repository
2. Click the green "Code" button
3. Click "Open with GitHub Desktop"
4. You may need to login to GitHub Desktop if you haven't already
5. You may be prompted to choose a local path to clone the repository to
6. Click 'Open in Visual Studio Code' to open the project in VS Code

---

**Using Git Command Line:**

```bash
git clone https://github.com/UTCSheffield/python-web-orm-starter.git
cd python-web-orm-starter
```

---

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

### Environment Configuration (.env)

```bash
cp .env.example .env
```

---

## Running the Application

Start the Flask development server:

```bash
python3 -m flask run --host=localhost --port=5000
```

The app will be available at [http://localhost:5000](http://localhost:5000)

Try it and create a few tasks!

---

## The Database

This code uses [SQLAlchemy](https://www.sqlalchemy.org/) to set up classes that have methods to talk to many [databases](https://docs.sqlalchemy.org/en/20/dialects/index.html). We use **SQLite for simplicity and easy local development**.

### Local Development (SQLite)

The database file is stored in `/instance/todo.db`

Hopefully Visual Code has promoted you to install the recommended extensions including the SQLite extension. and so todo.db should appear in the left hand side explorer view with a red icon.

Have a look, can you see the tables and data?
