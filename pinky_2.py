from tkinter import *
import requests

class QuoteGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Quote Generator")
        self.master.geometry("1000x250")

        self.quote_label = Label(self.master, wraplength=800, font=("Courier New", 14))
        self.quote_label.configure(text="")
        self.quote_label.pack(ipadx=20, ipady=20, padx=20, pady=20)

        self.generate_quote_button = Button(self.master, text='Generate!', command=self.generate, width=30, font=("Courier New", 14), bg="#0c20f7", activebackground="#2839f7", fg="white", activeforeground="white")
        self.generate_quote_button.pack()
        self.master.mainloop()

    def generate(self):
        self.quote_label.configure(text="")
        try:
            response = requests.get("https://zenquotes.io/api/random")
            response.raise_for_status()
            quote_json = response.json()
            quote = "{}\n\nBy: {}".format(quote_json[0]['q'], quote_json[0]['a'])
            print(quote)
            self.quote_label.configure(text=quote)
        except requests.exceptions.RequestException as e:
            self.quote_label.configure(text=f"Failed to retrieve quote: {e}")

if __name__ == "__main__":
    root = Tk()
    app = QuoteGenerator(root)
