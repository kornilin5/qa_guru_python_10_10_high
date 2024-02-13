from qa_guru_python_10.model.pages.registration_pages import RegistrationPage
from qa_guru_python_10.data import users

#tests
def test_user_registration_form():
    client = users.user
    registration_pages = RegistrationPage()
    registration_pages.open()
    registration_pages.registration_form_page(client)
    registration_pages.should_registration_form(client)
