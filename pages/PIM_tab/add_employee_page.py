page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'
inputs = {
    'first_name': '//input[@name="firstName"]',
    'middle_name': '//input[@name="middleName"]',
    'last_name': '//input[@name="lastName"]',
    'employee_id': '//label[text()="Employee Id"]/following::input[1]',
    'username': '//label[text()="Username"]/following::input[1]',
    'password': '//label[text()="Password"]/following::input[1]',
    'confirm_password': '//label[text()="Confirm Password"]/following::input[1]'
}
buttons = {
    'create_login_details': '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]',
    'save': '//button[text()=" Save "]',
    'cancel': '//button[text()=" Cancel "]'
}
error_messages = {
    'missing_first_name': '//input[@name="firstName"]/following::span[text()="Required"][1]',
    'missing_last_name': '//input[@name="lastName"]/following::span[text()="Required"][1]',
    'missing_username': '//label[text()="Username"]/following::input[1]/following::span[text()="Required"][1]',
    'missing_password': '//label[text()="Password"]/following::input[1]/following::span[text()="Required"][1]',
    'missing_password_confirmation':
        '//label[text()="Confirm Password"]/following::input[1]/following::span[text()="Required"][1]'
}
