from pyramid.compat import escape
import re
# from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )

from pyramid.view import view_config
# from pyramid.response import Response

# from sqlalchemy.exc import DBAPIError

from .. import models


# regular expression used to find WikiWords
wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    user = request.user
    if user is None or user.role not in ('admin'):
        raise HTTPForbidden
    return {'button_text': 'Algo en JS'}
