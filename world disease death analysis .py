#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the libraries for analysis and visualisation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


cd C:\Users\shaqu\Desktop\company questionaires\Dataleads


# In[3]:


# a vairiable created for our main dataset to read the file easily
data= 'masterfile.csv'


# In[4]:


# reading the dataset
df= pd.read_csv(data)
df


# In[5]:


# for displaying the maximum columns
pd.set_option('display.max_columns', None)
df.head(10)


# In[6]:


#checking the data types
df.info()


# In[7]:


df.describe() 


# In[8]:


# sorted the value into general float format
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[9]:


df.head()


# In[10]:


## create a new column for total death which sums up all the deaths from different diseases
df['Total_Deaths'] = df.iloc[:, 4::].sum(axis= 1)


# In[11]:


m= df
m.loc['Diseases deaths']=df.iloc[:, 4:].sum(axis= 0)
df= pd.DataFrame(m)
df


# In[12]:


df['Total_Deaths']


# # Section I: SEGREGATION
# You are provided a csv file (attached). Using python libraries at your disposal, run a loop to extract up to 10 datasets (preferably .xlxs format) based on different criterias (e.g., country, prevalence, etc.). Kindly document your steps as you go through the process.

# In[13]:


## we checked single column unique values!!
coutry_array= df['Entity'].unique()

## we converted array to list for using the list method!!
country_lst = coutry_array.tolist()


# In[14]:


## created a loop to extract different datasets from the same masterfile!!

# for i in country_lst:
#     grp = df.groupby(df.Entity) ## grouping the columns
#     temp = grp.get_group(i)
#     print(f'we created dataset from the masterfile: { i}')
#     temp.to_excel(i + ".xlsx")


# In[15]:


cd C:\Users\shaqu\Desktop\company questionaires\Dataleads\outputs


# In[16]:


## created a loop to extract 10 different datasets from the same masterfile with respect to coutries name!!

for i in country_lst[:10]:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created dataset from the masterfile: { i}')
    temp.to_excel(i + ".xlsx")


# ## Section II: VISUALISATION
# a. Using the same dataset, run a loop to generate up to 10 infographics using a suitable python library to visualize trends. The infographics need to be of the same format - i.e., you are required to generate them in a loop. Kindly document your steps as you go through the process.
# 
# b. Write up an article (~500 words) for any one, or a combination of, these infographics.

# In[17]:


# FInding the correlations between the features!!
corr1= df[['Diabetes (deaths)', 'Respiratory diseases (deaths)', 'Cardiovascular diseases (deaths)', 'Kidney disease (deaths)', 'Liver diseases (deaths)', 'Parkinson disease (deaths)', 'Meningitis (deaths)']].corr()
corr1


# We can say that from our correlation factor value that it is high chance patient who dies from Diabetes have some Liver disease aswell ~98.1%

# In[18]:


## creating a loop to plot different coutries graphs based on Year and Suicide deaths
# for i in country_lst:
#     grp = df.groupby(df.Entity) ## grouping the columns
#     temp = grp.get_group(i)
#     print(f'we created graphs from the masterfile based on suicide deaths and year: { i}')
#     plt.plot(temp['Year'], temp['Suicide (deaths)'])
#     plt.title(i)
#     plt.xlabel('Years')
#     plt.ylabel('Deaths')
#     plt.show()
    


# In[19]:


