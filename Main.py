import random
import tkinter as tk


def load_words():
    with open('pdictionary.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

#numbers
def generate_numbers():
    num = random.randint(0, 100)
    return num

#words
def generate_words():
    with open('pdictionary.txt') as f:
        words = f.read().split()
    word = random.choice(words).title()
    return word

#special characters
def generate_special_characters():
    schar = ["+", "-", ",", "."]
    return random.choice(schar)

#creating the password
def generate_password():
    word1 = generate_words()
    word2 = generate_words()
    
    num1 = generate_numbers()
    num2 = generate_numbers()
    
    schar1 = generate_special_characters()
    
    password = f"{word1}{num1}{schar1}{word2}{num2}{schar1}"
    return password

def setup_window():   
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("600x600")
    tk.Label(window, text="Password Generator", font=("Arial", 18)).pack(pady=20)
    tk.Button(window, text="Generate Password", command=lambda: generate_password()).pack(pady=10)
    output_frame = tk.LabelFrame(text="Results")
    output_frame.pack(padx=10, pady=5, fill="both", expand=True)
    output_list = tk.Listbox(output_frame, height=10)
    output_list.pack(padx=5, pady=5, fill="both", expand=True)
    output_list.insert(tk.END, "Generated Password:")
    output_list.insert(tk.END, generate_password())
    window.mainloop()

if __name__ == "__main__":
    try:
        setup_window()
        load_words()
        generate_password()
        generate_numbers()
    except Exception as e:
        print(f"An error occurred: {e}")
        