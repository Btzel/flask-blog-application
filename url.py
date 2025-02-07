from flask import url_for


def get_url_dict():
    assets_url = url_for('static', filename='assets')
    img_url = url_for('static', filename='assets/img')
    js_url = url_for('static', filename='js/scripts.js')
    css_url = url_for('static', filename='css/styles.css')
    favicon_url = url_for('static',filename='assets/favicon.ico')

    url_dict = {
        'assets':assets_url,
        'img':img_url,
        'js':js_url,
        'css':css_url,
        'favicon':favicon_url,
    }

    return url_dict