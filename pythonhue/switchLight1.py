import requests, sys

def switch(state):
    url = 'http://192.168.178.20/api/e3oooBFqgU1q8OmRn-8ubp2tfHpomwwWdB8v7ILG/lights/2/state'
    data = '{"on":' + state + '}'
    print data
    response = requests.put(url, data=data)
    print response

switchState = sys.argv[1]
switch(switchState)

