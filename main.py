import file

def get_files(filename: str) -> list[file.File]:
    files = []
    with open(filename, 'r') as f:
        for i in f:
            info = i.split()
            if info[0] == 'pdf':
                files.append(file.PDFFile(*info))
            elif info[0] == 'png':
                files.append(file.PNGFile(*info))
            else:
                raise TypeError
    return files

