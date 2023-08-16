import requests


def test_put_activity():

    print('Before updating - ')
    head = {
        'Accept': 'text/plain'
    }

    id = 15

    url = f'https://fakerestapi.azurewebsites.net/api/v1/Activities/{id}'
    response = requests.get(url=url, headers=head)
    print(response.json())

    print("After updating - ")

    request_payload = {

        "id": 150,
        "title": "some random title {}".format(id),
        "dueDate": "2023-08-16T18:58:17.960Z",
        "completed": True
    }

    header_put = {
        'Accept': 'text/plain',
        'Content-Type': 'application/json'
    }

    response = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Activities', headers=header_put,
                             json=request_payload)

    data = response.json()
    print(data)
    assert response.status_code == 200
