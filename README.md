# Test Pyramid


Este es el desarrollo de un test técnico para Pyramid web Framework


## Test

Descripción: Levantar una aplicación utilizando el framework Pyramid, y poder autenticarse.
El escenario ideal implica levantar una aplicación web local en Pyramid con una base de datos: PostgreSQL subirla a un repositorio público de GitHub conteniendo simplemente dos URLs (el login y el home vacío) donde indique en el README como instalar su aplicación y lograr loguearse efectivamente con un usuario mostrando un Home con un template vacío (no es necesario que tenga diseño ni nada por el estilo).


## Entorno

**Sistema**: este sistema fue desarrollado en un entorno Ubuntu 20.04, con Postgres 12.3, y Python 3.8.2

**Herramientas y librerias**:
 - virtualenv
 - build-essentials, libsqlite3-dev
 - psycopg2 (pip)

## Instrucciones:

 - virtualenv -p python3 venv_test_kenwin
 - source venv_test_kenwin/bin/activate
 - git clone git@github.com:publicgvrepository/pyramid_test_gv.git
 - cd

- DB:
  - crear *test_kenwin* database on postgresql como postgres

  - a:
     - alembic -c development.ini upgrade head
     - alembic -c development.ini revision --autogenerate -m "use new model User"
     - initialize_test_kenwin_db development.ini

  - b:
     - psql -U postgres -W  test_kenwin < database/test_kenwin_gv.sql

- python setup.py develop

- pserve development.ini

- open your favourite browser on http://localhost:6543