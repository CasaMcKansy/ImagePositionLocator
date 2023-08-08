# Sript: ImagePositionLocator
#
#               -----------------------------------------------------------------------------------------
# Description:  | Script to determine the pixel position of the mouse cursor in an image after a click. |
#               -----------------------------------------------------------------------------------------
#
# Author: Caspar Hoyer
# Version: 1.0.0  08/08/2023


# Import of Packages
import matplotlib.pyplot as plt
from PIL import Image

# Import of Image
image_path = "plain_silhouette.jpg"  # adjust image name
image = Image.open(image_path)

# Creates Figure
fig, ax = plt.subplots()
ax.imshow(image)

# Creates Position Dictionary
positions = {}

# Mouse event handler
def onclick(event):
    x, y = event.xdata, event.ydata  # returns coordinates
    positions[len(positions) + 1] = (x, y)  # stores in dict
    ax.plot(x, y, 'ro')  # plots a dot
    plt.draw()

cid = fig.canvas.mpl_connect("button_press_event", onclick)

# Shows the Image
plt.show()

# Prints the Positions
print(positions)