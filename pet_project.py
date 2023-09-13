"""Проект по созданию парсера сайтов, в данном проекте будет реалезован парсинг
магазинов по продаже комплектующих для ПК. Данный парсер станет частью будущего
проекта по автомотическому подбору комплектующих исходя из цены и задач."""


import requests
import json


def get_data_DNS():

    cookies = {
        'cartUserCookieIdent_v3': '29eb80611295b177ab7db9c4d2acf5e7569311e6f17fb866348d5419d1a28574a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%222cf60e9f-1d18-3488-b6f4-2a86a3ce755c%22%3B%7D',
        'phonesIdent': '10bf1f8edb9a7daae5a75c2a0890b9c09d42cbbd0a92426570e6da8c62c8ba96a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%225c9623ad-a93f-40e6-b1c2-db4968d8532d%22%3B%7D',
        '_gcl_au': '1.1.1328264274.1688494503',
        '_ym_uid': '1688494503862198504',
        '_ym_d': '1688494503',
        'tmr_lvid': '3b8964a3b5d2c7a77d8d9c2452c20d93',
        'tmr_lvidTS': '1688494503461',
        'rrpvid': '65878629493937',
        'rcuid': '64aad914ec6cdba6f20a611f',
        'current_path': 'b08c9f032f09666a0ede0230afb69710f19a783d5dece723c75a44d390027a98a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A145%3A%22%7B%22city%22%3A%22fef6c676-86cd-11e5-a236-00155d03361b%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0430%5Cu043b%5Cu0438%5Cu043d%5Cu0438%5Cu043d%5Cu0433%5Cu0440%5Cu0430%5Cu0434%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
        'cookieImagesUploadId': '5670e220aba25e32827708949494a30ee8cb6bf3daa1868774f89ee17864bb10a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%226244447a-fda3-436b-ad0e-e188908e39fe%22%3B%7D',
        '_ga_ND7GY87YET': 'GS1.1.1689315099.1.0.1689315099.60.0.0',
        'qrator_ssid': '1694588226.629.2wAMEsr5Pr7MycNj-h42mr7fg0glh3jsrj6g777oesclpt6ha',
        '_gid': 'GA1.2.853264839.1694588229',
        'lang': 'ru',
        'city_path': 'kaliningrad',
        '_ab_1_': '333',
        'PHPSESSID': '9cce0ec02db56b430e6a144cd5d82996',
        '_csrf': 'a4e06ba5f38a83d3cfd4ac2b54d42453131915a145a2841f65dc6403898a177ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%227Z56Pgiy_ouE38Eyg--STmLUxpxmPi1Q%22%3B%7D',
        '_ym_visorc': 'b',
        '_ym_isad': '2',
        'qrator_jsid': '1694588225.160.VQ9fVQeoPgb2L1gL-j84vkvmtpa5q0bl422tsinlnbrom899u',
        '_ab_': '%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_test%22%7D',
        'tmr_detect': '0%7C1694589273628',
        'rr-testCookie': 'testvalue',
        '_gat': '1',
        '_gat_%5Bobject%20Object%5D': '1',
        '_gat_UA-8349380-2': '1',
        '_ga': 'GA1.1.1308029515.1688494502',
        '_ga_FLS4JETDHW': 'GS1.1.1694588229.5.1.1694589611.58.0.0',
        '_ga_YT23VHSRDB': 'GS1.2.1694588229.1.1.1694589613.60.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'cartUserCookieIdent_v3=29eb80611295b177ab7db9c4d2acf5e7569311e6f17fb866348d5419d1a28574a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%222cf60e9f-1d18-3488-b6f4-2a86a3ce755c%22%3B%7D; phonesIdent=10bf1f8edb9a7daae5a75c2a0890b9c09d42cbbd0a92426570e6da8c62c8ba96a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%225c9623ad-a93f-40e6-b1c2-db4968d8532d%22%3B%7D; _gcl_au=1.1.1328264274.1688494503; _ym_uid=1688494503862198504; _ym_d=1688494503; tmr_lvid=3b8964a3b5d2c7a77d8d9c2452c20d93; tmr_lvidTS=1688494503461; rrpvid=65878629493937; rcuid=64aad914ec6cdba6f20a611f; current_path=b08c9f032f09666a0ede0230afb69710f19a783d5dece723c75a44d390027a98a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A145%3A%22%7B%22city%22%3A%22fef6c676-86cd-11e5-a236-00155d03361b%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0430%5Cu043b%5Cu0438%5Cu043d%5Cu0438%5Cu043d%5Cu0433%5Cu0440%5Cu0430%5Cu0434%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; cookieImagesUploadId=5670e220aba25e32827708949494a30ee8cb6bf3daa1868774f89ee17864bb10a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%226244447a-fda3-436b-ad0e-e188908e39fe%22%3B%7D; _ga_ND7GY87YET=GS1.1.1689315099.1.0.1689315099.60.0.0; qrator_ssid=1694588226.629.2wAMEsr5Pr7MycNj-h42mr7fg0glh3jsrj6g777oesclpt6ha; _gid=GA1.2.853264839.1694588229; lang=ru; city_path=kaliningrad; _ab_1_=333; PHPSESSID=9cce0ec02db56b430e6a144cd5d82996; _csrf=a4e06ba5f38a83d3cfd4ac2b54d42453131915a145a2841f65dc6403898a177ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%227Z56Pgiy_ouE38Eyg--STmLUxpxmPi1Q%22%3B%7D; _ym_visorc=b; _ym_isad=2; qrator_jsid=1694588225.160.VQ9fVQeoPgb2L1gL-j84vkvmtpa5q0bl422tsinlnbrom899u; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_test%22%7D; tmr_detect=0%7C1694589273628; rr-testCookie=testvalue; _gat=1; _gat_%5Bobject%20Object%5D=1; _gat_UA-8349380-2=1; _ga=GA1.1.1308029515.1688494502; _ga_FLS4JETDHW=GS1.1.1694588229.5.1.1694589611.58.0.0; _ga_YT23VHSRDB=GS1.2.1694588229.1.1.1694589613.60.0.0',
        'Origin': 'https://www.dns-shop.ru',
        'Referer': 'https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/no-referrer',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2564 Yowser/2.5 Safari/537.36',
        'X-CSRF-Token': 'WZ3FRrlU4N2EZrTw-o2p1OlT_saIWpZcittnSFgqcblux_Bw6TOJpNsJwbXJteytjn7Tldw32gnyqx8lCENA6A==',
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    data = 'data={"type":"product-buy","containers":[{"id":"as-HEVg5M","data":{"id":"4899465"}},{"id":"as-U5e2vK","data":{"id":"4874638"}},{"id":"as-SCZMeJ","data":{"id":"4801408"}},{"id":"as-A1pQAI","data":{"id":"5075451"}},{"id":"as-awlBP7","data":{"id":"5068607"}},{"id":"as-33PQgE","data":{"id":"5075460"}},{"id":"as-hXwmPj","data":{"id":"1363163"}},{"id":"as-DUPtVw","data":{"id":"5058289"}},{"id":"as-wcpNsD","data":{"id":"5061537"}},{"id":"as-DH0oPG","data":{"id":"1214055"}},{"id":"as-kWdk88","data":{"id":"5026149"}},{"id":"as-DJng79","data":{"id":"5058958"}},{"id":"as-I0dMub","data":{"id":"5054039"}},{"id":"as-Bxyleq","data":{"id":"5054463"}},{"id":"as-z4ZJDc","data":{"id":"5062894"}},{"id":"as-hqLAbY","data":{"id":"1645747"}},{"id":"as-eX-wm8","data":{"id":"5073722"}},{"id":"as-lJsnAy","data":{"id":"5026143"}}]}'

    response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', cookies=cookies, headers=headers,
                             data=data)
    return response

def main():
    response = get_data_DNS()

if __name__ == '__main__':
    main()
