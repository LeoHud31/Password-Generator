import random
import tkinter as tk

#generating the numbers
def generate_numbers():
    num = random.randint(0, 100)
    return num

#function to load words from the file
def load_words():
    try:
        with open('pdictionary.txt') as f:
            words = f.read().split()
        return words
    #error handling for file not found
    except FileNotFoundError:
        print("Error: 'pdictionary.txt' file not found.")
        return []
    
#function to generate words from the dictionary
def generate_words():
    if not words:
        raise ValueError("Word list is empty. Please load words first.")
    return random.choice(words).title()

words = load_words()


#defining the special characters
def generate_special_characters():
    schar = ["+", "-", ",", "."]
    return random.choice(schar)

#function thats creating the password
def generate_password(length=None):
    #gets the words pulled from the dictionary
    word1 = generate_words()
    word2 = generate_words()
    
    #gets the numbers pulled from the random number generator
    num1 = generate_numbers()
    num2 = generate_numbers()
    
    #pulls the special characters from the list
    schar1 = generate_special_characters()
    
    #assembling the password
    password = f"{word1}{num1}{schar1}{word2}{num2}{schar1}"

    return password


#setup the window for the GUI
def setup_window():
    #prevents the password from being generated before the GUI is loaded
    def on_generate_password():
        #adds the generated password to the listbox
        output_list.insert(tk.END, generate_password())

    #main body of the GUI   
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("600x600") # Set the initial size of the window
    window.resizable(True, True) #resizeable window
    tk.Label(window, text="Password Generator", font=("Arial", 18)).pack(pady=20)

    #generate password button
    tk.Button(window, text="Generate Password", command=on_generate_password, font=("Arial", 14)).pack(pady=10)
    
    #frame for the results
    output_frame = tk.LabelFrame(text="Results", font=("Arial", 12))
    output_frame.pack(padx=10, pady=5, fill="both", expand=True)

    #defining the scrollbar
    scrollbar = tk.Scrollbar(output_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    #adding the scrollbar to the window
    output_list = tk.Listbox(output_frame, height=10, font=("Arial", 12), yscrollcommand=scrollbar.set)
    output_list.pack(padx=5, pady=5, fill="both", expand=True)

    scrollbar.config(command=output_list.yview)

    #inserting the initial text into the listbox
    output_list.insert(tk.END, "Generated Password:")

    window.mainloop()


#main function driving events
if __name__ == "__main__":
    try:
        setup_window()
    except Exception as e:
        print(f"An error occurred: {e}")
        