import os
import requests
from bot.config import config
import base64
import json
from convertio import Client


def get_dir(path_to_dir_with_files):
    for file in os.listdir(path_to_dir_with_files):
        file_path = f"{path_to_dir_with_files}{file}"
        if os.path.isfile(file_path):
            standard_file(file_path)


i = 1


# def convert(base_str: str, path: str):
#     global i
#     base64_string = "ваша_base64_строка_здесь"
#
#     decoded_data = base64.b64decode(base64_string)
#
#     with open(path + str(i), 'wb') as file:
#         file.write(decoded_data)
#         i += 1


def convert_file(path: str, filename: str, to: str):
    if '.DS' in filename:
        return
    api = Client(config.services.convertio_api_key)
    print(path)
    upload_id = api.convert_by_filename(
        fp=path,
        output_format=to
    )

    st = filename.split('.')
    r = requests.get(f'https://api.convertio.co/convert/{upload_id}/status')
    print('resp', r.text)

    # r = json.loads(str(r))
    # with open('data.json', 'w+') as f:
    #     f.write(str(r))

    # put_args = {
    #     "id": "",
    #     "filename": filename,
    # }
    # requests.put(url, data=put_args)

    # base_id = file['data']['id']
    # convert(base_id, '/'.join(path.split('/')[:-1]))


def standard_file(path: str):
    filename = path.split('/')[-1]
    file_extension = filename.split('.')[-1]
    if file_extension in ['png', 'jpg', 'jpeg']:
        new_file_path = '/'.join(path.split('/')[:-1]) + '/' + filename.split('.')[0] + '.jpg'
        os.rename(path, new_file_path)
    else:
        convert_file(path, filename, '.jpg')


def main():
    path: str
    # standard_file(path)
    for dr in os.listdir('./'):
        if os.path.isdir(dr):
            get_dir(f'./{dr}/')

    pass


if __name__ == '__main__':
    main()
