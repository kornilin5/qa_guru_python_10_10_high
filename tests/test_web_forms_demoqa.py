from qa_guru_python_10.model.pages.registration_pages import RegistrationPage


def test_user_registration_form():
    registration_pages = RegistrationPage()
    registration_pages.open()
    registration_pages.fill_first_name('ИМЯ')
    registration_pages.fill_last_name('ФАМИЛИЯ')
    registration_pages.fill_email('EMAIL@mail.ru')
    registration_pages.fill_gender('Male')
    registration_pages.fill_phone('2381491357')
    registration_pages.fill_date_of_birth("17", "March", "1999")
    registration_pages.fill_subjects('English')
    registration_pages.fill_hobbies('Reading')
    registration_pages.attach_photo('ZnugKfP5UJk.jpg')
    registration_pages.fill_current_address('ТУТ АДРЕСС')
    registration_pages.fill_state('Haryana')
    registration_pages.fill_city('Panipat')
    registration_pages.sumbit()
    registration_pages.should_registration_form(
        'ИМЯ',
        'ФАМИЛИЯ',
        'EMAIL@mail.ru',
        'Male',
        '2381491357',
        '17 March,1999',
        'English',
        'Reading',
        'ZnugKfP5UJk.jpg',
        'ТУТ АДРЕСС',
        'Haryana',
        'Panipat',
    )
