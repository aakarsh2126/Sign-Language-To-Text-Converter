import matplotlib.pyplot as plt 
  
# x axis values 
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43] 
# corresponding y axis values 
y = [198,190,200,203,177,188,204,205,209,202,212,209,194,228,208,187,184,193,189,199,201,212,199,199,212,200,196,187,205,205,232,216,187,196,199,182,206,195,200,203,209,211,170,199] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Gesture_NO.') 
# naming the y axis 
plt.ylabel('Support') 
  
# giving a title to my graph 
plt.title('Support vs Gesture_NO.') 
  
# function to show the plot 
plt.show() 