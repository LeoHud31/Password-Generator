import random
import tkinter as tk

#loads the words from the dictionary file into the file
def load_words():
    with open('pdictionary.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

#generating the numbers
def generate_numbers():
    num = random.randint(0, 100)
    return num

#generating the words
def generate_words():
    with open('pdictionary.txt') as f:
        words = f.read().split()
    word = random.choice(words).title()
    return word

#defining the special characters
def generate_special_characters():
    schar = ["+", "-", ",", "."]
    return random.choice(schar)

#function thats creating the password
def generate_password(length=None):
    word1 = generate_words()
    word2 = generate_words()
    
    num1 = generate_numbers()
    num2 = generate_numbers()
    
    schar1 = generate_special_characters()
    
    password = f"{word1}{num1}{schar1}{word2}{num2}{schar1}"

    return password


#setup the window for the GUI
def setup_window():
    #prevents the password from being generated before the GUI is loaded
    def on_generate_password():
        output_list.insert(tk.END, generate_password())

    #main body of the GUI   
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("600x600")
    window.resizable(True, True)
    tk.Label(window, text="Password Generator", font=("Arial", 18)).pack(pady=20)

    tk.Button(window, text="Generate Password", command=on_generate_password, font=("Arial", 14)).pack(pady=10)
    output_frame = tk.LabelFrame(text="Results", font=("Arial", 14))
    output_frame.pack(padx=10, pady=5, fill="both", expand=True)
    output_list = tk.Listbox(output_frame, height=10, font=("Arial", 14))
    output_list.pack(padx=5, pady=5, fill="both", expand=True)
    output_list.insert(tk.END, "Generated Password:")
    window.mainloop()


#main function driving events
if __name__ == "__main__":
    try:
        setup_window()
        load_words()
        generate_password()
        generate_numbers()
    except Exception as e:
        print(f"An error occurred: {e}")
        