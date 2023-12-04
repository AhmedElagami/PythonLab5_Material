---
theme: css/mattropolis.css
---
# Matplotlib

---
## How to install Matplotlib?

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
```

---
### How does it work?
- Matplotlib graphs your data on Figures (e.g., windows, Jupyter widgets, etc.).
- Each figure of which can contain one or more Axes, an area where points can be specified in terms of x-y coordinates (or theta-r in a polar plot, x-y-z in a 3D plot, etc.).
- The simplest way of creating a Figure with an Axes is using pyplot.subplots.
- We can then use Axes.plot to draw some data on the Axes:

```python
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
```

--

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_001.png)

> Note that to get this Figure to display, you may have to call plt.show(), depending on your backend. For more details of Figures and backends, see Introduction to Figures.

---
## What are the components of a Figure? 

--

![](https://matplotlib.org/stable/_images/anatomy.png)

---
### What is a Figure?
- The whole figure. 
- The Figure keeps track of 
	- all the child Axes,
	- a group of 'special' Artists (titles, figure legends, colorbars, etc),
	- and even nested subfigures.
 
--
### What is an Axes?
- An Axes is an Artist attached to a Figure that contains 
	- a region for plotting data, 
	- and usually includes two (or three in the case of 3D) Axis objects **(be aware of the difference between Axes and Axis)** that provide ticks and tick labels to provide scales for the data in the Axes.
- Each Axes also has a title (set via set_title()), an x-label (set via set_xlabel()), and a y-label set via set_ylabel()).

> The Axes class and its member functions are the primary entry point to working with the OOP interface, and have most of the plotting methods defined on them (e.g. ax.plot(), shown above, uses the plot method)

--
### What is an Axis?
- These objects set the scale and limits and generate ticks (the marks on the Axis) and ticklabels (strings labeling the ticks).
- The location of the ticks is determined by a Locator object and the ticklabel strings are formatted by a Formatter.
- The combination of the correct Locator and Formatter gives very fine control over the tick locations and labels.

--
### What is an Artist?
- Basically, everything visible on the Figure is an Artist (even Figure, Axes, and Axis objects).
- This includes Text objects, Line2D objects, collections objects, Patch objects, etc.
- When the Figure is rendered, all of the Artists are drawn to the canvas.
- Most Artists are tied to an Axes; such an Artist cannot be shared by multiple Axes, or moved from one to another.

--

The easiest way to create a new Figure is with pyplot:

```python
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

# a figure with one axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
```

> It is often convenient to create the Axes together with the Figure, but you can also manually add Axes later on.

> Note that many Matplotlib backends support zooming and panning on figure windows.

--
---
### What input do you plot? 
- Plotting functions expect numpy.array or numpy.ma.masked_array as input, or objects that can be passed to numpy.asarray.
- Classes that are similar to arrays ('array-like') such as pandas data objects and numpy.matrix may not work as intended. 
- Common convention is to convert these to numpy.array objects prior to plotting. For example, to convert a numpy.matrix

```python
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
```

--

- Most methods will also parse a string-indexable object like a dict, a structured numpy array, or a pandas.DataFrame.
- Matplotlib allows you to provide the data keyword argument and generate plots passing the strings corresponding to the x and y variables.
--

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_002.png)

```python
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.abs(np.random.randn(50)) * 100 }
data['b'] = data['a'] + 10 * np.random.randn(50)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
```

---
### What are the two different Coding Styles?
As noted above, there are essentially two ways to use Matplotlib:
- Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").
- Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot functions for plotting.

---
### How to use the OO-style?
So one can use the OO-style
```python
x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
```

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_003.png)

--
### How to use the OO-style?
```python
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_003.png)