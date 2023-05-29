import os
def search_files(directory, extension):
    foundFiles = []
    for item in os.listdir(directory):
        itemPath = os.path.join(directory, item)
        if os.path.isdir(itemPath):
            foundFiles.extend(search_files(itemPath, extension))
        elif os.path.isfile(itemPath) and item.endswith(extension):
            foundFiles.append(itemPath)
    return rem_dir(foundFiles)

def rem_dir(foundFiles):
    splitFiles = []
    for element in foundFiles:
        if isinstance(element, str):
            newElement = element.split(directory,1)
            splitFiles.append(newElement)
            del newElement[0]
        else:
            splitFiles.append(element)
    return splitFiles

directory = 'C:\\Users\\jan\\Downloads\\'
extension = '.pdf'
foundFilesUpper = search_files(directory,extension.upper())
foundFiles = search_files(directory, extension)

if foundFilesUpper is not None:
    for i in foundFilesUpper:
        foundFiles.append(i)

for file in foundFiles:
    file = ''.join(file)
    print(file)
print(f'Es wurden {len(foundFiles)} {extension} gefunden')