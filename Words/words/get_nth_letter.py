def get_nth_letter(words):
# TODO: add list of positions to test different cases
    result = ""
    for word in words:
        n = int(input("Enter the position (n): "))  # Input the n-th position
        if n < len(word):  # Ensure the n-th position is within the bounds of the word
            result += word[n]  # Add the n-th letter of the word
    return result
    


       