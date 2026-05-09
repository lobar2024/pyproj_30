def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

def caesar_cipher(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def longest_common_prefix(words):
    if not words: return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("Hello"))                        # False

    text = "python java python c python java"
    print(word_frequency(text))  # {'python':3, 'java':2, 'c':1}

    msg = "Hello World"
    enc = caesar_cipher(msg, 3)
    dec = caesar_cipher(enc, -3)
    print(f"Shifr: {enc}")  # Khoor Zruog
    print(f"Ochiq: {dec}")  # Hello World

    words = ["flower", "flow", "flight"]
    print(longest_common_prefix(words))  # fl
