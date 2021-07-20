class Proxy:
    home = 'https://seller.tiki.tw/'

    login_page_url = 'https://seller.tiki.tw/account/signin'

    account_input_css_selector = "input[placeholder='email']"

    password_input_css_selector = "input[placeholder='password']"

    login_button_xpath = "//div[contains(., 'login')][contains(@class, 'tiki-button')]"


    general_header = {  'authority':'seller.tiki.tw',
                        'scheme':'https',
                        'accept':'application/json, text/javascript, */*; q=0.01',
                        'accept-encoding':'gzip, deflate, br',
                        'accept-language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                        'dnt': ';',
                        'referer':'https://seller.tiki.tw/portal/product/new',
                        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}