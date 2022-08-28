import matplotlib.pyplot as plt
con=[23.4,17.8,25,34,40]
zones=['east','west','north','south','central']
plt.axis("equal")
plt.pie(con,labels=zones,explode=[0,0,0.2,0,0],autopct="%1.2f%%")
plt.show()
#292
