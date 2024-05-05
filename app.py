import pymysql
import boto3
import json
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app = app 

# Retrieve database credentials from AWS Secrets Manager
def get_db_credentials():
    client = boto3.client('secretsmanager', region_name='eu-north-1')
    response = client.get_secret_value(SecretId='databasecredentials')
    secret_data = response['SecretString']
    return json.loads(secret_data)

# Define database connection function
def get_db_connection():
    credentials = get_db_credentials()
    return pymysql.connect(
        host=credentials['host'],
        user=credentials['username'],
        password=credentials['password'],
        database=credentials['dbInstanceIdentifier']
    )


@app.route('/')
def homepg():
        return render_template('index.html')

@app.route('/blog')
def blogpg():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT img_link, img_description, title, DATE_FORMAT(date, '%d/%m/%Y') AS date, content FROM blog")
            blog_data = cursor.fetchall()
    except pymysql.Error as e:
        # Handle database errors
        print(f"Error fetching blog data!: {e}")
        blog_data = []

    # finally:
    #     connection.close()

    return render_template('blog.html', blog=blog_data)

@app.route('/contact')
def contactpg():
        return render_template('contact.html')

@app.route('/gallery')
def gallerypg():
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT img_link, img_description FROM gallery")
            gallery_data = cursor.fetchall()
    except pymysql.Error as e:
        # Handle database errors
        print(f"Error fetching gallery data: {e}")
        gallery_data = []

    # finally:
    #     connection.close()

    return render_template('gallery.html', gallery=gallery_data)

@app.route('/login')
def loginpg():
        return render_template('login.html')

@app.route('/owner_login', methods=['POST'])
def owner_login():
    username = request.form['username']
    password = request.form['password']

    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    connection.close()

    if user:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('loginpg'))

@app.route('/success')
def success():
    return render_template('imginfo.html')


@app.route('/imginfo')
def imginfo():
        return render_template('imginfo.html')

@app.route('/add_image', methods=['POST'])
def add_image():
    img_link = request.form['img_link']
    img_description = request.form['img_description']
    
    # Insert image details into the database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO gallery (img_link, img_description) VALUES (%s, %s)", (img_link, img_description))
    connection.commit()
    connection.close()
    
    return redirect(url_for('gallerypg'))

@app.route('/add_blog', methods=['POST'])
def add_blog():
        img_link = request.form['img_link']
        img_description = request.form['img_description']
        title = request.form['title']
        date = request.form['date']
        content = request.form['content']
        
        # Insert blog details into the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO blog (img_link, img_description, title, date, content) VALUES (%s, %s, %s, %s, %s)", (img_link, img_description, title, date, content))
        connection.commit()
        connection.close()
        
        return redirect(url_for('blogpg'))


if __name__ == '__main__':
        app.run()
