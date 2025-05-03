import os

os.mkdir('new_directory') #Create a directory

os.rmdir('directory_name') #Remove a directory

os.listdir('path_to_directory')  #List files in a directory

os.chdir('path_to_directory') #Change the current working directory

os.getcwd() #Get the current working directory

os.rename('old_name', 'new_name') #Rename a file or directory

os.remove('filename') #Remove a file

"""Environment Variables"""

os.getenv('HOME') #Get the value of an environment variable:

os.environ['MY_VAR'] = 'value' #os.environ['MY_VAR'] = 'value'

"""Path Manipulation"""

os.path.join('folder', 'file.txt') #Join paths

os.path.exists('path') #Check if a path exists

os.path.isdir('path') #Check if a path is a directory

os.path.abspath('file.txt') #Get the absolute path of a file

"""System Information"""

os.getlogin() #Get the current user’s name

os.name #Get the system's platform

os.getpid() #Get the process ID

"""Run System Commands"""

os.system('ls')  # For Unix/Linux; for Windows use 'dir'
