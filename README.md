# learn_python_django_rest_api
Learning to build rest api in django rest framework.


# running single test file
example: running test from core/tests/test_admin.py file
docker-compose exec web python manage.py test core.tests.test_admin

# running all test
docker-compose exec web /bin/sh test.sh

# creating new superuser
docker-compose exec web python manage.py createsuperuser