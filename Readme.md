## How to install
1. Clone repository from github

    ```
    git clone https://github.com/toptal0212/careerxrosspoint.com
    ```

2. Install Packages for Python

    ```
    pip install -r requirements.txt
    ```

3. Install nodemodules for usage of tailwindcss

    ```
    npm install
    ```

4. Configure .env file and create database

    ```
    ON_SERVER=False

    MYSQL_DATABASE_NAME=careerxrosspoint_db
    MYSQL_DATABASE_USER=root
    MYSQL_DATABASE_PASSWORD=

    DEFAULT_FROM_EMAIL=
    EMAIL_HOST=
    EMAIL_PORT=587                  
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    EMAIL_USE_TLS=True 
    ```

5. Initialize Database

    ```
    python manage.py migrate
    ```

6. Run Tailwind dev server.

    ```
    npm run dev
    ```

7. Run Django

    ```
    python manage.py runserver
    ```
    