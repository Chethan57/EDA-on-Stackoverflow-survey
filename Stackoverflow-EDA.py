#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[31]:


survey_raw_df=pd.read_csv('survey_results_public.csv')


# In[32]:


survey_raw_df


# In[33]:


survey_raw_df.columns


# In[34]:


schema_df=pd.read_csv('survey_results_schema.csv')


# In[35]:


schema_df


# In[36]:


selected_columns = [
    # Demographics
    'Country',
    'Age',
    'Gender',
    'EdLevel',
    'UndergradMajor',
    # Programming experience
    'Hobbyist',
    'Age1stCode',
    'YearsCode',
    'YearsCodePro',
    'LanguageWorkedWith',
    'LanguageDesireNextYear',
    'NEWLearn',
    'NEWStuck',
    # Employment
    'Employment',
    'DevType',
    'WorkWeekHrs',
    'JobSat',
    'JobFactors',
    'NEWOvertime',
    'NEWEdImpt'
]


# In[37]:


len(selected_columns)


# In[38]:


survey_df=survey_raw_df[selected_columns].copy()


# In[39]:


survey_df


# In[40]:


survey_df.shape


# In[41]:


survey_df.info


# In[42]:


survey_df.describe


# In[43]:


survey_df['Age1stCode']=pd.to_numeric(survey_df.Age1stCode, errors='coerce')
survey_df['YearsCode']=pd.to_numeric(survey_df.YearsCode, errors='coerce')
survey_df['YearsCodePro']=pd.to_numeric(survey_df.YearsCodePro, errors='coerce')


# In[44]:


survey_df


# In[45]:


survey_df.describe()


# In[46]:


(survey_df.Age<10).sum()


# In[47]:


survey_df.drop(survey_df[survey_df.Age< 10].index, inplace=True)
survey_df.drop(survey_df[survey_df.Age> 100].index, inplace=True)


# In[48]:


survey_df


# In[49]:


survey_df.Age.describe()


# In[50]:


survey_df.drop(survey_df[survey_df.WorkWeekHrs > 140].index, inplace=True)


# In[51]:


survey_df.WorkWeekHrs.describe()


# In[52]:


survey_df.Gender.value_counts()


# In[53]:


survey_df.to_csv('survey.csv',index='Fasle')


# In[54]:


import pandas as pd


# In[55]:


survey_df=pd.read_csv('survey.csv')


# In[56]:


survey_df


# In[57]:


survey_df.where(~(survey_df.Gender.str.contains(';', na=False)), np.nan, inplace=True)


# In[58]:


import numpy as np


# In[59]:


survey_df


# In[60]:


survey_df.Gender.value_counts()


# In[61]:


survey_df.sample(10)


# In[62]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[70]:


survey_df.Country.nunique()


# In[64]:


top_countries=survey_df.Country.value_counts().head(15)
top_countries


# In[65]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
sns.barplot(x=top_countries.index,y=top_countries)
plt.show()


# In[66]:


plt.figure(figsize=(12, 6))
plt.xlabel('Age')
plt.ylabel('Number of respondents')

plt.hist(survey_df.Age, bins=np.arange(10,80,5), color='purple');


# In[67]:


gender_counts = survey_df.Gender.value_counts()
gender_counts


# In[68]:


plt.figure(figsize=(12,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=180);


# In[69]:


sns.countplot(y=survey_df.EdLevel)
plt.xticks(rotation=75);
plt.ylabel(None);


# In[71]:


(survey_df.Employment.value_counts(normalize=True, ascending=True)*100).plot(kind='barh', color='g')
plt.xlabel('Percentage');


# #### Q: In which countries do developers work the highest number of hours per week? Consider countries with more than 250 responses only.
# 
# 

# In[73]:


countries_df = survey_df.groupby('Country')[['WorkWeekHrs']].mean().sort_values('WorkWeekHrs', ascending=False)


# In[75]:


high_response_countries_df = countries_df.loc[survey_df.Country.value_counts() > 250].head(15)


# In[76]:


high_response_countries_df


# #### Q: How important is it to start young to build a career in programming?
# 
# 

# In[77]:


sns.scatterplot(x='Age', y='YearsCodePro', hue='Hobbyist', data=survey_df)
plt.xlabel("Age")
plt.ylabel("Years of professional coding experience");


# #### Q.At what Age did you first start to code?

# In[78]:


sns.histplot(x=survey_df.Age1stCode, bins=30, kde=True);


# In[83]:


Languages_desired=survey_df.LanguageDesireNextYear.value_counts()


# In[85]:


Languages_desired1=survey_df.LanguageDesireNextYear.unique()


# In[86]:


Languages_desired1


# In[84]:


Languages_desired


# In[ ]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
sns.barplot(x=Languages_desired.index,y=Languages_desired)
plt.show()