## creating a loop to plot 10 different coutries graphs based on Year and Suicide deaths
for i in country_lst[:10]:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on suicide deaths and year: { i}')
    plt.plot(temp['Year'], temp['Suicide (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()


# In[20]:


from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')
plt.savefig(pp, format='pdf')


# In[21]:


## creating a loop to plot 10 different coutries scatter graphs based on Year and Suicide deaths
for i in country_lst[:10]:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on suicide deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Suicide (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()
   


# From the above graph we come into a conclusion that Argentina have thee maximums deaths due to Suicide around ~5500 from year 2013- 2017

# In[22]:


for i in country_lst[::10]:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on Terrorism deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Terrorism (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()
    plt.savefig('plot.pdf')
    plt.savefig(pp, format='pdf')


# I plotted different scatter plots to get insights that which country have the highest deaths due to terrorism!!
# we get out answer from the plots that contry Afghanistan had most deaths from Terrrorism of around 6000 people deaths in year 2015-2017
# 
# And the country which have least deaths from terrorism is Comoros which is almost 0 since 1994- 2000 and 1 case was happened in year 1992 only!

# In[23]:


df.head()


# In[24]:


## created dfx dataframe to add a row column for total sum of the each diseases!
m= df
m.loc['Diseases deaths']=df.iloc[:, 4:-1].sum(axis= 0)
dfx= pd.DataFrame(m)
dfx

df_neural_diseases= dfx[['Meningitis (deaths)', 'Dementia (deaths)', 'Parkinson disease (deaths)']]
df_neural_diseases


# In[25]:


df[['Meningitis (deaths)', 'Dementia (deaths)', 'Parkinson disease (deaths)']].sum(axis = 0, skipna = True)


# # Comparing deaths of Terrorism and Cardiovascular diseases  for India and Pakistan 

# In[26]:


ind_pak= df.loc[(df['Entity']== 'India') | (df['Entity']=='Pakistan')]
ind_pak[::10]


# In[27]:


date= ind_pak['Year']


# In[28]:


date_time=pd.to_datetime(date, format='%Y')
date1=date_time[:28]


# In[29]:


ind_pak_terror= ind_pak[['Entity', 'Terrorism (deaths)']]
ind_pak_terror[::10]


# In[30]:


x= ind_pak_terror.loc[df['Entity']== 'Pakistan']
y= ind_pak_terror.loc[df['Entity']== 'India']


# In[31]:


x.reset_index(drop = True).filter('Terrorism (deaths)')
# plt.scatter(x,y, c='coral')
xx= x['Terrorism (deaths)'].values
xx


# In[32]:


y.reset_index(drop = True).filter('Terrorism (deaths)')
# plt.scatter(x,y, c='coral')
yy= y['Terrorism (deaths)'].values 
yy


# In[33]:


plt.scatter(date1, xx)
plt.xlabel('Years')
plt.ylabel('Terrotism Deaths')
plt.title('Pakistan')

plt.plot(date1, xx)
plt.xlabel('Years')
plt.ylabel('Terrotism Deaths')
plt.title('Pakistan')


# From the above graph we came upto a conclusion that there is a surge in terrorrism attack in Pakistan during 1996- 2003 and during 2010- 2013.
# 
# highest death was in year 2013 which was around 3000 deaths

# In[34]:


plt.scatter(date1, yy)
plt.xlabel('Years')
plt.ylabel('Terrotism Deaths')
plt.title('India')

plt.plot(date1, yy)
plt.xlabel('Years')
plt.ylabel('Terrotism Deaths')
plt.title('India')


# I created a new data frame for country name India and Pakistan using all death causes colummns. Then comparing the terrorism deaths and Cardiovascular Heart diseases deaths. 
# 
# From our Terrorism and deaths graph we can say that there was terror attack in Pakistan which killed around 2700 people in Pakistan during year 2010 -2013. 
# 
# And In India there was a surge in terror attack during year 2004 – 2012 which killed around 700 people deaths per annum.
# 

# In[35]:


alc_neur_prob= df[['Alcohol use disorders (deaths)', 'Drug use disorders (deaths)', 'Parkinson disease (deaths)']]
alc_neur_prob.corr()


# In[36]:


ind_pak_CardioDeaths= ind_pak[['Entity', 'Cardiovascular diseases (deaths)']]
ind_pak_CardioDeaths[::10]


# In[37]:


x= ind_pak_CardioDeaths.loc[df['Entity']== 'Pakistan']
y= ind_pak_CardioDeaths.loc[df['Entity']== 'India']


# In[ ]:





# We can see that there is a high correlation between those use drugs are addicted by alcohals and also have a high chance of Parkinson death in future!!

# In[38]:


y.reset_index(drop = True).filter('Cardiovascular diseases (deaths)')
# plt.scatter(x,y, c='coral')
yy= y['Cardiovascular diseases (deaths)'].values 
yy


# In[39]:


plt.scatter(date1, yy)
plt.xlabel('Years')
plt.ylabel('Cardiovascular diseases (deaths)')
plt.title('India')


plt.xlabel('Years')
plt.ylabel('Cardiovascular diseases (deaths)')


# In india Cardiovascular heart problems are increases significantly from year 2010- 2017 which cause deaths of around 2700000 people

# In[40]:


x.reset_index(drop = True).filter('Cardiovascular diseases (deaths)')
# plt.scatter(x,y, c='coral')
xx= x['Cardiovascular diseases (deaths)'].values 
xx


# In[41]:


plt.scatter(date1, xx)
plt.xlabel('Years')
plt.ylabel('Cardiovascular diseases (deaths)')
plt.title('Pakistan')

plt.xlabel('Years')
plt.ylabel('Cardiovascular diseases (deaths)')


# In Pakistan Cardiovascular heart problems are increases significantly from year 2012- 2017 which cause deaths of around 400000 people

# So here we can conclude that people who died due to cardiovascular disesases are higher in Inida as compare to Pakistan by around 2300000 people

# In[42]:


## convert the jupyter notebook into Pdf format


# In[43]:


# pip install -U notebook-as-pdf


# In[44]:


df


# In[45]:


for i in country_lst[:15]:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on Liver diseases deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Liver diseases (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()
    


# Created graphs for liver disease death an dyear of first 10 countries.
# We can conclude from the graphs that coountries name Argentina and Andean Latin America have the most deaths due to Liver diseas of aroound ~10000 and ~13000 in year 2017
# 
# And we can also conclude that from the year 2000 there is a significant increase in liver diseases in all of the countries!

# In[46]:


for i in country_lst[::15]:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on Cancer diseases deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Cancers (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()


# from our graphs we can conclude that among the list of our coutries graphs above country name India and Africa have the maximum cancer deaths which around 900000 and 600000.
# 
# Cancer deaths also increases from the year 2007 to 2017 very surgely!

# In[47]:


# created a favourite list of countries!!
fav_conty= df.loc[(df['Entity']== 'India') | (df['Entity']== 'Pakistan') | (df['Entity']== 'Canada') | (df['Entity']== 'United States') | (df['Entity']== 'United Kingdom')]
fav_conty


# In[48]:


fav_cont= fav_conty['Entity'].unique()

## we converted array to list for using the list method!!
fav_conty_lst = fav_cont.tolist()


# In[49]:


for i in fav_conty_lst:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on Cancer diseases deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Cancers (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()


# From the cancer death graph of our favourite country list it is clear that in every coutnries there is aan increase in deaths of people from cancer disease.
# 
# India has the max deaths rate of around ~900000 in year 2017, and US comes to 2 with around ~700000 deaths in year 2016.
# 
# from Our grapgh of UK country we can say that they had taken some measure to control deaths from Cancer in year between 1997- 2000 but again increase from year 2007.

# In[50]:


for i in fav_conty_lst:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on Malaria diseases deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Malaria (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()


# From our favourite list of countries we can conclude that there is almost no death because of Malaria in United States, UK  and Canada
# 
# But Saddenly Malaria deaths in India and Pakistan are signifcantly high around~ 90000 in year between 1990 to 2000 and around~ 6000 in year 2000- 2005 in Pakistan
# 
# Although India is decreases the death rate of malaria from last 20 years, but It needs to be eradicated as US and UK.
# It shows that India and PAkistan is more unhygienic and lives in dirty environment that leads to Malaria mosquitoes 

# In[51]:


for i in fav_conty_lst:
    grp = df.groupby(df.Entity) ## grouping the columns
    temp = grp.get_group(i)
    print(f'we created graphs from the masterfile based on TB diseases deaths and year: { i}')
    plt.scatter(temp['Year'], temp['Tuberculosis (deaths)'])
    plt.title(i)
    plt.xlabel('Years')
    plt.ylabel('Deaths')
    plt.show()


# In India year between 1990- 2000 there were around 600000 died because of TB which was reduces to 400000 in year 2017. But it should be reduced more and India needs to work on the TB health issues.
# 
# While in US, UK and Canada it already reducces to less than 800 people died due to TB from year 2000- 2017

# In[ ]:




