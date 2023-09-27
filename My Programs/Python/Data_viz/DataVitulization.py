'''
Seaborn inbuild DATA:
1.  anscombe
2.  attention
3.  brain_networks
4.  car_cashes
5.  diamonds
6.  dots
7.  exercise
8.  flights
9.  fmri
10.  gammas
11.  gayser
12.  iris
13.  mpg
14.  penguins
15.  planets
16.  tips 
17.  titanic

'''

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# load dataset
phool = sns.load_dataset("iris")
# draw a line plot
sns.lineplot(x="sepal_length", y="sepal_width", data=phool)
plt.title("Example Graph")   # adding title
plt.show()

'''set limit by adding this:
   plt.xlim(2)
   plt.ylim(3)   

   set names
   plt.xlabel ("MOIZ", size=10)        #font change
   plt.ylabel ("ALI", weight="bold")   #hightlight name

   change figure by adding this:
   plt.figure(figsize=(8,4))
   
    Styles
   * darkgrid
   * whitegrid
   * dark 
   * white
   * ticks    
   change style by adding this:
sns.set_style("dark")
sns.set_style(style=None, rc=None)                

replace lineplot to barplot.. for different graphs  

for changing order
add in plot line:
order=["female", "male"]  

for changing color
add in plot line:
color="pink"  

for customize color 
Google= hex color picker
copy hex code and paste like:
color= "#1515eb"

for changing color shades
add in plot line:
palette="pastel"
#Google: seaborn color palettes python

for changing color saturation
add in plot line:
saturation = 2

for advance changing in graph
add in plot line:
linewidth=3 
facecolor=(2,1,0,1)  #different combination makes different color 
errcolor= ".5"
edgecolor= ".2"  

for changing boxplot position
add in plot line:
dodge=True or dodge =False    

for removing error line
add in plot line:
ci=None           #confidence intervals 

for barplot:

add in plot line:
estimator=mean   or   estimator=median 

for adding symbol in boxplot  #median
add in plot line:
showmeans= True
meanprops= {"marker"            : "*" ,   #not every or more than 1 sign
            "markersize"        : "12" ,
            "markeredgecolor"   : "pink"}
            
plt.savefig('count_plot.pdf')   
            
add in histogram plot for adding Bell-Shaped:
      kde = True

for making scatter plot:
make a scatter plot on x axis is height and y is weight and color is male vs female

for making CatPlot:
sns.catplot(data = df, x='gender', y='age', hue='qualification', kind='violin', col="gender")



For making CountPlot:

plt.figure(figsize=(7, 5))
ax = sns.countplot(data=df, x='gender', hue='qualification', palette=['chartreuse', 'darkviolet'])
plt.xticks(size=12)
plt.xlabel('Gender', size=14)
plt.yticks(size=12)
plt.ylabel('Count', size=12)
plt.title("Gender with respect to qualification", size=16)
ax.set_xticklabels (ax.get_xticklabels (), rotation=40, ha="right")
total = len(df)
for p in ax.patches:
      percentage = f'{100 p.get_height() / total:.1f}%\n'
      x = p.get_x() + p.get_width() / 2
      y = p.get_height()
      ax.annotate(percentage, (x, y), ha='center', va='center')
plt.tight_layout()
plt.show()



For making BOX PLOT:

sns.boxplot(data=df, orient='h', palette='Set2')
plt.show()
   
   
   
For making Correlation plot:

corr = X.corr(method='pearson')
sns.heatmap(corr, annot=True, cmap='RdylGn')
'''


'''
m = plt.hist(df[df["diagnosis"] == "M"].area_worst	,bins=30,fc = (1,0,0,0.5),label = "Malignant")
b = plt.hist(df[df["diagnosis"] == "B"].area_worst	,bins=30,fc = (0,1,0,0.5),label = "Bening")
plt.legend()
plt.xlabel("Radius Mean Values")
plt.ylabel("Frequency")
plt.title("Histogram of Radius Mean for Bening and Malignant Tumors")
plt.show()
frequent_malignant_radius_mean = m[0].max()
index_frequent_malignant_radius_mean = list(m[0]).index(frequent_malignant_radius_mean)
most_frequent_malignant_radius_mean = m[1][index_frequent_malignant_radius_mean]
print("Most frequent malignant radius mean is: ",most_frequent_malignant_radius_mean)

'''
#########################################################

