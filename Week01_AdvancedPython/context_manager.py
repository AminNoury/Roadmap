# Placeholder for context_manager.py


with open('Week01_AdvancedPython/hello.txt', 'r') as f:
    print(f.readlines())
    f.close()


class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exe_type, exe_vals, tracback):
        self.file.close()


with FileManager("Week01_AdvancedPython/hello.txt", "r") as f:
    f.readlines()

print(f.closed)