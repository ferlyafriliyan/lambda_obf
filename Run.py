#! /usr/bin/env python3
import requests, re, json, os, time
from requests.exceptions import ChunkedEncodingError
from requests.exceptions import ConnectionError

while True:
    if os.path.exists('Data/Subscribe.json') == False:
        if os.path.exists('Data') == False:
            os.mkdir('Data')
        os.system('xdg-open https://www.youtube.com/c/RozhakID')
        with open('Data/Subscribe.json', 'w') as w:
            w.write(json.dumps({
                'Subscribe': True
            }))
        w.close();time.sleep(4.5);continue
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''\x1b[1;91m  ________        __          ___________     __                  
\x1b[1;91m /  _____/  _____/  |_        \__    ___/___ |  | __ ____   ____  
\x1b[1;91m/   \  ____/ __ \   __\  ______ |    | /  _ \|  |/ // __ \ /    \ 
\x1b[1;91m\    \_\  \  ___/|  |   /_____/ |    |(  <_> )    <\  ___/|   |  \\
\x1b[1;97m \______  /\___  >__|           |____| \____/|__|_ \\___  >___|   /
\x1b[1;97m        \/     \/                                 \/    \/     \/ 
\x1b[1;94m--------------------------------------------
\x1b[1;92mGet Facebook Token From Cookies by Rozhak-XD
\x1b[1;94m--------------------------------------------''') # DO NOT CHANGE THE AUTHOR'S NAME!
        your_cookies = input("\x1b[1;97m[\x1b[1;92m?\x1b[1;97m] Your Cookie :\x1b[1;93m ")
        with requests.Session() as r:
            try:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01',
                    'scope': ''
                }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
                r.headers.pop(
                    'content-type'
                )
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');break
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0,
                        'user_code': user_code,
                    }
                    r.headers.update({
                        'origin': 'https://m.facebook.com',
                        'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com',
                            'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type,
                            'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format,
                        }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        r.headers.update({
                            'referer': 'https://m.facebook.com/',
                        })
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            print(f"\x1b[1;97m[\x1b[1;92m*\x1b[1;97m] Token :\x1b[1;92m {access_token}");break
                        else:
                            print('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Gagal...');break
            except (ConnectionError, ChunkedEncodingError):
                print("\x1b[1;97m[\x1b[1;93m!\x1b[1;97m]\x1b[1;93m Koneksi Error...", end='\r');time.sleep(3.5);print("                     ", end='\r');break
            except Exception as e:
                print(f"\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m {str(e).title()}...");break