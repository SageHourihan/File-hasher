# Assignment 4. Sage Hourihan 

import hashlib, os

# Creating a function to collect input on the file name
def filename():
  file = input("Type file name: ")
  return file

def get_hash_of_binary_file_contents (file_path, algorithm = 'MD5'):

  """This function will read and hash the contents of a file. 
  :param file_path: The path to the file to be hashed.
  :type file_path: str.
  :param algorithm: The hashing algorithm to be used. Defaults to 'MD5'.
  :type algorithm: str.
  :returns: str -- The hash of the contents of the file.
  """
  file_contents = read_binary_file(file_path)
  file_hash = get_hash_of_string(file_contents, algorithm)
  return file_hash

def get_hash_of_string (string, algorithm = 'MD5'):
  if algorithm == 'MD5': 
    hash_object = hashlib.md5(string)
    hash_digest = hash_object.hexdigest()
  else:
    hash_digest = ''
  return hash_digest

def read_binary_file (file_path):
  try:
    file_object = open(file_path,'rb')
    file_contents = file_object.read()
  except:
    raise
  return file_contents

def print_hash():
  printHash = input("Would you like to print the hash?: ")
  if printHash == "Yes" or printHash == "yes":
    print(get_hash_of_binary_file_contents(x))
  else:
    print("Goodbye")
  
# Calling the functions

x = filename()
get_hash_of_binary_file_contents(x)
#get_hash_of_string(b"insert string here")
read_binary_file(x)
print_hash()
  
