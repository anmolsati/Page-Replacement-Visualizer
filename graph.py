import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_bar_chart(master, algorithm_name, faults):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6.5, 3))
    ax.bar([algorithm_name], [faults], color='limegreen')
    ax.set_title(f"{algorithm_name} - Page Faults")
    ax.set_ylabel("Faults")

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def compare_all_algorithms(master, results):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(results.keys(), results.values(), color='limegreen')
    ax.set_title("Page Fault Comparison", fontsize=12)
    ax.set_ylabel("Faults")

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
