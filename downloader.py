from image_handler import image_handler_func
import uuid, pathlib, os
from flask import (
    flash,
    redirect,
    url_for
)
import urllib.request


def downloader_func():
    try:
        global requested_url, specific_element, tag
        for img in image_handler_func(tag, specific_element, requested_url):
            image_url = img

            filename = str(uuid.uuid4())
            file_ext = pathlib.Path(image_url).suffix

            picture_filename = filename + file_ext

            downloads_path = str(pathlib.Path.home() / "Downloads")

            picture_path = os.path.join(downloads_path, picture_filename)

            urllib.request.urlretrieve(image_url, picture_path)

        flash("Images sucessfully downloaded", "success")

    except Exception as e:
        flash(e, "danger")

    return redirect(url_for('index'))
