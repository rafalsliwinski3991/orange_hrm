page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
login_input = '//input[@name="username"]'
password_input = '//input[@name="password"]'
login_button = '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]'
error_message = {
    'invalid_credentials': '//div[@class="oxd-alert-content oxd-alert-content--error"]',
    'missing_username': '//label[text()="Username"]/following::span[1]',
    'missing_password': '//label[text()="Password"]/following::span[1]'
}
