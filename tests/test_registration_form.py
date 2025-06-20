import allure
from pages.registration_page import RegistrationPage
from data.student_data import Student


@allure.title("Успешная регистрация пользователя через UI")
def test_submit_registration_form():
    registration_page = RegistrationPage()
    student = Student()

    with allure.step("Открыть страницу регистрации"):
        registration_page.open()

    with allure.step("Заполнить форму"):
        registration_page.register(student)

    with allure.step("Проверить успешную регистрацию"):
        registration_page.should_have_registered(student)
