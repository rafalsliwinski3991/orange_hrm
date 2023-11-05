page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
inputs = {
    'login': '//input[@name="username"]',
    'password': '//input[@name="password"]'
}
buttons = {
    'login': '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]'
}
error_messages = {
    'invalid_credentials': '//div[@class="oxd-alert-content oxd-alert-content--error"]',
    'missing_username': '//label[text()="Username"]/following::span[1]',
    'missing_password': '//label[text()="Password"]/following::span[1]'
}
links = {
    'forgot_your_password': '//p[text()="Forgot your password? "]'
}
