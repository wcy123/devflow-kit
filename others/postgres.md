# install postgreSql



https://www.enterprisedb.com/postgres-tutorials/how-install-postgres-ubuntu

``` console
% sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
% wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
% sudo apt-get update
% sudo apt-get install -y postgresql-11
% id postgres
% sudo adduser chunywan postgres
```

``` console
% ps -aux | grep postgres
% sudo  /etc/init.d/postgresql start
% ps -aux | grep postgres
% sudo  /etc/init.d/postgresql status
```



https://stackoverflow.com/questions/11919391/postgresql-error-fatal-role-username-does-not-exist

``` console
% sudo -u postgres -i
postgres % createuser chunywan
postgres % psql
postgres=# ALTER USER chunywan Superuser CreateDB;
postgres=# \du;
postgres=# exit;
postgres % exit;
```

https://stackoverflow.com/questions/17633422/psql-fatal-database-user-does-not-exist

``` console
% createdb chunywan
```

``` console
% psql
```

``` console
% psql
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;
postgres=# grant all privileges on database mydb to myuser;
postgres=# exit;
```

https://www.postgresqltutorial.com/postgresql-create-table/

``` console
% psql -h localhost -U myuser -d mydb
%
```
