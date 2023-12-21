import requests


def create_table(url: str):
    requests.post(url=url, json={
        'name': "new_created_table",
    })


def update_table(url: str):
    res = requests.put(url=url, json={
        'table_name': "new_created_table",
        "photo_url": "https://w.forfun.com/fetch/5f/5fae8b9ce29a10950b001db52779ca78.jpeg",
    })


def delete_table(url):
    res = requests.delete(url=url, json={"table_name": "new_created_table"})


def main():
    url = "http://127.0.0.1:5000/api/"
    delete = "delete_table"
    create = "create_new_table"
    update = "update_table"
    create_table(url=url + create)
    update_table(url=url + update)
    delete_table(url=url + delete)


if __name__ == '__main__':
    main()
