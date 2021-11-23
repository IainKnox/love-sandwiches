import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    get input sales figures from the user
    """
    while True:

        print('Please enter the sales figures from the last market')
        print('Figures should be six numbers, seperated by commas')
        print('Example 10,20,30,40,50,60\n')

        data_str = input('Enter your figures here: ')

        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print('Data is Valid!')
            break
    return sales_data

def validate_data(values):
    """
    inside the try, coverts all str values to integers
    raise valuerror is str cannot be converted to integer
    or if there arent exactly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(F"exactly 6 figures are required, you provided {len(values)}")
    except ValueError as e:
        print(F"invalid data: {e}, please try again\n")
        return False
    
    return True



data = get_sales_data()