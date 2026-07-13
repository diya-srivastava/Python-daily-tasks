def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()

    
    return cleaned_text == cleaned_text[::-1]


word = input("Enter a word or sentence: ")

if is_palindrome(word):
    print("✅ It is a palindrome!")
else:
    print("❌ It is not a palindrome.")