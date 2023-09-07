from api.test import SeleniumTestCase

"""
Tu run the tests, execute:
    python manage.py test
To run the tests in the browser, execute:
    python manage.py test --browser
To resume the execution from the fourth step for example, execute:
   python manage.py test --browser --from 2
To create development database from the fourth step for example, execute:
   python manage.py test --restore 4
To run the test as a tutorial, execute:
   python manage.py test --tutorial
"""

class TesteIntegracao(SeleniumTestCase):

    def test(self):
        self.create_superuser('admin', '123')

        if self.step():
            self.login('admin', '123')
            self.logout()

