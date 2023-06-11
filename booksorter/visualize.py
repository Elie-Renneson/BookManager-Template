import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

sorting_steps = []  # Array to store sorting steps for visualization

def visualize_sorting(arr):
    sorting_steps.append(arr.copy())  # Add a copy of the array to the sorting steps

def visualize_sorting_animation():
    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(sorting_steps[0])), sorting_steps[0], width=1)

    def animate(frame):
        ax.clear()  # Clear the plot
        ax.bar(range(len(sorting_steps[frame])), sorting_steps[frame], width=1)  # Plot the current step
        ax.set_xlim(0, len(sorting_steps[frame]))  # Set x-axis limits based on the actual array length

    def on_key(event):
        if event.key == 'escape':
            plt.close(fig)
            sys.exit()  # Exit the program

    fig.canvas.mpl_connect('key_press_event', on_key)
    anim = animation.FuncAnimation(fig, animate, frames=len(sorting_steps), repeat=False)
    plt.pause(0.1 * len(sorting_steps))  # Delay between each step
    plt.show()
