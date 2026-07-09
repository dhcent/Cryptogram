import random
import streamlit as st
print("Logic loaded")


global new_quote

def sattolo_cycle(items) -> None:
    """Sattolo's algorithm."""
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]

"""    
    Creates nicely ordered rows based on maximum column length for each.
    Returns a list of lists of words for each row
"""
def wrap_by_words(text, max_cols) -> list[list[str]]:
    words = text.split(" ")
    current_len = 0
    rows, current_row = [], []
    for word in words:
        # for all words not the first, add 1 (to acc for ' ')
        needed = len(word) + (1 if current_row else 0)
        # if the word cannot fit in the current row, add the current row to the list and move to next row
        if needed + current_len > max_cols and current_row:
            rows.append(current_row)
            current_row, current_len = [], 0
        current_row.append(word)
        current_len += needed
    if current_row:
        rows.append(current_row)
    return rows




"""
    Display the cryptogram by putting words in proper rows and indexing to next row accordingly.
    Stores global indexes for each index.
    TODO: 
"""
def render_cryptogram(text, max_cols=15) -> None:
    global_index = 0
    for row in wrap_by_words(text, max_cols):    
        # Identify the column specifications. Let CSS/HTML do the styling
        col_spec = []
        for w_idx, word in enumerate(row):
            if w_idx > 0:
                col_spec.append(1) # space between words
            col_spec.extend([1] * len(word)) #use extend to append two lists
        
        cols = st.columns(col_spec)
        
        col_idx = 0
        for w_idx, word in enumerate(row):
            if w_idx > 0:
                col_idx += 1 # spaces between words
            for char in word:
                with cols[col_idx]:
                    st.text_input(
                        label = f"Letter {global_index + 1}",
                        value = "",
                        max_chars = 1,
                        label_visibility = "hidden",
                        key = f"letter_{global_index}"
                    )
                col_idx += 1
                global_index += 1
            global_index += 1 # For the space between words

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

