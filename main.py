import os

def get_all_paths(current_path , all_files):
    in_dir = os.listdir(current_path)
    files_in_dir = []
    directories = []

    for file in in_dir:
        if os.path.isdir(file):
            directories.append(current_path + '/' +  file)
        elif '.html' in file:
            files_in_dir.append(current_path + '/' + file)
        elif '.js' in file:
            files_in_dir.append(current_path + '/' + file)
        elif '.css' in file:
            files_in_dir.append(current_path + '/' + file)

    all_files += files_in_dir
    for directory in directories:
        get_all_paths(directory, all_files)


def main():
    current_dir_path = '.'
    all_files = []
    get_all_paths(current_dir_path, all_files)

    print(all_files)
 
if __name__ == "__main__":
    main()
