import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab as plb
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, Polygon
from pylab import *
from sys import argv

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
    
#    plt.xlim(-2, 4)
    plt.ylim(-2, 2)
    plt.show()

def example_line_styles():
    t = np.arange(0.0, 1.0, 0.1)
    s = np.sin(2 * np.pi * t)
    linestyles = ['_', '-', '--', ':']
    markers = []
    for m in Line2D.markers:
        try:
            if len(m) == 1 and m != ' ':
                markers.append(m)
        except TypeError:
            pass
    
    styles = linestyles + markers
    
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
    
    
    axisNum = 0
    for row in range(5):
        for col in range(5):
            axisNum += 1
            ax = plt.subplot(5, 5, axisNum)
            style = styles[axisNum % len(styles) ]
            color = colors[axisNum % len(colors) ]
            plt.plot(t, s, style + color, markersize=10)
            ax.set_yticklabels([])
            ax.set_xticklabels([])
    
    plt.show()
    
def example_hatching():
    fig = plt.figure()
    ax1 = fig.add_subplot(131)
    ax1.bar(range(1, 5), range(1, 5), color='red', edgecolor='black', hatch="/")
    ax1.bar(range(1, 5), [6] * 4, bottom=range(1, 5), color='blue', edgecolor='black', hatch='//')
    ax1.set_xticks([1.5, 2.5, 3.5, 4.5])
    
    ax2 = fig.add_subplot(132)
    bars = ax2.bar(range(1, 5), range(1, 5), color='yellow', ecolor='black') + \
        ax2.bar(range(1, 5), [6] * 4, bottom=range(1, 5), color='green', ecolor='black')
    ax2.set_xticks([1.5, 2.5, 3.5, 4.5])
    
    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    for bar, pattern in zip(bars, patterns):
         bar.set_hatch(pattern)
    
    ax3 = fig.add_subplot(133)
    ax3.fill([1, 3, 3, 1], [1, 1, 2, 2], fill=False, hatch='\\')
    ax3.add_patch(Ellipse((4, 1.5), 4, 0.5, fill=False, hatch='*'))
    ax3.add_patch(Polygon([[0, 0], [4, 1.1], [6, 2.5], [2, 1.4]], closed=True,
                          fill=False, hatch='/'))
    ax3.set_xlim((0, 6))
    ax3.set_ylim((0, 2.5))
    
    plt.show()
    
def example_histogram():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    
    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
    
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)
    
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    
    plt.show()
    
def example_histogram_3():
    # first create a single histogram
    mu, sigma = 200, 25
    x = mu + sigma * plb.randn(10000)
        
    plb.figure(6)
    
    # finally: make a multiple-histogram of data-sets with different length
    x0 = mu + sigma * plb.randn(10000)
    x1 = mu + sigma * plb.randn(7000)
    x2 = mu + sigma * plb.randn(3000)
    
    n, bins, patches = plb.hist([x0, x1, x2], 10, histtype='bar')
    
    plb.show()
    
def example_annotate_advanced():
    fig = figure(2)
    fig.clf()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, 5), ylim=(-5, 3))

    el = Ellipse((2, -1), 0.5, 0.5)
    ax.add_patch(el)

    ax.annotate('$->$', xy=(2., -1), xycoords='data',
                xytext=(-150, -140), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="->",
                                patchB=el,
                                connectionstyle="angle,angleA=90,angleB=0,rad=10"),
                )

    ax.annotate('fancy', xy=(2., -1), xycoords='data',
                xytext=(-100, 60), textcoords='offset points',
                size=20,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="fancy",
                                fc="0.6", ec="none",
                                patchB=el,
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                )

    ax.annotate('simple', xy=(2., -1), xycoords='data',
                xytext=(100, 60), textcoords='offset points',
                size=20,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="simple",
                                fc="0.6", ec="none",
                                patchB=el,
                                connectionstyle="arc3,rad=0.3"),
                )

    ax.annotate('wedge', xy=(2., -1), xycoords='data',
                xytext=(-100, -100), textcoords='offset points',
                size=20,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="wedge,tail_width=0.7",
                                fc="0.6", ec="none",
                                patchB=el,
                                connectionstyle="arc3,rad=-0.3"),
                )


    ann = ax.annotate('wedge', xy=(2., -1), xycoords='data',
                xytext=(0, -45), textcoords='offset points',
                size=20,
                bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec=(1., .5, .5)),
                arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                fc=(1.0, 0.7, 0.7), ec=(1., .5, .5),
                                patchA=None,
                                patchB=el,
                                relpos=(0.2, 0.8),
                                connectionstyle="arc3,rad=-0.1"),
                )

    ann = ax.annotate('wedge', xy=(2., -1), xycoords='data',
                xytext=(35, 0), textcoords='offset points',
                size=20, va="center",
                bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none"),
                arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                fc=(1.0, 0.7, 0.7), ec="none",
                                patchA=None,
                                patchB=el,
                                relpos=(0.2, 0.5),
                                )
                )


    show()

