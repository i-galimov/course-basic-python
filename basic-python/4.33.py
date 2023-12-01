import os

text = input()

def write_and_read(text):
    tmp_path = os.path.abspath('/tmp')
    file_name = text.replace(" ", "_") + ".txt"
    file_path = os.path.join(tmp_path, file_name)
    open(file_path, "w").write(text)
    return(open(file_path, "r").read())

print(write_and_read(text))