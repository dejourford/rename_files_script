# Import OS Library
import os

# Change directory to desired directory
base_path = "C:/Users/dejou/workspace/pcap_samples"
os.chdir(base_path)

# List all folders inside directory
parent_folders = os.listdir()

for folder in parent_folders:
    folder_path = os.path.join(base_path, folder)
    
    # Change the directory to each sub folder
    os.chdir(folder_path)
    
    # Assign the file_to_edit variable to the items in each folder
    folder_of_files = os.listdir()
    
    # for each file in the folder, append .pcap to the file name and rename file
    for file in folder_of_files:
        if not file.endswith('.pcap'):
            
            new_name = file + ".pcap"
            
            os.rename(file, new_name)
            print(f"file renamed to:', {new_name}")
        else:
            print("The file already has the .pcap extension!")
