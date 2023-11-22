page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
inputs = {
    'employee_name': '//label[text()="Employee Name"]/following::input[1]',
    'employee_id': '//label[text()="Employee Id"]/following::input[1]',
    'supervisor_name': '//label[text()="Supervisor Name"]/following::input[1]'
}
buttons = {
    'reset': '//button[text()=" Reset "]',
    'search': '//button[text()=" Search "]',
    'add': '//button[text()=" Add "]',
    'removal_confirmation': '//button[text()=" Yes, Delete "]',
    'removal_cancellation': '//button[text()=" No, Cancel "]'
}
icons = {
    'edit': '//i[@class="oxd-icon bi-pencil-fill"]',
    'delete': '//i[@class="oxd-icon bi-trash"]'
}
dropdowns = {}
