def get_modified_date(file_path):
    modified_date_timestamp = os.path.getmtime(file_path)
    modified_date_datetime = datetime.datetime.fromtimestamp(modified_date_timestamp)
    return modified_date_datetime