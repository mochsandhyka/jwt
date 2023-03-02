# JWT EXTENDED
## Requirements.txt
1. Flask == 2.2.3 (Framework)
2. python-dotenv == 1.0.0 (Membaca File .env)
3. psycopg2-binary == 2.9.5 (Membaca Postgres)
4. pony == 0.7.16 (ORM)
5. Flask-JWT-Extended == 4.4.4 (Json Web Token)
## Install Requirements.txt
1. python3 -m venv venv (Membuat Virtual Environtment)
2. source venv/bin/activate (Mengaktifkan venv)
3. pip install -r requirements.txt (Menginstall semua yang ada pada requirements.txt)
## .env File
1. FLASK_APP = main.py

## db.py
1. Menambahkan dictionary/object berupa provider,user,password,host,database

## Folder Model
1. Buat File base.py (Menampung semua import seperti configuration.py)
2. __init__.py (File yang pertamakali dieksekusi berisi db.bind(**db_settings.db_params) dan db.generate_mapping(create_tables=True) dan import semua class tabel db yang dibuat)


## configuration.py
1. From flask import Flask (Import Semua library yang dibutuhkan Flask)
2. app = Flask(__name__) (Run aplikasi dari .env)

## main.py
1. import flaskr.jwt (Import file jwt pada folder flaskr )

## flaskr
### jwt.py
1. 