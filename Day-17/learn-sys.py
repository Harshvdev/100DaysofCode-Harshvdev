import sys

# 1. Command-line arguments
# Run as: python script.py hello 123
print("sys.argv:", sys.argv)            # ['script.py', 'hello', '123']
print("First argument:", sys.argv[1])   # hello
print("Second argument:", sys.argv[2])  # 123

# 2. Exit the script
# sys.exit("Exiting program...")        # Stops the program here (uncomment to test)

# 3. Module search paths
print("\nsys.path:")                    # Shows where Python looks for modules
for p in sys.path:
    print(" ", p)

# 4. Detect current OS
print("\nsys.platform:", sys.platform)  # e.g., 'win32' (Windows), 'linux', 'darwin'

# 5. Full Python version
print("\nsys.version:", sys.version)    # e.g., '3.11.6 (main,...)'

# 6. Structured Python version
print("sys.version_info:", sys.version_info)  # e.g., sys.version_info(major=3, minor=11, ...)

# 7. Loaded modules (shows count)
print("\nLoaded modules count:", len(sys.modules))  # All modules Python has loaded so far

# 8. Standard input/output/error
print("\nsys.stdin:", sys.stdin)        # Default input stream (keyboard)
print("sys.stdout:", sys.stdout)       # Default output stream (console)
print("sys.stderr:", sys.stderr)       # Error output stream

# 9. Default string encoding
print("\nsys.getdefaultencoding():", sys.getdefaultencoding())  # Usually 'utf-8'

# 10. Recursion limit
print("sys.getrecursionlimit():", sys.getrecursionlimit())      # Default is usually 1000
# sys.setrecursionlimit(2000)          # (Optional) set higher limit, be careful with this

print("\nDone.")
