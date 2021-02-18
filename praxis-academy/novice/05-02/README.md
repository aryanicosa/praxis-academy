<h1>Installing and basic use of Postgresql </h1>

1. Installation
    
    $ sudo apt update
    $ sudo apt install postgresql postgresql-contrib

2. enter postgresql
    
    (choose an account, here is using postgres)
    $ sudo -i -u postgres
    
    (acces postgres)
    $ psql
    
    (exit)
    postgres=# \q

3. Creating new role
    
    (creating new role as superuser)
    $ sudo -u postgres createuser --interactive
    
    enter name : 
    enter password :
    (the rest are optional)
    
    check more control using
    $ man createuser

4. Create new database

    it's may create from your account or using root, i preferely using root
    
    $ sudo -u postgres createdb <name>

5. opening database with new role

    $ sudo adduser <your role name>
    
    (log into database)
    $ sudo -u <your role name> psql

6. check current connection information

    <your role name>=# \conninfo

 the rest is yours.....

to open more information, you maight check : 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

