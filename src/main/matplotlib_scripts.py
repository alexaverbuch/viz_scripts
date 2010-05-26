import matplotlib.pyplot as plt
import numpy as np

def example_plot_linear():
    plt.plot([1, 2, 3])
    plt.ylabel('some numbers')
    plt.show()

def example_plot_linear_points():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])    
    plt.ylabel('some numbers')
    plt.show()

def example_plot_linear_points_axis():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    #[xmin, xmax, ymin, ymax]
    plt.axis([0, 6, 0, 20])
    plt.ylabel('some numbers')
    plt.show()

def example_plot_colors_shapes():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')    
    plt.ylabel('some numbers')
    plt.show()

