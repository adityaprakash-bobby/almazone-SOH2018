## setup
```bash
virtualevn venv
. venv/bin/activate
pip install -r requirements.txt
```
## database setup (Postgresql)
```bash
sudo systemctl start postgresql
python
>>>from flaskblog import create_app, db
>>>app = create_app()
>>>app.app_context().push()
>>>db.create_all()
>>>db.session.commit()
```

## Run the program:
```bash
python run.py
```

Open link 127.0.0.1:5000/ in browser.
