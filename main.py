import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <folder_name>")
    sys.exit(1)

folder = sys.argv[1]

if folder == "Costs":
    from Costs.main import main as costs_main
    costs_main()
elif folder == "Dictionary":
    from Dictionary.main import main as dictionary_main
    dictionary_main()
elif folder == "Words":
    from Words.main import main as words_main
    words_main()
else:
    print(f"Unknown folder: {folder}")
    sys.exit(1)
