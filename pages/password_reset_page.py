page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode'
inputs = {
    'username': '//input[@name="username"]'
}
buttons = {
    'cancel': '//button[text()=" Cancel "]',
    'reset_password': '//button[text()=" Reset Password "]'
}
error_messages = {
    'missing_username': '//span[text()="Required"]'
}
