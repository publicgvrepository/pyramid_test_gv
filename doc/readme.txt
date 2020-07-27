    Primero que nada me guie con estos dos enlaces:
        * https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/cookiecutters.html
        * https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/index.html
    El resto es deducción y googleo.

La descripción de lo realizado es mas o menos el siguiente:

Con ellos setié el proyecto para que trabaje con el template jinja2 (que lo conoczco de django y flask),
setié el ORM sqlAlchemy y modifiqué para que se conecte a la base postgresql test_kenwin en localhost.
    Para que el proyecto funcione con esto, en setup.py agregué los modulos db-psycopg2 y
alembic (para trabajar con migraciones iniciales)

En el medio modifiqué para que trabaje con postgresql y no con sqlite.

Del proyecto generado borre el modelo por defecto mymodels.py y cree el modelo User en /models/user.py para manejar
los usuarios que se iban a autenticar en el sistema.

Por si se elegía la opción de migrar datos iniciales en vez de  importar la DB administrada, se modificó
el script /scripts/initialize_db para agruegar el usuario gv como admin (password: gvadmin)

Para la Authentication, en setup.py indico que trabajaré con el módulo bcrypt (password hashing).
Agregue en routes.py las siguientes rutas válidas del proyecto:
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
que se correponderan a las vistas en view/auth.py.

Agregue un home que solo sea accesible si se está logueado en view/defatul.py
@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    user = request.user
    if user is None or user.role not in ('admin'):
        raise HTTPForbidden
    return {'button_text': 'Algo en JS'}

Agregue un pequeño static/theme-login.css
Agregue el cdn de bootstrap 4.5.0

Mientras me encontraba realizando el README.md me encontré con un problema al ejecutar python setup.py develop, pero
al ejecutarlo dos veces finaliza bien. Creo que es un bug:
*************************
        match: db 0.1.1
        Processing db-0.1.1.tar.gz
        Writing /tmp/easy_install-uvb8ciau/db-0.1.1/setup.cfg
        Running db-0.1.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-uvb8ciau/db-0.1.1/egg-dist-tmp-tw81hkjg
        File "build/bdist.linux-x86_64/egg/db/__init__.py", line 69
            print "var", var
                ^
        SyntaxError: Missing parentheses in call to 'print'. Did you mean print("var", var)?
**************************

Cabe aclarar que es lo mejor que pude hacer en dos días, es la primera vez que trabajo con Pyramid por lo
cual me costó un poco entender como funcionaba.