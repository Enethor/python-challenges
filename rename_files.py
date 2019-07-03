import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r'C:\Users\Zé Pedro\Documents\prank')
    saved_path = os.getcwd()
    os.chdir(r'C:\Users\Zé Pedro\Documents\prank')
    #print(file_list)
    
    #(2) for each file, rename filename
    translation_table = str.maketrans("0123456789", "          ", "0123456789")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(translation_table))
    os.chdir(saved_path)

rename_files()
    
