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
            print(newElement)
        else:
            splitFiles.append(element)
    return splitFiles


directory = 'C:\\Users\#\Desktop\\testus\\'
extension = '.pdf'
foundFiles = search_files(directory, extension)

print(foundFiles)
print(len(foundFiles))