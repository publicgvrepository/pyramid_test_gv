

Primero que nada me guie con estos dos enlaces

https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/cookiecutters.html

https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/index.html

con ellos setié el proyecto para que trabaje con el template jinja2 (que lo conoczco de django y flask)
setié el ORM sqlalquemy y modifiqué para que se conecte a la base postgresql test_kenwin en localhost
en setup.py agregué los modulos db-psycopg2 y alembic (para trabajar con migraciones iniciales)

en el medio modifiqué para que trabaje con postgresql

borre el modelo por defecto mymodels.py
cree el modelo User en /models/user.py

modifiqué el script /scripts/initialize_db para agruegar el usuario gv como admin (password: gvadmin)


me salté lo de crear page
me salteo lo de crear algunas vistas

Authentication

en setup.py bcrypt (password hashing)

... agregue en routes.py
config.add_route('login', '/login')
config.add_route('logout', '/logout')

y el view/auth.py para manejar las vistas de logue


agregue un home que solo sea accesible si se está logueado en view/defatul.py
@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    # next_url = request.route_url('view_page', pagename='FrontPage')
    # return HTTPFound(location=next_url)
    user = request.user
    if user is None or user.role not in ('admin'):
        raise HTTPForbidden
    return {'one': "dos", 'project': 'GV RULES'}

agregue un pequeño static/theme-login.css


agregue el cdn de bootstrap 4.5.0