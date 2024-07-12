def rename_file(current_file_path, new_file_path):
    try:
        os.rename(current_file_path, new_file_path)
        print(f"File renamed from {current_file_path} to {new_file_path}")
    except FileNotFoundError:
        print(f"Error: The file {current_file_path} was not found.")
    except PermissionError:
        print(f"Error: Permission denied to rename the file {current_file_path}.")
    except Exception as e:
        print(f"Error: {e}")