def example_arrows():
    
    rates_to_bases = {'r1':'AT', 'r2':'TA', 'r3':'GA', 'r4':'AG', 'r5':'CA', 'r6':'AC', \
            'r7':'GT', 'r8':'TG', 'r9':'CT', 'r10':'TC', 'r11':'GC', 'r12':'CG'}
    
    numbered_bases_to_rates = dict([(v, k) for k, v in rates_to_bases.items()])
    
    lettered_bases_to_rates = dict([(v, 'r' + v) for k, v in rates_to_bases.items()])
    
    def add_dicts(d1, d2):
        """Adds two dicts and returns the result."""
        result = d1.copy()
        result.update(d2)
        return result
    
    def make_arrow_plot(data, size=4, display='length', shape='right', \
            max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5, \
            normalize_data=False, ec=None, labelcolor=None, \
            head_starts_at_zero=True, rate_labels=lettered_bases_to_rates, \
            **kwargs):
        """Makes an arrow plot.
    
        Parameters:
    
        data: dict with probabilities for the bases and pair transitions.
        size: size of the graph in inches.
        display: 'length', 'width', or 'alpha' for arrow property to change.
        shape: 'full', 'left', or 'right' for full or half arrows.
        max_arrow_width: maximum width of an arrow, data coordinates.
        arrow_sep: separation between arrows in a pair, data coordinates.
        alpha: maximum opacity of arrows, default 0.8.
    
        **kwargs can be anything allowed by a Arrow object, e.g.
        linewidth and edgecolor.
        """
    
        xlim(-0.5, 1.5)
        ylim(-0.5, 1.5)
        gcf().set_size_inches(size, size)
        xticks([])
        yticks([])
        max_text_size = size * 12
        min_text_size = size
        label_text_size = size * 2.5
        text_params = {'ha':'center', 'va':'center', 'family':'sans-serif', \
            'fontweight':'bold'}
        r2 = sqrt(2)
    
        deltas = {\
            'AT':(1, 0),
            'TA':(-1, 0),
            'GA':(0, 1),
            'AG':(0, -1),
            'CA':(-1 / r2, 1 / r2),
            'AC':(1 / r2, -1 / r2),
            'GT':(1 / r2, 1 / r2),
            'TG':(-1 / r2, -1 / r2),
            'CT':(0, 1),
            'TC':(0, -1),
            'GC':(1, 0),
            'CG':(-1, 0)
            }
    
        colors = {\
            'AT':'r',
            'TA':'k',
            'GA':'g',
            'AG':'r',
            'CA':'b',
            'AC':'r',
            'GT':'g',
            'TG':'k',
            'CT':'b',
            'TC':'k',
            'GC':'g',
            'CG':'b'
            }
    
        label_positions = {\
            'AT':'center',
            'TA':'center',
            'GA':'center',
            'AG':'center',
            'CA':'left',
            'AC':'left',
            'GT':'left',
            'TG':'left',
            'CT':'center',
            'TC':'center',
            'GC':'center',
            'CG':'center'
            }
    
    
        def do_fontsize(k):
            return float(clip(max_text_size * sqrt(data[k]), \
                min_text_size, max_text_size))
    
        A = text(0, 1, '$A_3$', color='r', size=do_fontsize('A'), **text_params)
        T = text(1, 1, '$T_3$', color='k', size=do_fontsize('T'), **text_params)
        G = text(0, 0, '$G_3$', color='g', size=do_fontsize('G'), **text_params)
        C = text(1, 0, '$C_3$', color='b', size=do_fontsize('C'), **text_params)
    
        arrow_h_offset = 0.25  #data coordinates, empirically determined
        max_arrow_length = 1 - 2 * arrow_h_offset
    
        max_arrow_width = max_arrow_width
        max_head_width = 2.5 * max_arrow_width
        max_head_length = 2 * max_arrow_width
        arrow_params = {'length_includes_head':True, 'shape':shape, \
            'head_starts_at_zero':head_starts_at_zero}
        ax = gca()
        sf = 0.6   #max arrow size represents this in data coords
    
        d = (r2 / 2 + arrow_h_offset - 0.5) / r2    #distance for diags
        r2v = arrow_sep / r2                      #offset for diags
    
        #tuple of x, y for start position
        positions = {\
            'AT': (arrow_h_offset, 1 + arrow_sep),
            'TA': (1 - arrow_h_offset, 1 - arrow_sep),
            'GA': (-arrow_sep, arrow_h_offset),
            'AG': (arrow_sep, 1 - arrow_h_offset),
            'CA': (1 - d - r2v, d - r2v),
            'AC': (d + r2v, 1 - d + r2v),
            'GT': (d - r2v, d + r2v),
            'TG': (1 - d + r2v, 1 - d - r2v),
            'CT': (1 - arrow_sep, arrow_h_offset),
            'TC': (1 + arrow_sep, 1 - arrow_h_offset),
            'GC': (arrow_h_offset, arrow_sep),
            'CG': (1 - arrow_h_offset, -arrow_sep),
            }
    
        if normalize_data:
            #find maximum value for rates, i.e. where keys are 2 chars long
            max_val = 0
            for k, v in data.items():
                if len(k) == 2:
                    max_val = max(max_val, v)
            #divide rates by max val, multiply by arrow scale factor
            for k, v in data.items():
                data[k] = v / max_val * sf
    
        def draw_arrow(pair, alpha=alpha, ec=ec, labelcolor=labelcolor):
            #set the length of the arrow
            if display == 'length':
                length = max_head_length + (max_arrow_length - max_head_length) * \
                    data[pair] / sf
            else:
                length = max_arrow_length
            #set the transparency of the arrow
            if display == 'alph':
                alpha = min(data[pair] / sf, alpha)
            else:
                alpha = alpha
            #set the width of the arrow
            if display == 'width':
                scale = data[pair] / sf
                width = max_arrow_width * scale
                head_width = max_head_width * scale
                head_length = max_head_length * scale
            else:
                width = max_arrow_width
                head_width = max_head_width
                head_length = max_head_length
    
            fc = colors[pair]
            ec = ec or fc
    
            x_scale, y_scale = deltas[pair]
            x_pos, y_pos = positions[pair]
            arrow(x_pos, y_pos, x_scale * length, y_scale * length, \
                fc=fc, ec=ec, alpha=alpha, width=width, head_width=head_width, \
                head_length=head_length, **arrow_params)
    
            #figure out coordinates for text
            #if drawing relative to base: x and y are same as for arrow
            #dx and dy are one arrow width left and up
            #need to rotate based on direction of arrow, use x_scale and y_scale
            #as sin x and cos x?
            sx, cx = y_scale, x_scale
    
            where = label_positions[pair]
            if where == 'left':
                orig_position = 3 * array([[max_arrow_width, max_arrow_width]])
            elif where == 'absolute':
                orig_position = array([[max_arrow_length / 2.0, 3 * max_arrow_width]])
            elif where == 'right':
                orig_position = array([[length - 3 * max_arrow_width, \
                    3 * max_arrow_width]])
            elif where == 'center':
                orig_position = array([[length / 2.0, 3 * max_arrow_width]])
            else:
                raise ValueError, "Got unknown position parameter %s" % where
    
    
    
            M = array([[cx, sx], [-sx, cx]])
            coords = dot(orig_position, M) + [[x_pos, y_pos]]
            x, y = ravel(coords)
            orig_label = rate_labels[pair]
            label = '$%s_{_{\mathrm{%s}}}$' % (orig_label[0], orig_label[1:])
    
            text(x, y, label, size=label_text_size, ha='center', va='center', \
                color=labelcolor or fc)
    
        for p in positions.keys():
            draw_arrow(p)
    
        #test data
    all_on_max = dict([(i, 1) for i in 'TCAG'] + \
            [(i + j, 0.6) for i in 'TCAG' for j in 'TCAG'])
    
    realistic_data = {
            'A':0.4,
            'T':0.3,
            'G':0.5,
            'C':0.2,
            'AT':0.4,
            'AC':0.3,
            'AG':0.2,
            'TA':0.2,
            'TC':0.3,
            'TG':0.4,
            'CT':0.2,
            'CG':0.3,
            'CA':0.2,
            'GA':0.1,
            'GT':0.4,
            'GC':0.1,
        }
    
    extreme_data = {
            'A':0.75,
            'T':0.10,
            'G':0.10,
            'C':0.05,
            'AT':0.6,
            'AC':0.3,
            'AG':0.1,
            'TA':0.02,
            'TC':0.3,
            'TG':0.01,
            'CT':0.2,
            'CG':0.5,
            'CA':0.2,
            'GA':0.1,
            'GT':0.4,
            'GC':0.2,
        }
    
    sample_data = {
            'A':0.2137,
            'T':0.3541,
            'G':0.1946,
            'C':0.2376,
            'AT':0.0228,
            'AC':0.0684,
            'AG':0.2056,
            'TA':0.0315,
            'TC':0.0629,
            'TG':0.0315,
            'CT':0.1355,
            'CG':0.0401,
            'CA':0.0703,
            'GA':0.1824,
            'GT':0.0387,
            'GC':0.1106,
        }
    
    
    d = None
    if len(argv) > 1:
        if argv[1] == 'full':
            d = all_on_max
            scaled = False
        elif argv[1] == 'extreme':
            d = extreme_data
            scaled = False
        elif argv[1] == 'realistic':
            d = realistic_data
            scaled = False
        elif argv[1] == 'sample':
            d = sample_data
            scaled = True
    if d is None:
        d = all_on_max
        scaled = False
    if len(argv) > 2:
        display = argv[2]
    else:
        display = 'length'

    size = 4
    figure(figsize=(size, size))

    make_arrow_plot(d, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=scaled, head_starts_at_zero=True, size=size)

    draw()

    show()

