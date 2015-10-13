import os
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='home', renderer='json')
def system_status(request):
    return {'database': 'ok'}

@view_config(route_name='login', renderer='json')
def authenticate(request):
    return {'key':'abcde12345'}




@view_defaults(route_name='user')
class USERView(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', renderer='json')
    def get(self):
        return Response('get')

    @view_config(request_method='POST')
    def post(self):
        return Response('post')

    @view_config(request_method='PUT')
    def put(self):
        return Response('put')

    @view_config(request_method='DELETE')
    def delete(self):
        return Response('delete')

@view_config(route_name='list', renderer='json')
def listdir(request):
    dir_name = request.matchdict['dir_path']
    if os.path.isdir(dir_name):
        return os.listdir(dir_name)

# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     try:
#         one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(conn_err_msg, content_type='text/plain', status_int=500)
#     return {'one': one, 'project': 'technicolor_test'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_technicolor_test_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

