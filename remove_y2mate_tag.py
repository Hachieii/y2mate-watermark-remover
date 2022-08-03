import os
import time

with open("path_to_folder.txt","r+") as path_to_folder:
    # Path verify
    if os.stat("path_to_folder.txt").st_size == 0:
        path_to_folder.write(input("What is the path to your folder that needs to be modify? (only one alow at a time) \nFor exampe: C:\\Users\\YourUser\\Music \nYour path: "))
    else:
        while True:
            # Check if it's already has a path
            check = input(r"The system detect that there is one exesting path (" + path_to_folder.read() + r"), do you want to replace it? (y/n) (default: y): ").lower()

            if check == "y" or "":
                path_to_folder.truncate() # Clear all content in the file
                path_to_folder.write(input("What is the path to your folder that needs to be modify? (only one allow at a time) \nFor exampe: C:\\Users\\YourUser\\Music \nYour path: "))
                break

            elif check == "n":
                break

            else:
                print ("Invalid input")

    # Get the folder location
    path_to_folder.seek(0,0)
    path_target = path_to_folder.read()

    def main (folder = path_target):
        os.chdir(folder) # Change to the folder that needed to modify

        for files_name in os.listdir(folder):
            # Check if the name of the files has the watermark
            if files_name[0:13] == "y2mate.com - ":
                os.rename(files_name,files_name[13:])
            
            # Check if it's pointing to a folder
            # If it's a folder then run the function again but working in that child folder instead
            elif os.path.isdir(files_name):
                main(path_target +  "\\" + files_name)

    # Run the function
    main()
    print ("Done! (auto close after 10 secs).")
    time.sleep(10)
