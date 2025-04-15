#from playwright.sync_api import Page, expect
from camoufox.sync_api import Camoufox
import time

class FetchResponses:
    def __init__(self, number):
        self.number = number
        # browser options
        self.browser_options = {
            "headless": True,
            "humanize": False,
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

    def viettel(self):
        page = self.page
        url = 'https://viettel.vn/vx/'
        page.goto(url)
        
        try:
            page.get_by_role("button", name="Đăng nhập").click()
            page.get_by_placeholder('Nhập số điện thoại').fill(self.number)
            page.get_by_text('Lấy mã OTP').click()
            time.sleep(0.5)
            return "success"

        except Exception as e:
            print(e)
            return "error"
            
        finally:
            print("Done")

    def tv360(self):
        page = self.page
        url = 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Nhập số điện thoại/Tài khoản").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def fpt(self):
        page = self.page
        url = 'https://accounts.fpt.vn/'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Nhập số điện thoại").fill(self.number)
            page.get_by_role("link", name="Tiếp tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def fptplay(self):
        page = self.page
        url = 'https://fptplay.vn'
        page.goto(url)

        try:
            page.get_by_role("listitem").filter(has_text="Đăng nhập").nth(1).click()
            page.get_by_placeholder("Số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()

            try:
                OTP = page.get_by_role("button", name="Lấy mã OTP")
                OTP.wait_for(timeout=5000)
                OTP.click()
                print("OTP sent successfully")
                time.sleep(0.5)
                return "success"
            except:
                print("OTP failed")
                return "failed"
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def fptshop(self):
        page = self.page
        url = 'https://fptshop.com.vn/gio-hang' # gio-hang load faster, idk
        page.goto(url)

        try:
            page.get_by_role("button", name="Đăng ký / Đăng nhập").first.click()
            page.get_by_role("textbox", name="Nhập số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            page.get_by_role("checkbox", name="Tôi đồng ý với điều khoản dị").check()
            page.get_by_role("button", name="Tiếp tục").first.click()
            page.get_by_role("button", name="Nhận qua SMS").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def tgdd(self): # have captcha
        page = self.page
        url = 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Nhập số điện thoại mua hàng").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def viettelpost(self):
        page = self.page
        url = 'https://id.viettelpost.vn/Account/Register'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Nhập họ và tên").fill('Nguyen Thi Lmao')
            page.get_by_role("textbox", name="Nhập số điện thoại hoặc email").fill(self.number)
            page.locator("#password").fill('Lm@ao123123')
            page.locator("#password_confirm").fill('Lm@ao123123')
            page.get_by_role("button", name="Đăng ký ngay").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def shopee(self):
        page = self.page
        url = 'https://shopee.vn/buyer/signup'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp theo").click()
            page.get_by_role("button", name="Các phương pháp khác").click()
            page.get_by_role("button", name="Tin nhắn SMS").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def vnpt(self):
        page = self.page
        url = 'https://my.vnpt.com.vn/vinaphone-plus/'
        page.goto(url)

        try:
            page.get_by_role("paragraph").filter(has_text="Đăng nhập").click()
            page.get_by_role("textbox", name="Mời nhập số điện thoại").fill(self.number)
            page.get_by_role("button", name="Gửi mã OTP").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

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

    def galaxyplay(self):
        page = self.page
        url = 'https://galaxyplay.vn/auth'
        page.goto(url)

        try:
            page.get_by_role("button", name="Dùng số điện thoại của bạn").click()
            page.get_by_role("textbox", name="Nhập số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def danet(self):
        page = self.page
        url = 'https://danet.vn/'
        page.goto(url)

        try:
            page.get_by_role("button", name="đăng nhập").click()
            page.get_by_role("button", name="ĐĂNG KÝ NGAY").click()
            page.get_by_role("textbox", name="Tài khoản").fill(self.number)
            page.get_by_role("textbox", name="Mật khẩu", exact=True).fill('Lm@ao123123')
            page.get_by_role("textbox", name="Xác nhận mật khẩu").fill('Lm@ao123123')
            page.get_by_role("button", name="Đăng ký").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def cliptv(self):
        page = self.page
        url = 'https://cliptv.vn/'
        page.goto(url, timeout=20000)

        try:
            page.get_by_role("link", name="Đăng nhập").click()
            page.get_by_role("textbox", name="Nhập số điện thoại").press_sequentially(self.number)
            page.locator("#loginByPhoneModal label").check()
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(0.5)

            check = page.get_by_text("Đăng ký tài khoản", exact=True)
            if check.is_visible():
                print("create acc")
                page.locator("input[name=\"password-create\"]").press_sequentially('Lm@ao123123')
                page.locator("input[name=\"password-create-confirm\"]").press_sequentially('Lm@ao123123')
                page.get_by_role("button", name="Đăng nhập").click(force=True)
                return "success"

            elif page.locator("#modalLoginByPhonePassword").get_by_text("Đăng nhập").is_visible():
                print("acc exist")
                page.get_by_role("link", name="Quên mật khẩu?").click()
                page.locator("input[name=\"password-create\"]").press_sequentially('Lm@ao123123')
                page.locator("input[name=\"password-create-confirm\"]").press_sequentially('Lm@ao123123')
                page.get_by_role("button", name="Đăng nhập").click(force=True)
                return "success"

            else:
                print("error")
                return "failed"

            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def vieon(self):
        page = self.page
        url = 'https://vieon.vn/auth/'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Số điện thoại").fill(self.number)
            page.get_by_role("button", name="Bắt đầu").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def pharmacity(self):
        page = self.page
        url = 'https://www.pharmacity.vn/tu-van-thuoc?utm_source=web&utm_medium=header&utm_campaign=tuvanthuoc'
        page.goto(url)

        try:
            page.get_by_role("button", name="Đăng nhập/ Đăng ký").click()
            page.get_by_role("textbox", name="Nhập số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp tục", exact=True).click()
            page.get_by_label("Thỏa thuận người dùng").locator("label span").nth(1).check()
            page.get_by_role("button", name="Tôi đồng ý").click()
            page.get_by_role("button", name="Gửi mã xác thực qua SMS").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def hasaki(self):
        page = self.page
        url = 'https://hasaki.vn/'
        page.goto(url, timeout=20000)

        try:
            time.sleep(0.5)
            check = page.get_by_role("button", name="Không đồng ý")
            if check.is_visible(timeout=8000): check.click()
            page.locator("#btn-login").click()
            page.get_by_role("link", name="Đăng ký ngay").click()
            page.get_by_role("textbox", name="Nhập email hoặc số điện thoại").press_sequentially(self.number, delay=80)
            page.get_by_role("button", name="lấy mã").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")
    
    def vtcpay(self):
        page = self.page
        url = 'https://vtcpay.vn/'
        page.goto(url)

        try:
            page.get_by_role("link", name="Đăng ký").click()
            page.get_by_role("textbox", name="Nhập số điện thoại/tên tài").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(1)
            check = page.locator("#error_notify")#.filter(has_text="Tài khoản chưa tồn tại")
            if check.is_visible(timeout=8000):
                print("create acc")
                page.get_by_role("button", name="Tiếp tục").click(force=True)
                time.sleep(0.5)
                return "success"
            else: 
                print("acc exist") 
                return "failed"
            
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def vnggames(self):
        page = self.page
        url = 'https://id.vnggames.app/login'
        page.goto(url)

        try:
            language = page.locator("[id=\"popover-trigger-\\:r3\\:\"]").get_by_text("Tiếng Việt")
            if language.is_visible(timeout=1000):
                print("vietnamese")
                page.locator("[id=\"popover-trigger-\\:r3\\:\"]").get_by_role("button").click()
                page.get_by_text("English").click()
                print("changed to english")
            if language.is_visible(timeout=1000) == False:
                print("english")
                page.get_by_role("textbox", name="Enter email or phone number").fill(self.number)
                page.get_by_role("button", name="Continue").click()
                time.sleep(0.6)
                check = page.get_by_text("Phone number is not registered")
                if check.is_visible(timeout=8000):
                    print("create acc")
                    page.get_by_role("button", name="Register").click()
                    page.get_by_role("button", name="Continue").click()
                    page.get_by_role("textbox", name="Password").fill("Lm@ao123123")
                    page.locator(".ecn-css-cache-p86b9p").check()
                    page.get_by_role("button", name="Continue").click()
                    time.sleep(0.5)
                    return "success"
                else:
                    print("acc exist")
                    return "failed"
                

            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def dienmayxanh(self):
        page = self.page
        url = 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap'
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Nhập số điện thoại mua hàng").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def quangtrimang(self):
        page = self.page
        url = 'https://account.meta.com.vn/signup' # idk, meta?
        page.goto(url)

        try:
            page.get_by_role("textbox", name="Nhập chính xác số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def phongvu(self):
        page = self.page
        url = 'https://phongvu.vn/login?challenge=fb91d4aace32404ca76679ba4391703f'
        page.goto(url, timeout=20000)

        try:
            page.get_by_label("", exact=True).check()
            page.get_by_role("button", name="Tiếp tục với số điện thoại").click()
            page.get_by_role("textbox", name="Nhập số điện thoại").fill(self.number)
            page.get_by_role("button", name="Gửi").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def chotot(self):
        page = self.page
        url = 'https://id.chotot.com/register'
        page.goto(url)

        try:
            page.locator("input[name=\"name\"]").fill("Nguyen Thi Lmao")
            page.locator("input[name=\"phone\"]").fill(self.number)
            page.locator("input[name=\"password\"]").fill("Lm@ao123123")
            page.get_by_role("button", name="ĐĂNG KÝ").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")

    def tiki(self):
        page = self.page
        url = 'https://tiki.vn/thong-tin/tiki-doi-tra-de-dang-an-tam-mua-sam'
        page.goto(url, timeout=20000)

        try:
            check = page.get_by_role("img", name="close-icon")
            if check.is_visible(timeout=5000):
                print("closed ads")
                check.click()
            page.get_by_text("Tài khoản").click()
            page.get_by_role("textbox", name="Số điện thoại").fill(self.number)
            page.get_by_role("button", name="Tiếp Tục").click()
            time.sleep(0.5)
            return "success" 
            
        except Exception as e:
            print(e)
            return "error"

        finally:
            print("Done")