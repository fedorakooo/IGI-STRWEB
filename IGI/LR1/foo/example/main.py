import os

def sort_and_rename_images(folder_path):
    files = os.listdir(folder_path)
    
    image_extensions = ('.png')
    images = [file for file in files if file.lower().endswith(image_extensions)]
    
    images.sort()

    for index, filename in enumerate(images):
        ext = os.path.splitext(filename)[1]
        new_name = f'image{index + 1}{ext}'

        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        os.rename(old_file, new_file)
        print(f'Переименовано: {filename} -> {new_name}')

folder_path = "/home/alexander/353502_Fedorako_23/IGI/LR1/images"
sort_and_rename_images(folder_path)
