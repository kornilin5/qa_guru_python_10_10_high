import os
def path_picture():
    resource_folder = os.path.abspath('tests/resources')
    image_name = 'ZnugKfP5UJk.jpg'
    image_path = os.path.join(resource_folder, image_name)
    return image_path
