import requests

header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 1875532baa86e067e37b9a466e0ba1ab3d013f46acff422ccbc04ac0da678726'  # need to generate it
    # first before making api calls
}

url = 'https://gorest.co.in/public/v2/users'


def test_create_and_get_user():
    body = {
        "name": "Prasanth 11",  # needs to be unique everytime
        "email": "p@p1.com",  # needs to be unique everytime
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url=url, headers=header, json=body)
    print(response.json())
    assert response.status_code == 201

    # now get the response for same id -
    getResponse = requests.get(url=url + f"/{response.json()['id']}", headers=header)

    print(getResponse.json())


def test_create_delete_user():

    body = {
        "name": "Prasanth 111",  # needs to be unique everytime
        "email": "p@p11.com",  # needs to be unique everytime
        "gender": "male",
        "status": "active"
    }

    response = requests.post(url=url, headers=header, json=body)
    print(response.json())
    assert response.status_code == 201

    id = response.json()['id']

    # now get the response for same id -
    getResponse = requests.get(url=url + f"/{id}", headers=header)
    print(getResponse.json())

    # now delete the user with this id -
    deleteResponse = requests.delete(url=url + f"/{id}",headers=header)

    # 204 is status code for deleted
    assert deleteResponse.status_code == 204


    # now try to get deleted user -
    deletedUser = requests.get(url=url + f"{id}",headers=header)

    # 404 is status code for not found
    assert deletedUser.status_code == 404
