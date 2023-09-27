'''
.unstack()      #use in last of code for showing clear DataSet
df.index
df.sort_index(axis=1, ascending=True)
df.sort_values(by="A", ascending=False)
df[0:10]        #Row wise selection
df.loc[dates[0]]
df.loc["20220102":"20220102"["A","B","C"]]
df.at[dates[12],"A"] #Give index value take columns
df.iloc[0:5, : ]
df_numeric.iloc[:,0:31]     # : means all rows & 0:30 means 0 to 30 columns
df[df["A"]>0]
df=df2.copy()
df["A"]=["one","two","three","one","two","three"] #write equal colums times
df['coloum']['index']=[0000]   #for changing value in DataFrame



df.isnull().sum()          # checking for missing values
df.dropna(inplace=True)    # removing the missing values
df.dropna(subset=['embarked','embark_town'],inplace=True)
df['age'].fillna(df['age'].mean(),inplace=True)
df.fillna(0, inplace=True) # replacing the null values
df['Date'].pd.to_datetime(df['Date'])   # replacing the null values in a datetime column
df.duplicated().sum()      # cheking duplicate values
df.drop_duplicates(inplace=True)

df1 = pd.read_csv(data1.csv()
df2 = pd.read_csv(data2.csv()
df = pd.merge(df1,df2, how='outer')

df.corr(method='pearson')
*** pearson | kendall | spearman ***

df.grouby('teams').count()     # for grouping data & also compare after this
*** mean | sum | min | max ***

df=pd.pivot_table(df, index=['A','B'])

df['column'] = df['column'].astype('string')

df['item_price']=df['item_price'].str.replace('$', '')

df[(df['deaths']<50) | (df['deaths']>500)]   # select the column less tha 50 or more than 500 deaths

df[df['regiment'] != 'Dragoons'] # Select all the regiments not named "Dragoons"

df['height'] = df ['height'].apply(lambda x: x* 25.5 if x < 20 else x) •


'''
