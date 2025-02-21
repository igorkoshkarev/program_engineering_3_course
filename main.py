import file

def get_files(filename: str) -> list[file.File]:
    files = []
    with open(filename, 'r') as f:
        for i in f:
            info = i.split()
            print(info)
            if info[0] == 'pdf':
                files.append(file.PDFFile(*info[1:]))
            elif info[0] == 'png':
                files.append(file.PNGFile(*info[1:]))
            else:
                raise TypeError
    return files


if __name__ == '__main__':
    files = get_files('files.txt')
    for f in files:
        f.print_all()
        print()
