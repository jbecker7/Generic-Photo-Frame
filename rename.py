import os
import json


def rename_files_in_directory(directory_path):
    new_filenames = []

    i = 1

    for filename in os.listdir(directory_path):
        new_filename = f"Ima{i}.jpg"
        new_filenames.append(new_filename)

        old_file = os.path.join(directory_path, filename)
        new_file = os.path.join(directory_path, new_filename)

        os.rename(old_file, new_file)

        i += 1

    return new_filenames


# Replace with your directory path
directory_path = ""
new_filenames = rename_files_in_directory(directory_path)

with open("images.json", "w") as file:
    json.dump(new_filenames, file)

print(f"New filenames written to images.json: {new_filenames}")
