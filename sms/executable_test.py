#from playwright.sync_api import Page, expect
from camoufox.sync_api import Camoufox
import time

class FetchResponses:
    def __init__(self, number):
        self.number = number
        # browser options
        self.browser_options = {
            "headless": False,
            "humanize": True,
            "os": ["windows", "macos", "linux"],
            "block_webrtc": True, 
            #"exclude_addons": ["ublock-origin"],
            #"window": (1920, 1080),
        }

        self.humanize_options = {
        "maxTime": 1.0
        }
        
        self.camoufox = Camoufox(**self.browser_options)
        self.browser = self.camoufox.__enter__()
        self.page = self.browser.new_page()
        self.page.set_default_timeout(15000)
    
    def close(self):
        self.camoufox.__exit__(None, None, None)

    def sctv(self):
        page = self.page
        url = 'https://sctvonline.vn/vi/box/signup'
        page.goto(url)

        try:
            page.locator("input[name=\"firstname\"]").fill('Nguyen Thi Lmao')
            page.locator("input[name=\"phone\"]").fill(self.number)
            page.get_by_role("textbox").nth(2).fill('Lm@ao123123')
            page.get_by_role("textbox").nth(3).fill('Lm@ao123123')
            page.locator("label input[type='checkbox']").check()
            page.get_by_test_id("register-form-register-btn").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

# main
if __name__ == "__main__":
    number = "0886590433" # Test number
    bot = FetchResponses(number)

    bot.sctv()
"""
    bot.viettel(),
    bot.tv360(),
    bot.fpt(),
    bot.fptplay(),
    bot.fptshop(),
    bot.tgdd(),
    bot.viettelpost(),
    bot.shopee(),
    bot.vnpt(),
    bot.sctv(),
    bot.galaxyplay(),
    bot.danet(),
    bot.cliptv(),
    bot.vieon(),
    bot.pharmacity(),

    bot.close()
"""
# time.sleep(100)
