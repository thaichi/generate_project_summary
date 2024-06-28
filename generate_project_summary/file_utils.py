def is_binary(file_path):
    with open(file_path, 'rb') as file:
        return b'\0' in file.read(1024)

def read_file_contents(file_path):
    encodings = ['utf-8', 'shift_jis']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                print(f'Reading file: {file_path}')
                return file.read()
        except UnicodeDecodeError:
            pass
    return ''
