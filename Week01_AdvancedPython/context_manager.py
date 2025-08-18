# Placeholder for context_manager.py
from contextlib import contextmanager

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


@contextmanager
def open_manager(file, mode):
    try:
        f = open(file, mode)
        yield f
    except Exception as e:
        raise f'{e}'
    finally:
        f.close()


with open_manager('Week01_AdvancedPython/hello.txt', 'r') as f:
    print(f.readlines())

print(f.closed)
