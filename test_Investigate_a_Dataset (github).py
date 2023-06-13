#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [tmdb-movies]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# This dataset contains information on 10,000 movies from The Movie Database (TMDb), including details such as user ratings and revenue. By analyzing this data, we can discover interesting information.
# 
# 
# <table>
# 	<thead>
# 		<tr>
# 			<th>Feature</th>
# 			<th>Description</th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<td><code>movie_id</code></td>
# 			<td>A unique identifier for each movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>imdb_id</code></td>
# 			<td>A unique identifier for each movie on IMDB</td>
# 		</tr>
# 		<tr>
# 			<td><code>cast</code></td>
# 			<td>The names of the lead and supporting actors</td>
# 		</tr>
# 		<tr>
# 			<td><code>director</code></td>
# 			<td>The director of the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>budget</code></td>
# 			<td>The budget of the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>genre</code></td>
# 			<td>The genre(s) of the movie (e.g., Action, Comedy, Thriller)</td>
# 		</tr>
# 		<tr>
# 			<td><code>homepage</code></td>
# 			<td>A link to the movie&rsquo;s homepage</td>
# 		</tr>
# 		<tr>
# 			<td><code>id</code></td>
# 			<td>Another unique identifier for each movie (same as&nbsp;<code>movie_id</code>)</td>
# 		</tr>
# 		<tr>
# 			<td><code>keywords</code></td>
# 			<td>Keywords or tags related to the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>original_title</code></td>
# 			<td>The original title of the movie before translation or adaptation</td>
# 		</tr>
# 		<tr>
# 			<td><code>overview</code></td>
# 			<td>A brief description of the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>popularity</code></td>
# 			<td>A numeric value representing the movie&rsquo;s popularity</td>
# 		</tr>
# 		<tr>
# 			<td><code>production_companies</code></td>
# 			<td>The production company(ies) behind the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>production_countries</code></td>
# 			<td>The country(ies) where the movie was produced</td>
# 		</tr>
# 		<tr>
# 			<td><code>release_date</code></td>
# 			<td>The date when the movie was released</td>
# 		</tr>
# 		<tr>
# 			<td><code>revenue</code></td>
# 			<td>The worldwide revenue generated by the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>runtime</code></td>
# 			<td>The duration of the movie in minutes</td>
# 		</tr>
# 		<tr>
# 			<td><code>tagline</code></td>
# 			<td>The tagline of the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>vote_average</code></td>
# 			<td>The average rating received by the movie</td>
# 		</tr>
# 		<tr>
# 			<td><code>budget_adj</code></td>
# 			<td>The budget of the movie in terms of 2010 dollars</td>
# 		</tr>
# 		<tr>
# 			<td><code>revenue_adj</code></td>
# 			<td>The revenue generated by the movie in terms of 2010 dollars</td>
# 		</tr>
# 	</tbody>
# </table>
#  
# 
# 
# ### Question(s) for Analysis
# >What is the relation between the revenue and other variables?
# 
# >Which are movies with the highest profit and lowest profit?
# 
# >What is the top 10 most profitable movies?
# 
# 
# > **Tip**: Once you start coding, use NumPy arrays, Pandas Series, and DataFrames where appropriate rather than Python lists and dictionaries. Also, **use good coding practices**, such as, define and use functions to avoid repetitive code. Use appropriate comments within the code cells, explanation in the mark-down cells, and meaningful variable names. 

# In[1]:


#  import  for all of the packages that i plan to use.
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Upgrade pandas to use dataframe.explode() function. 
#!pip install --upgrade pandas==0.25.0


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# ### General Properties
# 

# In[3]:


# Load the data and print out a few lines. 


# In[4]:


tmdb_df=pd.read_csv('tmdb-movies.csv')


# In[5]:


tmdb_df.head()


# In[6]:


tmdb_df.shape


# In[7]:


# I will dive in for more observations 


# In[8]:


tmdb_df.info()


# In[9]:


# Observations


# ### 1- There are 10866 columns and 21 columns.
# ### 2- 'id'is an int , and 'imdb_id' is string i will remove 'imdb_id' which is not given any useful     information.
# ### 3-'homepage', 'tagline', 'keywords', 'overview','budget_adj',and'revenue_adj' columns are not helpful for the analysis so I will delete them from the data frame.
# ### 4-'release_date' column is important. but I need to change the data type to the date type
# ### 5-'budget', and 'revenue'  are important columns by simply subtraction the revenue from the budget column we can get the profit.
# ### 6-We should investigate null and missing values

# 
# ### Data Cleaning
# 
#  

# In[10]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.


# In[11]:


# chick for duplicate value 
tmdb_df.duplicated().sum()


# In[12]:


# remove duplicate vale
tmdb_df.drop_duplicates(inplace=True)


# In[13]:


tmdb_df.duplicated().sum()


# In[14]:


# Remove unuseful columns 
tmdb_df.columns


# In[15]:


tmdb_df.drop(['imdb_id','homepage','tagline','keywords','overview','budget_adj','revenue_adj'],axis=1,inplace=True)


# In[16]:


tmdb_df.columns


# In[17]:


tmdb_df.info()


# In[18]:


tmdb_df.isnull().sum()


# In[19]:


tmdb_df.dropna(inplace=True)


# In[20]:


tmdb_df.isnull().sum()


# In[21]:


tmdb_df.info()


# In[22]:


# change the release_date from object to datetime 
tmdb_df.release_date=pd.to_datetime(tmdb_df.release_date)
tmdb_df.info()


# In[23]:


tmdb_df.release_date.head()


# In[24]:


tmdb_df.sample(10)


# In[25]:


tmdb_df[tmdb_df.runtime==0]


# In[26]:


