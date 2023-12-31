import requests
import pyfiglet

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)

        data ={
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Zip]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection [!]')

def main():
    ip = input('Введите IP адрес:')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()