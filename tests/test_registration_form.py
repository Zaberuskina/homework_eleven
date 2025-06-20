import allure
from data.student_data import Student
from pages.registration_page import RegistrationPage

@allure.title("Успешная регистрация пользователя через UI")
def test_submit_registration_form(setup_browser):
    student = Student()
    registration_page = RegistrationPage(setup_browser)

    with allure.step("Открыть страницу регистрации"):
        registration_page.open()

    with allure.step("Заполнить форму студента"):
        registration_page.register(student)

    with allure.step("Проверить успешную регистрацию"):
        registration_page.should_have_registered(student)

