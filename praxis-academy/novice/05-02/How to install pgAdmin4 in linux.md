<h1>How to install pgAdmin in Linux Mint </h1>

1.Running the command, can be used to get full details about your Linux os

    $ cat /etc/os-release 

2. Update system

    $ sudo apt-get update

3. Install PostgreSQL (if you don't have it installed already)

    $ sudo apt-get install postgresql postgresql-contrib

    (optional)    
    Create the username and password for PostgreSQL database. 
    Type the following command in the terminal to add login credentials for the user, Postgres
    
    $ sudo -u postgres psql postgres
    # \password postgres

4. Install the required packages

    $ sudo apt-get install build-essential libssl-dev libffi-dev libgmp3-dev
    
    $ sudo apt-get install python3-virtualenv libpq-dev python3-dev

5. Create a virtual environment

    Run the following commands navigate to your home directory, create a new folder named pgAdmin4 and create the virtual environment.

    $ cd ~
    $ mkdir pgAdmin4
    $ cd pgAdmin4
    $ virtualenv venv

    activate virtual environtment
    
    $ source venv/bin/activate

6. Install pgAdmin

    (pip/pip3)
    
    $ pip install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.23/pip/pgadmin4-4.23-py3-none-any.whl
    (if this link didn't work, goest to https://ftp.postgresql.org/pub/pgadmin/pgadmin4/, navigate to the already version
    move to pip direktori, choose the link end with ...whl
    
7. Configure and Run
   
    create this,
    
    $ nano venv/lib/python3.8/site-packages/pgadmin4/config_local.py

    add this command to file
    
    import os
    DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
    LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
    SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
    SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
    STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
    SERVER_MODE = False 

    (save it)

8. Run test installation
    
    $ python venv/lib/python3.8/site-packages/pgadmin4/pgAdmin4.py


