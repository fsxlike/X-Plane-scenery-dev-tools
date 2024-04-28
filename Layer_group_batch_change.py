import os

old_text = "markings -1" #Input the old layer group type you would like to change
new_text = "taxiways +2" #Input the new layer group type
folder_path = "THE PATH OF THE FOLDER CONTAINING .pol FILES, STARTING WITH YOUR DISK LIKE D:/"
#The format should include your disk name (not when modifying things in your disk C). All the sub-folders are seperated using /

def modify_pol(folder_path, old_text, new_text):

    files = os.listdir(folder_path)
    pol_files = [file for file in files if file.endswith('.pol')]

    for pol_file in pol_files:
        file_path = os.path.join(folder_path, pol_file)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line.startswith('LAYER_GROUP'):
                    line = line.replace(old_text, new_text) #This tool is designed to modify orthophoto's layer group
                file.write(line)

modify_pol(folder_path, old_text, new_text)
