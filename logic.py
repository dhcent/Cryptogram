import random


global new_quote

def sattolo_cycle(items) -> None:
    """Sattolo's algorithm."""
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]


alphabet = list("abcdefghijklmnopqrstuvwxyz")
quotes = ["Whether you think you can or you think you cannot, you are correct."]

selected_quote = random.choice(quotes)

# alphabet is now randomly shuffled
sattolo_cycle(alphabet)

new_quote = []

print(alphabet)

# iterate through and build the scrambled string based on the randomly shuffled alphabet
for i, char in enumerate(selected_quote):
    if char.isalpha():    
        new_quote.append(alphabet[ord(char.lower()) - ord("a")])
    else:
        new_quote.append(char)


# new_quote is now scrambled of the original
new_quote = "".join(new_quote)

