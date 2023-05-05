import requests

r = requests.get('http://httpbin.org')
r.status_code
r.ok
r.headers

r.text
r.encoding
r.url
r.content

params = {
    'city':'seoul',
    'name':'suji'
}
r= requests.get('http://httpbin.org/get', params=params)
r.ok
r.headers
r.json()

r = requests.post('http://httpbin.org/post', data={'password':'hello'})
r.ok
r.headers
r.json()