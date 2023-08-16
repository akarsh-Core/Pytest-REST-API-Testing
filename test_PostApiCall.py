import requests
import test_GetApiCall

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {

    "id": 150,
    "title": "some random title 1",
    "dueDate": "2023-08-16T18:58:17.960Z",
    "completed": True
}


def test_post_activity():
    response = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Activities', headers=header,
                             json=request_payload)

    data = response.json()
    assert response.status_code == 200
    assert data['id'] == request_payload['id']
