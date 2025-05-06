from pathlib import Path, PurePath

# 1. Create a Path object (representing a file or directory)
p = Path("learn-sys.py")
print("Path object:", p)

# 2. Check if the path exists (file or directory)
print("\np.exists():", p.exists())  # True if file/folder exists, False otherwise

# 3. Check if it’s a file or a directory
print("p.is_file():", p.is_file())  # True if it's a file
print("p.is_dir():", p.is_dir())    # True if it's a directory

# 4. Get the name of the file
print("\np.name:", p.name)  # 'example.txt'

# 5. Get the file stem (name without extension)
print("p.stem:", p.stem)  # 'example'

# 6. Get the file extension
print("p.suffix:", p.suffix)  # '.txt'

# 7. Get the parent directory
print("\np.parent:", p.parent)  # 'folder'

# 8. Combine paths (using `/` operator)
folder = Path("folder")
new_file = folder / "new_file.txt"
print("\nCombined path:", new_file)  # 'folder/new_file.txt'

# 9. Check if the parent directory exists and create if not
if not folder.exists():
    folder.mkdir()  # Create the 'folder' directory if it doesn't exist
    print("\nCreated folder:", folder)

# 10. PurePath for path manipulation without touching the filesystem
pure_p = PurePath("folder") / "example.txt"
print("\nPurePath object:", pure_p)  # 'folder/example.txt'

# 11. List all .txt files in the current directory
print("\nList of .txt files in current directory:")
for txt_file in Path(".").glob("*.txt"):
    print(txt_file)

# 12. Get the absolute (full) path
print("\np.resolve():", p.resolve())  # Full absolute path of the file

# 13. Create a new file (example with 'touch()' method)
new_file.touch()  # Creates 'new_file.txt' in 'folder' if it doesn’t exist

print("\nDone.")
