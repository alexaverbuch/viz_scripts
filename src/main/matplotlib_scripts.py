import matplotlib.pyplot as plt
import numpy as np

def example_plot_linear():
    plt.plot([1, 2, 3])
    plt.ylabel('some numbers')
    plt.show()

def example_plot_linear_points():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], linewidth=2.0)    
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
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^', linewidth=2.0)    
    plt.ylabel('some numbers')
    plt.show()

def example_antialiased():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    # red dashes, blue squares and green triangles
    line1, line2, line3 = plt.plot(t, t, 'r', t, t ** 2, 'bs', t, t ** 3, 'g^', linewidth=2.0)    
    # turn off antialising
    antialiased = True
    line1.set_antialiased(antialiased)     
    plt.ylabel('some numbers')
    plt.show()

def example_colors():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    # red dashes, blue squares and green triangles
#    lines = plt.plot(t, t, t, t ** 2, t, t ** 3)    
    line1, line2, line3 = plt.plot(t, t, t, t ** 2, t, t ** 3)    
    # use keyword args
#    plt.setp(lines, color='r', linewidth=2.0)
    plt.setp(line1, color='r', linewidth=2.0)
    plt.setp(line2, color='b', linewidth=2.0)
    plt.setp(line3, color='g', linewidth=2.0)
    # or matlab style string value pairs
#    plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
    plt.ylabel('y stuff')
    plt.xlabel('x stuff')
    plt.title("title")
    plt.show()

def example_properties():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    # red dashes, blue squares and green triangles
    line1, = plt.plot(t, t ** 3)
            
    # use keyword args
    plt.setp(line1, color='r', linewidth=2.0, alpha=0.5,)
    plt.ylabel('y stuff')
    plt.xlabel('x stuff')
    plt.title("title")
    plt.show()

def example_two_plots():
    def f(t): return np.exp(-t) * np.cos(2 * np.pi * t)
    
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    
    plt.figure(1)
    #  subplot(numrows, numcols, fignum) 
    #  plt.subplot(2,1,1) also valid 
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    
    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    
    plt.ylabel('y stuff')
    plt.xlabel('x stuff')
    plt.title("title")
    plt.show()

def example_multiple_figures():
    plt.figure(1)                # the first figure
    plt.subplot(211)             # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)             # the second subplot in the first figure
    plt.plot([4, 5, 6])

    plt.figure(2)                # a second figure
    plt.plot([4, 5, 6])            # creates a subplot(111) by default

    plt.figure(1)                # figure 1 current; subplot(212) still current
    plt.subplot(211)             # make subplot(211) in figure1 current
    plt.title('Easy as 1,2,3')   # subplot 211 title
    plt.show()

def example_text():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    
    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    
    t = plt.xlabel('Smarts', fontsize=14, color='red')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ ' + r'$\sigma_i=15$')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()

def example_annotate():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = plt.plot(t, s, lw=2)
    
    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                )
    
    plt.ylim(-2, 2)
    plt.show()
