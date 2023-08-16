import requests

para = {
    'page': 1,
    'per_page': 3
}

"""
The apis for this are available at - https://gorest.co.in/ 
"""

url = 'https://gorest.co.in/public/v2/users'


def test_get_users():
    response = requests.get(url=url, params=para)
    print(response.json())
    assert response.status_code == 200
