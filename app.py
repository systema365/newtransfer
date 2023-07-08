from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import uuid
#define db
db = SQLAlchemy()

app = Flask(__name__)

# Define the database connection parameters - uses a postgresql database found in the same dockercompose file
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/uploadz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Create the tables if they don't exist
db.init_app(app)
with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Database tables created successfully!")  

# The database is called 'uploadz' and the tables are called 'upload_user' and 'filepointer'
# upload_user contains the user information using the email address as the primary key, the source ip address, country the upload was made from and the date and time of the last upload
# filepointer contains the file name, email address, file pointer(guid), and timestamp of when it was uploaded - the file pointer is used to find the file in the uploads directory
# Define the upload_user table using sqlalchemy
class upload_user(db.Model):
    __tablename__ = 'upload_user'
    email = db.Column(db.String(120), primary_key=True)
    ip_address = db.Column(db.String(120))
    country = db.Column(db.String(120))
    last_upload = db.Column(db.String(120))

    def __init__(self, email, ip_address, country, last_upload):
        self.email = email
        self.ip_address = ip_address
        self.country = country
        self.last_upload = last_upload

    def __repr__(self):
        return '<User %r>' % self.email
# Define the filepointer table using sqlalchemy
class filepointer(db.Model):
    __tablename__ = 'filepointer'
    file_name = db.Column(db.String(120), primary_key=True)
    email = db.Column(db.String(120))
    file_pointer = db.Column(db.String(2000))
    timestamp = db.Column(db.String(120))

    def __init__(self, file_name, email, description, timestamp):
        self.file_name = file_name
        self.email = email
        self.description = description
        self.timestamp = timestamp

    def __repr__(self):
        return '<User %r>' % self.file_name

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        description = request.form['description']
        email = request.form['email']
        # Name the file with guid to be referenced in a postresql database
        file.filename = str(uuid.uuid4())
        # Create the directory if it doesn't exists
        # Process the uploaded file as desired
        file.save('/uploads' + file.filename)
        # Continue with your logic
    db.create_all()
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
