from selene import have, command
from selene.support.shared import browser
from pathlib import Path
from locators.registration_locators import RegistrationPageLocators as Locators
from data.student_data import Student

DATA_DIR = Path(__file__).parent.parent / 'data'

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, student: Student):
        browser.element(Locators.FIRST_NAME_INPUT).type(student.first_name)
        browser.element(Locators.LAST_NAME_INPUT).type(student.last_name)
        browser.element(Locators.EMAIL_INPUT).type(student.email)
        browser.element(Locators.GENDER_MALE_RADIO).click()
        browser.element(Locators.PHONE_INPUT).type(student.phone)

        browser.element(Locators.DATE_INPUT).click()
        browser.element(Locators.MONTH_SELECT).type(student.birth_month)
        browser.element(Locators.YEAR_SELECT).type(student.birth_year)
        browser.element(f'.react-datepicker__day--0{student.birth_day:0>2}').click()

        browser.element(Locators.SUBJECTS_INPUT).type(student.subject).press_enter()
        browser.element(Locators.HOBBIES_SPORTS).perform(command.js.click)
        browser.element(Locators.HOBBIES_MUSIC).perform(command.js.click)

        file_path = DATA_DIR / student.picture
        if file_path.exists():
            browser.element(Locators.UPLOAD_PICTURE).set_value(str(file_path))

        browser.element(Locators.ADDRESS_INPUT).type(student.address)

        browser.element(Locators.STATE_SELECT).perform(command.js.click)
        browser.all(Locators.STATE_OPTIONS).element_by(have.text(student.state)).click()
        browser.element(Locators.CITY_SELECT).perform(command.js.click)
        browser.all(Locators.CITY_OPTIONS).element_by(have.text(student.city)).click()

        browser.element(Locators.SUBMIT_BUTTON).perform(command.js.click)
        return self

    def should_have_registered(self, student: Student):
        browser.element(Locators.MODAL_TITLE).should(have.text('Thanks for submitting the form'))
        browser.all(Locators.TABLE_ROWS).should(have.exact_texts(
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
