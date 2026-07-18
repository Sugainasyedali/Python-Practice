import sys
try:
    print(f"Hello {sys.argv[1]}")
except:
    print("Usage: python greet.py name")