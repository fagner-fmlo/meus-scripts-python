def osint_shodan(target):
    import json
    import requests as rq

    key = ''
    ip = target
    url = f'https://api.shodan.io/shodan/host/{ip}?key={key}'

    response = rq.get(url)
    response = response.json()

    print(json.dumps(response, indent=4, sort_keys=True))

osint_shodan('8.8.8.8')
