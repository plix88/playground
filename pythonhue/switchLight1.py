import requests, sys

switchState = sys.argv[1]

url = 'http://192.168.178.20/api/e3oooBFqgU1q8OmRn-8ubp2tfHpomwwWdB8v7ILG/lights/1/state'
data = '{"on":' + switchState + '}'

response = requests.put(url, data=data)
