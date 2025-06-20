from selene import have, command
from pathlib import Path
from data.student_data import Student
from locators.registration_locators import RegistrationPageLocators as Locators
from pages.base_page import BasePage

DATA_DIR = Path(__file__).parent.parent / 'data'

class RegistrationPage(BasePage):

    def open(self):
        self.browser.open('/automation-practice-form')
        return self

    def register(self, student: Student):
        self.browser.element(Locators.FIRST_NAME_INPUT).type(student.first_name)
        self.browser.element(Locators.LAST_NAME_INPUT).type(student.last_name)
        self.browser.element(Locators.EMAIL_INPUT).type(student.email)
        self.browser.element(Locators.GENDER_MALE_RADIO).click()
        self.browser.element(Locators.PHONE_INPUT).type(student.phone)

        self.browser.element(Locators.DATE_INPUT).click()
        self.browser.element(Locators.MONTH_SELECT).type(student.birth_month)
        self.browser.element(Locators.YEAR_SELECT).type(student.birth_year)
        self.browser.element(f'.react-datepicker__day--0{student.birth_day:0>2}').click()

        self.browser.element(Locators.SUBJECTS_INPUT).type(student.subject).press_enter()
        self.browser.element(Locators.HOBBIES_SPORTS).perform(command.js.click)
        self.browser.element(Locators.HOBBIES_MUSIC).perform(command.js.click)

        file_path = DATA_DIR / student.picture
        if file_path.exists():
            self.browser.element(Locators.UPLOAD_PICTURE).set_value(str(file_path))

        self.browser.element(Locators.ADDRESS_INPUT).type(student.address)

        self.browser.element(Locators.STATE_SELECT).perform(command.js.click)
        self.browser.all(Locators.STATE_OPTIONS).element_by(have.text(student.state)).click()
        self.browser.element(Locators.CITY_SELECT).perform(command.js.click)
        self.browser.all(Locators.CITY_OPTIONS).element_by(have.text(student.city)).click()

        self.browser.element(Locators.SUBMIT_BUTTON).perform(command.js.click)
        return self

    def should_have_registered(self, student: Student):
        self.browser.element(Locators.MODAL_TITLE).should(have.text('Thanks for submitting the form'))
        self.browser.all(Locators.TABLE_ROWS).should(have.exact_texts(
            f'Student Name {student.first_name} {student.last_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.phone}',
            f'Date of Birth {student.birth_day} {student.birth_month},{student.birth_year}',
            f'Subjects {student.subject}',
            f'Hobbies {student.hobbies}',
            f'Picture {student.picture}',
            f'Address {student.address}',
            f'State and City {student.state} {student.city}'
        ))
        return self
