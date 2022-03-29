def intel(target):
    import json
    import requests as rq

    key = 't2pRa0wSFcfMz4CYUhtb85Y7mFyCvUEb'
    ip = target
    url = f'https://api.shodan.io/shodan/host/{ip}?key={key}'

    response = rq.get(url)
    response = response.json()

    print(json.dumps(response, indent=4, sort_keys=True))

intel('8.8.8.8')
