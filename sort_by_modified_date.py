def sort_by_modified_date(folder_path):
    # Get list of files in the folder
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Sort files by modified date
    files.sort(key=lambda x: os.path.getmtime(x))