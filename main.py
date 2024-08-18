import datetime
import os
import shutil


def main(source_folder, destination_folder):
    items = os.listdir(source_folder)
    files = [item for item in items if os.path.isfile(os.path.join(source_folder, item))]

    for f in files:
        filepath = os.path.join(source_folder, f)
        modified_date_float = os.path.getmtime(filepath)
        modified_date_datetime = datetime.datetime.fromtimestamp(modified_date_float)
        modified_year = modified_date_datetime.year

        year_folder = os.path.join(destination_folder, str(modified_year))

        if not os.path.exists(year_folder):
            os.makedirs(year_folder)

        file_extension = f.split('.')[-1]
        new_filename = modified_date_datetime.strftime('%Y_%m_%d %H_%M_%S')
        new_filename += f'.{file_extension}'
        new_path = os.path.join(year_folder, new_filename)

        shutil.move(filepath, new_path)


if __name__ == '__main__':
    SOURCE_FOLDER = 'E:\Camera Roll Raw - Copy'
    DESTINATION_FOLDER = 'E:\Camera Roll Organized - Copy'

    main(SOURCE_FOLDER, DESTINATION_FOLDER)

