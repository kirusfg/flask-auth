# Flask Auth

## Install:
```sh
python3 -m venv venv
python3 -m pip install -r requirements.txt
```

## Run:
```sh
flask --app auth init-db
flask --app auth run --debug
```

The app is available at `localhost:5000`. Routes are:
```
/
/auth/register
/auth/login
/auth/logout
```

## Check the database:
```sh
sqlite3 instance/local.db
sqlite> SELECT * FROM user;
```
