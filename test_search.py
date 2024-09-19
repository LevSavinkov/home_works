from selene import browser, be, have


def search(search_string):
    return browser.element("[role='combobox']").should(be.blank).type(search_string).press_enter()


def test_success_search(open_browser, open_google):
    search_string = "Selene"
    search(search_string)
    browser.element("(//div[@id='rso']//h3)[1]").should(have.text(search_string))


def test_error_search(open_browser, open_google):
    search_string = "zxyqlvnwrp23847hfglxq"
    search(search_string)
    browser.element("//div[@class='card-section']/p[@role='heading']").should(
        have.text(f"Your search - {search_string} - did not match any documents."))
