def move_files(source_folder, destination_folder):
    # Check if folder exists
    # If not, create a folder with the corresponding name 
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through every files in the folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        match = re.search(r'(\d{4})[-_]?\d{2}[-_]?\d{2}', filename)

        if match:
            timestamp = get_modified_datetime(file_path)
            
            year_folder = os.path.join(destination_folder, str(timestamp.year))

            if not os.path.exists(year_folder):
                os.makedirs(year_folder)

            shutil.move(file_path, os.path.join(year_folder, filename))
            print(f'Moved {filename} to {year_folder}')