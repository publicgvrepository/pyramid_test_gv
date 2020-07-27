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
 - clonar este repositorio en un directorio
 - cd pyramid_test_gv

 - crear *test_kenwin* database en postgresql como postgres

 - python setup.py develop **(dos veces si falla por bug)**

 - sigue **a** o **b**:
   - a (migra datos):
      - alembic -c development.ini upgrade head
      - alembic -c development.ini revision --autogenerate -m "use new model User"
      - initialize_test_kenwin_db development.ini

   - b (importa datos):
     - psql -U postgres -W test_kenwin < database/test_kenwin_gv.sql

- pserve development.ini

- abrir browser favorito en http://localhost:6543