import mimetypes

# takes in user input of a file name, and prints it's file media type
def main():
    file_name = input('File name: ')
    print(get_file_extension(file_name))

# gets file media type of input file name
def get_file_extension(file_name):
    file_name = file_name.strip()
    # use first index of file_extension, as it is type, second index is encoding
    file_extension =  mimetypes.guess_type(file_name)[0]
    if file_extension == None:
        return 'application/octet-stream'
    else:
        return file_extension

main()