from flask import (
    Flask,
    request,
)
from downloader import downloader_func
from request_parse import request_parse_func

app = Flask(__name__)
app.secret_key = "secret-key"


@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return request_parse_func(request)


@app.route("/download", methods=("GET", "POST"), strict_slashes=False)
def downloader():
    downloader_func()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
