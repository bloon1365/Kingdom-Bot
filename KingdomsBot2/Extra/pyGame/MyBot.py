import matplotlib.pyplot as plt

x = [1,2,3,5,7,8,9,1,2,3,5]
y = [5,7,4,6,7,8,6,4,3,2,1]


plt.scatter(x,y,label = 'skitskat', color = 'k')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting Graph\nCheck it out ')
plt.legend()

plt.show()