def example_line_charts_from_csv():
    fname = 'test.txt'
    fname2 = 'test2.txt'
    
#    # test 1; use ints
#    plotfile(fname, (0, 1, 2))
#    
#    # test 2; use names
#    plotfile(fname, ('column0', 'column1', 'column2'))
#    
#    # test 3; use semilogy for volume
#    plotfile(fname, ('column0', 'column1', 'column2'), plotfuncs={'column1': 'semilogy'})
    
#    # test 4; use semilogy for volume
#    plotfile(fname, (0, 1, 2), plotfuncs={1:'semilogy'})
    
    #test 5; single subplot
    plotfile(fname, ('column0', 'column1', 'column2'), subplots=False)
    
    # test 6; labeling, if no names in csv-file
    plotfile(fname2, cols=(0, 1, 2), delimiter=',',
             names=['$x$', '$f(x)=x^2$', '$f(x)=x^3$'])
    
    # test 7; more than one file per figure--illustrated here with a single file
    plotfile(fname, cols=(0, 1), delimiter=',')
    plotfile(fname, cols=(0, 2), newfig=False, delimiter=',') # use current figure
    gca().set_xlabel(r'$x$')
    gca().set_ylabel(r'$f(x) = x^2, x^3$')
    
#    # test 8; use bar for volume
#    plotfile(fname, (0, 1, 2), plotfuncs={1:'bar'})
    
    show()
