import os


SEARCHING_TEXT = 'YP0302'
DELIMITER = '/'

founded = set()

def search_in_folder(folder='C:\git\pda\RFHMR'):
    for dirpath, dirname, filenames in os.walk(folder):
        full_paths = [dirpath.replace('\\', '/') + DELIMITER + i for i in filenames if i.endswith('asp')]
        for f in full_paths:
            # print ('Fullpath:', f)
            # print 'Fullpath:', f
            try:
                with open(f, 'r', encoding='utf-8', errors='ignore') as file:
                    for line in file.readlines():
                        if SEARCHING_TEXT in line:
                            founded.add(f)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    search_in_folder()
    for i in founded:
        print('Path: ', i)