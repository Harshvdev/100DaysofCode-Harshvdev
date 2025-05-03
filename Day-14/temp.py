import os

def greet_the_world(planet):
    return f"Greetings, great {planet}."



if __name__ == "__main__":
    print("Running temp.py...")
    try:
        os.remove('imp.txt')
        print("imp.txt deleted.")
    except Exception as e:
        print(f"Error: {e}")

