from app import create_app

app = create_app()

# with app.app_context():
#     from app.extensions import db
#     print('deleting')
#     db.drop_all()
#     print('Creating database tables...')
#     db.create_all()
#     print('Database tables created.')


if __name__ == '__main__':
    app.run()
