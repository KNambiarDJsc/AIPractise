import os
import agentql
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

AGENTQL_API_KEY="7O-WMHybDtmOblVCFpA4btm18uk5EeOHNfOgBc0PZaEDHm4_4JaMlA"

EMAIL = os.getenv('EMAIL')

PASSWORD = os.getenv('PASSWORD')

os.environ["AGENTQL_API_KEY"] = os.getenv('AGENTQL_API_KEY')

INITIAL_URL = "https://www.idealist.org/en"

BASE_URL = "https://www.idealist.org/en"

EMAIL_INPUT_QUERY = """
{

        login_form{
            email_input
            continue_btn
        }

}
"""

VERIFY_QUERRY = """
{

        login_form{
            
            verify_not_robot_checkbox
    
        }

}
"""


PASSWORD_QUERY = """
{

        login_form{
            
            password_input
            continue_btn
    
        }

}
"""

with sync_playwright() as playwright, playwright.chromium.launch (headless=False) as browser:

    page = agentql.wrap(browser.new_page())

    page.goto(INITIAL_URL)

    #Use query Lements() method to locate "Log In" button on the page

    response = page.query_elements(EMAIL_INPUT_QUERY) 
    response.login_form.email_input.fill(EMAIL)

    page.wait_for_timeout(1000)


    #Verify human

    verify_response = page.query_elements()

    verify_response.login_form.verify_not_robot_checkbox.click()

    page.wait_for_timeout(1000)

    response.login_form.continue_btn.click()

    password_response = page.query_elements(PASSWORD_QUERY) 
    password_response.login_form.password_input.fill(PASSWORD)

    password_response.login_form.continue_btn.click()

    page.wait_for_page_ready_state()

    