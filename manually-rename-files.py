# Assume the source folder only contains folders with files
# No subfolders in folders

if __name__ == '__main__':
    source = "E:\\Camera Roll Copy"
    
    for dir in os.listdir(source):
        folder = os.path.join(source, dir)
        
        for index, item in enumerate(os.listdir(folder)):
            current_file_path = os.path.join(folder, item)
            
            # Unique ID for each file
            number_of_files = len(os.listdir(folder))
            number_of_digits = math.log10(len(os.listdir(folder)))
            number_of_digits = math.ceil(number_of_digits)
            
            extension = item.split('.')[-1]
            modified_date_timestamp = get_modified_datetime(current_file_path)
            modified_date_datetime = modified_date_timestamp.strftime("%Y_%m_%d %H_%M_%S")
            
            index_s = f'{index:04}'
            index_s = str(index_s)
            
            # Naming convention for each file
            new_file_path = os.path.join(folder, f'{str(date_time)} {index_s}.{extension}')

            rename_file(current_file_path, new_file_path)