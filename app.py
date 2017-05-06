import os
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# var of the app path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    # target the images folder
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    # if the images folder doesn't exist, make it in the target folder
    if not os.path.isdir(target):
        os.mkdir(target)

    # look through the list of uploaded files, because we allowed multiple files
    for file in request.files.getlist("file"):
        print(file)
        # we get objects, so file.filename will return the filename
        filename = file.filename
        # we are adding the filename to the images folder
        destination = "".join([target, filename])
        print(destination)
        # save the file to the destination
        file.save(destination)

    return render_template("complete.html")


if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)