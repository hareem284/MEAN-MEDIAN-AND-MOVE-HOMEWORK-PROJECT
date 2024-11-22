#importing statisctics 
import statistics as st
#importing pandas
import pandas as pd
#reading dataframe
rdf=pd.read_csv('Bestsellers with categories.csv')
print(rdf.info())
rdf.isnull().any()
#
#
meanuserrating=st.mean(rdf['User Rating'])
print("this is the mean of the user rating ", meanuserrating)
#
#
medianuserrating=st.median(rdf['User Rating'])
print("this is the median of the user rating ", medianuserrating)
#
#
modeuserrating=st.mode(rdf['User Rating'])
print("this is the mode of the user rating ", modeuserrating)
#
#
meanprice=st.mean(rdf['Price'])
print("this is the mean of price is ", meanprice)
#
#
medianprice=st.median(rdf['Price'])
print("this is the median of the price is ", medianprice)
#
#
modeprice=st.mode(rdf['Price'])
print("this is the mode of the price is ", modeprice)
#
#
meanReviews=st.mean(rdf['Reviews'])
print("this is the mean of the Reviews are ", meanReviews)
#
#
medianReviews=st.median(rdf['Reviews'])
print("this is the median of the Reviews are ", medianReviews)
#
#
modeReviews=st.mode(rdf['Reviews'])
print("this is the mode of the Reviews are ", modeReviews)