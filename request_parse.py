from bs4 import BeautifulSoup
import requests
from image_handler import image_handler_func
from flask import (
    render_template,
    flash
)


def request_parse_func(request):
    if request.method == "POST":

        try:
            global requested_url, specific_element, tag

            requested_url = request.form.get('urltext')
            tag = request.form.get('specificElement')

            source = requests.get(requested_url).text
            # parser library?
            soup = BeautifulSoup(source, "html.parser")

            specific_element = soup.find_all(tag)

            counter = len(specific_element)

            image_paths = image_handler_func(
                tag,
                specific_element,
                requested_url
            )

            return render_template("index.html",
                                   url=requested_url,
                                   counter=counter,
                                   image_paths=image_paths,
                                   results=specific_element
                                   )

        except Exception as e:
            flash(e, "danger")

    return render_template("index.html")