tmdb_df[tmdb_df.runtime==0].shape[0]


# In[27]:


# After chick for runtime=0, I observed that also the budget and revenue also equal zero(0)
# Then I will remove them from the data set because they unuseful for analysis
tmdb_df.drop(tmdb_df.index[tmdb_df.runtime==0],axis=0,inplace=True)


# In[28]:


tmdb_df[tmdb_df.runtime==0]


# In[29]:


tmdb_df.info()


# In[30]:


tmdb_df.shape


# In[31]:


tmdb_df.describe()


# In[32]:


tmdb_df = tmdb_df.rename(columns={'vote_average': 'rating'})
tmdb_df.columns


# In[33]:


tmdb_df.describe().round(2)


# In[34]:


tmdb_df.tail()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. **Compute statistics** and **create visualizations** with the goal of addressing the research questions that you posed in the Introduction section. You should compute the relevant statistics throughout the analysis when an inference is made about the data. Note that at least two or more kinds of plots should be created as part of the exploration, and you must  compare and show trends in the varied visualizations. 
# 
# 
# 
# > **Tip**: - Investigate the stated question(s) from multiple angles. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables. You should explore at least three variables in relation to the primary question. This can be an exploratory relationship between three variables of interest, or looking at how two independent variables relate to a single dependent variable of interest. Lastly, you  should perform both single-variable (1d) and multiple-variable (2d) explorations.
# 
# 
# ### Research Question 1 (What is the relation between the revenue and other variables?)

# In[35]:


sns.pairplot(tmdb_df);


# In[36]:


# I will check the correlation between Popularity and Revenue


# In[37]:


# Function to plot the corrlation between variables
def corrlation(tmdb_df, x, y, title):
    tmdb_df.plot(x,y,kind='scatter')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)

# Now the function is ready to use let's try it   
    
# input data frame,xlable,ylable,title
corrlation(tmdb_df,'popularity','revenue','Poularity Vs Revenue')


# ## There is a corrlelation betwee popularity and revenue

# In[38]:


# I will check the correlation between Budget and Revenue


# In[39]:


# input data frame,xlable,ylable,title
corrlation(tmdb_df,'budget','revenue','Budget Vs Revenue')


# In[40]:


# I will check the correlation between Vote_Count and Revenue


# In[41]:


# input data frame,xlable,ylable,title
corrlation(tmdb_df,'vote_count','revenue','Vote Vs Revenue')


# In[42]:


# input data frame,xlable,ylable,title
corrlation(tmdb_df,'rating','revenue','Rating Vs Revenue')


# # We observe that Revenue increases with an increase in Popularity and vote_count 
# # On the other side I observe no correlation between rating and the revenue

# In[43]:


tmdb_df['profit']=tmdb_df['revenue']-tmdb_df['budget']


# In[44]:


tmdb_df.describe().round(2)


# In[45]:


tmdb_df.sample(10)


# In[46]:


sns.pairplot(tmdb_df);


# In[47]:


# input data frame,xlable,ylable,title
corrlation(tmdb_df,'profit','revenue','Profit Vs Revenue')


# In[48]:


tmdb_df.corr()


# In[49]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.


# ### Research Question 2  (Which are movies with the highest profit and lowest profit?
# ### What is the top 10 most profitable movies?)

# In[50]:


# Which are movies with the highest profit and lowest profit?
max_profit = tmdb_df['profit'].max()
tmdb_df.loc[tmdb_df['profit'] == max_profit, 'original_title']


# In[51]:


# Which are movies with the lowest profit ?
min_profit = tmdb_df['profit'].min()
tmdb_df.loc[tmdb_df['profit'] == min_profit, 'original_title']


# In[52]:


# What is the top 10 most profitable movies?


# In[53]:


plt.figure(figsize=(20,10));
ds = tmdb_df[['original_title','profit']].sort_values('profit', ascending=False).head(10)
sns.barplot(x='original_title', y='profit',data=ds,color='Blue')
plt.title('Top 10 most profitable movies',fontsize=25)
plt.xlabel('Original_title',fontsize=15)
plt.ylabel('Revenue',fontsize=15)
plt.xticks(rotation=90)
plt.show();


# ## As we can see, the movie ‘Avatar’, directed by James Cameron, earned the highest profit of all.”
# 

# In[54]:


# Which has been the most popular genres over the years?


# In[55]:


du=tmdb_df.genres.str.get_dummies(sep='|')
du1=du.sum().reset_index()


# In[56]:


plt.figure(figsize=(20,10))
sns.barplot(x=du.columns, y=du.sum(), data=du1)
plt.title('The most popular genres over the years', fontsize=25)
plt.xlabel('genres', fontsize=15)
plt.ylabel('')
plt.xticks(rotation=90)
plt.show()


# ## The most popular movie genres have changed over the years. here drama at first and next comedy, third is thriller and action is the four grade 

# In[ ]:





# <a id='conclusions'></a>
# ## Conclusions
# 
# > Based on the scatter plots, it is evident that there is a direct correlation between Revenue and Popularity. As Popularity increases, so does Revenue also observe no correlation between rating and the revenue
# 
# > According to the bar chart, Drama is the most popular genre, followed by Action, Comedy, and Thriller. These four genres are also the most frequently produced. 
# 
# 
# >During the analysis, I encountered several limitations. The data frame contained numerous rows with null values, which had to be dropped. Additionally, there was a duplicated row (2090) that needed to be removed. After these steps, I re-checked for null values in the key parameters
# > The columns for Directors, genres, and production companies contained values separated by ‘|’. To extract the data, I needed to create a function that could take any column as an argument and keep track of the count while separating the string by ‘|’.
# 
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[ ]:





# In[ ]:





# In[57]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




