from urllib.parse import urljoin
import validators


def image_handler_func(tag, specific_element, requested_url):
    image_paths = []

    if tag == 'img':
        images = [img['src'] for img in specific_element]
        for i in specific_element:
            image_path = i.attrs['src']
            valid_imgpath = validators.url(image_path)
            if valid_imgpath == True:
                full_path = image_path
            else:
                full_path = urljoin(requested_url, image_path)
                image_paths.append(full_path)

    return image_paths