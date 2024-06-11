#done.
#this is the program that happened in my tcs digital exam internal.
def rearrange_word(word, num):
    # Check if the length of the word is divisible by the given number
    if len(word) % num != 0:
        return "Invalid input: Length of the word is not divisible by the given number"

    # Calculate the size of each chunk
    chunk_size = len(word) // num

    # Rearrange the word
    rearranged_word = ""
    for i in range(num):
        chunk = word[i * chunk_size : (i + 1) * chunk_size]
        rearranged_word += chunk[::-1]  # Reverse each chunk and concatenate
    return rearranged_word

# Example usage
word = "PROGRAM"
num = 4
print("Original word:", word)
print("Number of parts:", num)
print("Rearranged word:", rearrange_word(word, num))