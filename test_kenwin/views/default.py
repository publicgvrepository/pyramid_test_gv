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
    # next_url = request.route_url('view_page', pagename='FrontPage')
    # return HTTPFound(location=next_url)
    user = request.user
    if user is None or user.role not in ('admin'):
        raise HTTPForbidden
    return {'one': "dos", 'project': 'GV RULES'}


# @view_config(route_name='view_page', renderer='../templates/view.jinja2')
# def view_page(request):
#     pagename = request.matchdict['pagename']
#     page = request.dbsession.query(models.Page).filter_by(name=pagename).first()
#     if page is None:
#         raise HTTPNotFound('No such page')

#     def add_link(match):
#         word = match.group(1)
#         exists = request.dbsession.query(models.Page).filter_by(name=word).all()
#         if exists:
#             view_url = request.route_url('view_page', pagename=word)
#             return '<a href="%s">%s</a>' % (view_url, escape(word))
#         else:
#             add_url = request.route_url('add_page', pagename=word)
#             return '<a href="%s">%s</a>' % (add_url, escape(word))

#     content = publish_parts(page.data, writer_name='html')['html_body']
#     content = wikiwords.sub(add_link, content)
#     edit_url = request.route_url('edit_page', pagename=page.name)
#     return dict(page=page, content=content, edit_url=edit_url)




# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(models.MyModel)
#         one = query.filter(models.MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'test_kenwin'}


# db_err_msg = """\
# Pyramid is having a problem using your SQL database.  The problem
# might be caused by one of the following things:

# 1.  You may need to initialize your database tables with `alembic`.
#     Check your README.txt for descriptions and try to run it.

# 2.  Your database server may not be running.  Check that the
#     database server referred to by the "sqlalchemy.url" setting in
#     your "development.ini" file is running.

# After you fix the problem, please restart the Pyramid application to
# try it again.
# """
