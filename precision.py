import matplotlib.pyplot as plt 
  
# x axis values 
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43] 
# corresponding y axis values 
y = [0.99,1,1,1,0.99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Gesture_NO.') 
# naming the y axis 
plt.ylabel('Precision') 
  
# giving a title to my graph 
plt.title('Precision vs Gesture_NO.') 
  
# function to show the plot 
plt.show() 