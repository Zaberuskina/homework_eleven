class RegistrationPageLocators:
    FIRST_NAME_INPUT = '#firstName'
    LAST_NAME_INPUT = '#lastName'
    EMAIL_INPUT = '#userEmail'
    GENDER_MALE_RADIO = '[for="gender-radio-1"]'
    PHONE_INPUT = '#userNumber'

    DATE_INPUT = '#dateOfBirthInput'
    MONTH_SELECT = '.react-datepicker__month-select'
    YEAR_SELECT = '.react-datepicker__year-select'

    SUBJECTS_INPUT = '#subjectsInput'
    HOBBIES_SPORTS = '[for="hobbies-checkbox-1"]'
    HOBBIES_MUSIC = '[for="hobbies-checkbox-3"]'

    UPLOAD_PICTURE = '#uploadPicture'
    ADDRESS_INPUT = '#currentAddress'

    STATE_SELECT = '#state'
    STATE_OPTIONS = '#stateCity-wrapper div[id^="react-select"][id*="-option"]'
    CITY_SELECT = '#city'
    CITY_OPTIONS = '#stateCity-wrapper div[id^="react-select"][id*="-option"]'

    SUBMIT_BUTTON = '#submit'

    MODAL_TITLE = '#example-modal-sizes-title-lg'
    TABLE_ROWS = 'tbody tr'
