import os
import shutil


def organize_files(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = os.path.splitext(filename)[1][1:]
            target_folder = os.path.join(target_dir, file_extension.upper())

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_folder, filename)
            shutil.move(source_path, target_path)
            print(f"Moved {filename} to {target_folder}")
