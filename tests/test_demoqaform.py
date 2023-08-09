import allure
from selene import have
from pages.registration_page import RegistrationPage


@allure.title("Successful fill form")
def test_student_registration_form():
    registration_page = RegistrationPage()
    with allure.step("Open practice form page"):
        registration_page.open_practice_form_page()

    with allure.step("Fill form"):
        registration_page.fill_first_name('Ivan')
        registration_page.fill_last_name('Ivanov')
        registration_page.fill_email('Ivan@example.com')
        registration_page.fill_gender()
        registration_page.fill_phone_number('9881234567')
        registration_page.fill_date_of_birth('2', 'October', '2000')
        registration_page.fill_subjects('Chemistry')
        registration_page.fill_hobbies()
        registration_page.upload_image('Ivan.jpg')
        registration_page.fill_current_address('Mira str., 5')
        registration_page.fill_state('NCR')
        registration_page.fill_city('Delhi')
        registration_page.submit()

    with allure.step("Check form results"):
        registration_page.should_registered_user_with.should(
            have.exact_texts(
                'Ivan Ivanov',
                'Ivan@example.com',
                'Male',
                '9881234567',
                '02 October,2000',
                'Chemistry',
                'Sports, Reading, Music',
                'Ivan.jpg',
                'Mira str., 5',
                'NCR Delhi'
            )
        )
