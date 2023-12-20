import os
from pdf2image import convert_from_path

"""file for standardizing comics
from jpeg to jpg
from pdf to jpg
func calling from end to top
"""


def convert_file(path: str):
    """converting and saving files from pdf extension"""
    images = convert_from_path(path)
    for i, image in enumerate(images):
        image.save(f"{'/'.join(path.split('/')[:-1])}/{i}.jpg", "JPEG")


def standard_file(path: str):
    """
    func to convert one file to jpg

    :param path:  like <./Cyberpunk_Edgerunners_Rebecca/2.jpg> string
    :return: 
    """
    filename: str = path.split('/')[-1]  # getting filename
    file_extension: str = filename.split('.')[-1]
    if file_extension in ['png', 'jpg', 'jpeg']:
        # converting image to image
        new_file_path = '/'.join(path.split('/')[:-1]) + '/' + filename.split('.')[0] + '.jpg'
        os.rename(path, new_file_path)
    # other converting
    elif file_extension == 'pdf':
        """lazy to do"""
        return
        # convert_file(path)


def get_dir(path_to_dir_with_files):
    """
    get directory with files to convert
    :param path_to_dir_with_files:
    :return:
    """
    for file in os.listdir(path_to_dir_with_files):
        file_path = f"{path_to_dir_with_files}{file}"
        if os.path.isfile(file_path):
            standard_file(file_path)


def standard_files():
    """
    main func to convert all files
    :return:
    """
    for dr in os.listdir('./'):
        if os.path.isdir(dr):
            get_dir(f'./{dr}/')


def main():
    standard_files()


if __name__ == '__main__':
    main()
