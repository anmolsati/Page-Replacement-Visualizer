import tkinter as tk
from tkinter import ttk, messagebox
from fifo import fifo
from lru import lru
from optimal import optimal
from lfu import lfu
from graph import show_bar_chart, compare_all_algorithms

class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Algorithm Analysis")
        self.root.configure(bg="#ffffff")
        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bg="#ffffff")
        input_frame.pack(pady=15)

        label_style = {"bg": "#ffffff", "fg": "#000000", "font": ("Arial", 11)}

        tk.Label(input_frame, text="Reference String (comma-separated):", **label_style).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.ref_entry = tk.Entry(input_frame, width=40, bg="#f0f0f0", fg="#000000", insertbackground="#000000")
        self.ref_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Number of Frames:", **label_style).grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.frame_entry = tk.Entry(input_frame, bg="#f0f0f0", fg="#000000", insertbackground="#000000")
        self.frame_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Select Algorithm:", **label_style).grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.algo_var = tk.StringVar()
        self.algo_menu = ttk.Combobox(input_frame, textvariable=self.algo_var, state="readonly")
        self.algo_menu['values'] = ("FIFO", "LRU", "Optimal", "LFU")
        self.algo_menu.grid(row=2, column=1, pady=5)

        button_frame = tk.Frame(input_frame, bg="#ffffff")
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="Run", command=self.run_algorithm).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Compare All", command=self.compare_algorithms).pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#ffffff", fg="#007700")
        self.result_label.pack(pady=(0, 5))

        display_frame = tk.Frame(self.root, bg="#ffffff")
        display_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.output_frame = tk.LabelFrame(display_frame, text="Step-by-Step Frames", bg="#ffffff", fg="black", font=("Arial", 11))
        self.output_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.text_output = tk.Text(self.output_frame, height=20, width=50, bg="#f8f8f8", fg="#000000", insertbackground="#000000", relief=tk.FLAT, font=("Courier", 10))
        self.text_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.chart_frame = tk.Frame(display_frame, bg="#ffffff", width=300)
        self.chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=5)

    def run_algorithm(self):
        self.text_output.delete("1.0", tk.END)
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        ref_input = self.ref_entry.get()
        frame_input = self.frame_entry.get()
        algorithm = self.algo_var.get()

        try:
            ref_string = list(map(int, ref_input.split(',')))
            frames = int(frame_input)
            if frames <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter reference string as comma-separated integers and a positive frame number.")
            return

        algo_functions = {
            "FIFO": fifo,
            "LRU": lru,
            "Optimal": optimal,
            "LFU": lfu
        }

        if algorithm not in algo_functions:
            messagebox.showwarning("No Algorithm Selected", "Please select an algorithm.")
            return

        faults, table = algo_functions[algorithm](ref_string, frames)

        self.result_label.config(text=f"Page Faults: {faults}")
        for i, frame_state in enumerate(table):
            self.text_output.insert(tk.END, f"Step {i+1:>2}: Page {ref_string[i]:>2} => {frame_state}\n")

        show_bar_chart(self.chart_frame, algorithm, faults)

    def compare_algorithms(self):
        self.text_output.delete("1.0", tk.END)
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        ref_input = self.ref_entry.get()
        frame_input = self.frame_entry.get()

        try:
            ref_string = list(map(int, ref_input.split(',')))
            frames = int(frame_input)
            if frames <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Use integers and commas correctly, and positive frame number.")
            return

        algorithms = {
            'FIFO': fifo,
            'LRU': lru,
            'Optimal': optimal,
            'LFU': lfu
        }

        results = {name: func(ref_string, frames)[0] for name, func in algorithms.items()}

        self.result_label.config(
            text="Page Faults:\n" + ", ".join([f"{name}: {faults}" for name, faults in results.items()])
        )

        compare_all_algorithms(self.chart_frame, results)

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#ffffff")
    app = PageReplacementGUI(root)
    root.mainloop()
