#from playwright.sync_api import Page, expect
from camoufox.sync_api import Camoufox
from bot_functions import FetchResponses

number = "0886890402"  # phone number here, only vietnamese
# PROXY = "localhost:3128"  # squid proxy

if __name__ == '__main__':
    for i in range(1):
        bot = FetchResponses(number)
        results = []  # Store results

        methods = [
            bot.viettel,
            bot.tv360,
            bot.fpt,
            bot.fptplay,
            bot.fptshop,
            bot.tgdd,
            bot.viettelpost,
            bot.shopee,
            bot.vnpt,
            bot.sctv,
            bot.galaxyplay,
            bot.danet,
            bot.cliptv,
            bot.vieon,
            bot.pharmacity,
            bot.hasaki,
            bot.vtcpay,
            bot.vnggames,
            bot.dienmayxanh,
            bot.quangtrimang,
            bot.phongvu,
            bot.chotot,
            bot.tiki,
            
            bot.close  # must have :3
        ]

        for method in methods:
            try:
                print(f"Executing {method.__name__}.")
                result = method()
                results.append(result)
                print(f"{method.__name__} completed w/ result: {result}")
            except Exception as e:
                print(f"Error in {method.__name__}: {e}")
                results.append("error")  # Append "error"
            finally:
                print(f"{method.__name__} cleanup complete")
                print("------------------------------")

        print(f"Submission {i + 1} results: {results}")