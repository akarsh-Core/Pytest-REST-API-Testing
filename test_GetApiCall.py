import requests

"""
swagger link - https://fakerestapi.azurewebsites.net/index.html
"""


def test_get_all_activities():
    header = {
        'Accept': 'text/plain'
    }

    url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'
    response = requests.get(url=url, headers=header)

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_specific_activity_by_id():
    head = {
        'Accept': 'text/plain'
    }

    id = 15

    url = f'https://fakerestapi.azurewebsites.net/api/v1/Activities/{id}'
    response = requests.get(url=url, headers=head)

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()['id'] == id
