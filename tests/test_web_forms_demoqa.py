from qa_guru_python_10.model.pages.registations_pages import RegistrationPage
import time
def test_form():
    registations_pages = RegistrationPage()
    registations_pages.open()
    registations_pages.registration_form_page()
    time.sleep(5)
    registations_pages.should_registration_form()
