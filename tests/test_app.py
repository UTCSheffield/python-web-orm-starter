import pytest
from app import create_app
from todo import db, Todo, Category


@pytest.fixture
def app():
    """Configure the real app for testing."""
    test_app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })

    db_uri = test_app.config.get('SQLALCHEMY_DATABASE_URI', '')
    assert db_uri == 'sqlite:///:memory:', (
        f"Expected in-memory DB for tests, got {db_uri}"
    )

    with test_app.app_context():
        # Reset tables for a clean in-memory DB
        db.drop_all()
        db.create_all()

        # Seed test categories
        urgent = Category(name="Urgent")
        non_urgent = Category(name="Non-urgent")
        db.session.add(urgent)
        db.session.add(non_urgent)
        db.session.commit()

    yield test_app
    
    # Cleanup
    with test_app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'TodoApp' in response.data

def test_add_todo(app, client):
    with app.app_context():
        category = Category.query.first()
        todo = Todo(task='Test Task', done=False, user_id='default', category_id=category.id)
        db.session.add(todo)
        db.session.commit()
        assert Todo.query.count() >= 1
        
def test_add_todo_via_form(app, client):
    with app.app_context():
        category = Category.query.first()
        response = client.post('/add', data={
            'task': 'New Test Task',
            'category_id': category.id
        }, follow_redirects=True)
        assert response.status_code == 200
        assert Todo.query.filter_by(task='New Test Task').first() is not None

def test_privacy_page(client):
    response = client.get('/privacy')
    assert response.status_code == 200
    assert b'Privacy and Cookie Policy' in response.data
    assert b'do not collect any personal information' in response.data
