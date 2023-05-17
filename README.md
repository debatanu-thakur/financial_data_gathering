# Financial service
## Prerequisits
1. Please download the api key and store it in `.env` in the root folder.
2. Please store it as `API_KEY=<api_key>`

## Solution
1. To start the application
```
docker compose up -d
```
2. To generate and add data to the the psql database
```
docker-compose exec web python3 get_raw_data.py
```

3. To run unit and integration tests
```
$  docker-compose exec web pytest --cov=financial # for coverage
```

## Chosen technology
1. Used Python Flask to build website. The reason for this is because flask is light weight and provides with a lot of libraries to create web services and also db orms.
2. Used flask sqlalchemy db orm to setup db model and used flask-migration to create database tables.
3. Used Postgres SQL, because I wanted to use SQL, relational database and also have provisioning for using no-sql if need be.
4. Used pytest for unit test, as it provides fixtures which simplifies lot of boilerplate code needed to be written to setup tests and tear it down once the tests are done.
5. Used docker to setup testing environment. That helped with setup installation of dependencies agnostic of my development laptop os and helped setup a dev environment of calling between web service and db service.
6. With regards to securely storing the API_KEY
    - The API key can be stored in the repository by encrypting it while pushing it to git and decrypting it while pulling it using - [git-crypt](https://www.agwa.name/projects/git-crypt/)
    - We can also use docker secrets to store the encrypted API key and then decrypt and provide it during application run.
    - The idea is to store the API key in an encrypted datastore so that we can fetch and decrypt it while running the web application.
