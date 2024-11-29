# main.py

from words.get_nth_letter import get_nth_letter

def main():
    
    
    words = ["yoda", "best", "has"]   
    new_word = get_nth_letter(words)
    print(f"New word formed from position: {new_word}")
    
    
if __name__ == "__main__":
    main()
