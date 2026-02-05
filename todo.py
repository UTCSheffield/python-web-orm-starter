# todo.py - todo functionality
from flask import Blueprint, render_template, request, redirect

# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
from sqlalchemy import ForeignKey


# Base that adds dataclass behaviors to mapped classes
class Base(MappedAsDataclass, DeclarativeBase):
    pass


todo_bp = Blueprint('todo', __name__)
db = SQLAlchemy(model_class=Base)


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return self.name


class Todo(db.Model):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    task: Mapped[str] = mapped_column(db.String(200), nullable=False)
    user_id: Mapped[str] = mapped_column(db.String(100), nullable=False, default="default")
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False, default=1)
    done: Mapped[bool] = mapped_column(db.Boolean, default=False)

    @property
    def category(self):
        return db.session.get(Category, self.category_id)

@todo_bp.route('/')
def home():
    todos = Todo.query.filter_by(user_id="default").all()
    categories = Category.query.all()
    return render_template('index.html', todos=todos, categories=categories)


@todo_bp.route('/add', methods=['POST'])
def add():
    task_text = request.form['task']
    category_id = request.form.get('category_id', type=int)
    if not category_id:
        return redirect('/')
    new_task = Todo(task=task_text, category_id=category_id, user_id="default")
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')


@todo_bp.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    todo = Todo.query.get(todo_id)
    if todo and todo.user_id == "default":
        todo.done = not todo.done
        db.session.commit()
    return redirect('/')


@todo_bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    if todo and todo.user_id == "default":
        db.session.delete(todo)
        db.session.commit()
    return redirect('/')


def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # Seed initial categories if they don't exist
        if Category.query.count() == 0:
            urgent = Category(name="Urgent")
            non_urgent = Category(name="Non-urgent")
            db.session.add(urgent)
            db.session.add(non_urgent)
            db.session.commit()
            
        if Todo.query.count() == 0:
            mreggleton = Todo(task="Checking your Todo App!", done=False, user_id="default", category_id=non_urgent.id)
            db.session.add(mreggleton)
            db.session.commit()
