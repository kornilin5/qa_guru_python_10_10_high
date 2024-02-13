from selene import browser, be, have
from qa_guru_python_10.data.users import Users
from qa_guru_python_10.utils import resources_path



class RegistrationPage:

    def open(self):
        browser.open("/")

    def registration_form_page(self, user: Users):

        browser.element('#firstName').should(be.visible).type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[for^=gender-radio]').element_by(
            have.exact_text(user.gender)).click()

        browser.element("#userNumber").type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(user.moth)
        browser.element('.react-datepicker__year-select').send_keys(user.year)
        browser.element(
            f'.react-datepicker__day.react-datepicker__day--0{user.day}'
        ).click()

        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.all('[for^=hobbies-checkbox]').element_by(
            have.exact_text(user.hobbies)).click()

        browser.element("#uploadPicture").send_keys(
            resources_path.path_photo(user.photo))

        browser.element("#currentAddress").type(user.current_address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)).click()

        browser.element('#submit').should(be.clickable).press_enter()

    def should_registration_form(self, user: Users):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(f'{user.first_name} {user.last_name}', {user.email},
                       {user.gender}, {user.phone}, {user.date_of_birth},
                       {user.subjects}, {user.hobbies}, {user.photo},
                       {user.current_address}, f'{user.state} {user.city}'))
