import numpy as np
import os


xSize = 51
ySize = 51
filename = "/home/marcus/git/vtkPlot/Point/filename.txt"
A, B = np.meshgrid(np.linspace(-np.pi, np.pi, xSize), np.linspace(-np.pi, np.pi, ySize))
C = np.sin(A)*np.sin(B)
X = np.reshape(A, (-1, np.size(A)))
Y = np.reshape(B, (-1, np.size(B)))
Z = np.reshape(C, (-1, np.size(C)))
np.savetxt("X.txt", X)
np.savetxt("Y.txt", Y)
np.savetxt("Z.txt", Z)
os.system("build/Point "+filename+" "+str(xSize)+" "+str(ySize))