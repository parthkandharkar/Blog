from flaskblog import create_app, create_missing_tables

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        create_missing_tables()
    app.run(debug=True)