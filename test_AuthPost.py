import requests

header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 1875532baa86e067e37b9a466e0ba1ab3d013f46acff422ccbc04ac0da678726'  # need to generate it
    # first before making api calls
}

body = {
    "name": "Prasanth 1234",  # needs to be unique everytime
    "email": "p@ppp.com",  # needs to be unique everytime
    "gender": "male",
    "status": "active"
}

url = 'https://gorest.co.in/public/v2/users'


def test_create_and_get_user():
    response = requests.post(url=url, headers=header, json=body)
    print(response.json())
    assert response.status_code == 201

    # now get the response for same id -
    getResponse = requests.get(url=url + f"/{response.json()['id']}", headers=header)

    print(getResponse.json())
