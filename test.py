import os
import fnmatch
import time

from diffusionmodel import DiffusionModel
from diffusionsettigs import DiffusionSettings
from prompt import Prompt
def check_files(directory, file_extension):
    files_of_type = []
    for file in os.listdir(directory):
        if fnmatch.fnmatch(file, f"*.{file_extension}"):
            files_of_type.append(file)
    return files_of_type

def check_subdirectories(directory):
    subdirectories = [subdir for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]
    for subdir in subdirectories:
        if(str(subdir)=='unet'):
            return True
    return False


def main():
    dire=[]
    with open("slozky.txt", "r") as file:
        directories = [line.strip() for line in file]
    with open("prompt.txt", "r") as file:
        prompts = [line.strip() for line in file]
    last_modified_time = os.path.getmtime("prompt.txt")
    
    file_extension = "ckpt"

    for directory in directories:
        namespil=directory.split('@')

        found_files = check_files(namespil[0], file_extension)
        subdirectories = check_subdirectories(namespil[0])
        if found_files or subdirectories:
            print(f"Složka {namespil[0]}:")
            if found_files:
                print("Existuje ckpt")
            if subdirectories:
                print("Existuje unet")
            dire.append(DiffusionModel(namespil[0],namespil[1]))
        else:
            print(f"Složka {namespil[0]} neobsahuje žádné soubory ani podsložky.")
            directories.remove(directory)

    for x in prompts:
            make_prompt(x,dire)
    while(True):
            filename = "prompt.txt"
            time.sleep(5)
            if last_modified_time != os.path.getmtime(filename):
                with open(filename, 'r') as file:
                        lines = file.readlines()
                for line in lines[len(prompts) :]: 
                    make_prompt(line,dire)
                    prompts.append(line)
                print("Soubor byl změněn.")
                last_modified_time = os.path.getmtime(filename)
def make_prompt(x,dire):
            with open('prompt.txt', 'w') as file:
                file.write('1')
            prompt=Prompt(x)
            if(prompt.isForModel('None')):
                for dic in dire:
                    dic.diffuse(prompt)
            else:
                for dic in dire:
                    if(prompt.isForModel(dic.name)):
                        dic.diffuse(prompt)
            prompt.isdone=True
            with open('prompt.txt', 'w') as file:
                file.write('0')

if __name__ == "__main__":
    settings = DiffusionSettings()
    settings.load_from_command_line()
    main()
