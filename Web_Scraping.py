import pandas as pd 
import os  
import matplotlib.pyplot as plt

#Import Beautiful Soup
from bs4 import BeautifulSoup
import requests 
import csv
filename="Top500 Supercomputers.csv"
#Open the file in write mode
f=open(filename,"w",newline='')
csv_writer = csv.writer(f,lineterminator='\n')
#Write the headers
csv_writer.writerow(['Rank','Site','Systems','Cores','Rmax','Rpeak','Power'])
pages = [1,2,3,4,5]
for i in pages:
    companynamestring = "https://top500.org/list/2019/06/?page=" + str(i)
    url=requests.get(companynamestring)
    soup = BeautifulSoup(url.content, 'html.parser')
    for record in soup.findAll('tr'):
# Building the record with an empty string
        tbltxt = []
# Adding all table data strings to tbltxt and cleaning it
        for data in record.findAll('td'):
            tbltxt.append(data.text.replace('\n',' '))
        if tbltxt:    
            csv_writer = csv.writer(f)
            csv_writer.writerow(tbltxt)
f.close()


#Read the created Top500 Supercomputers.csv file
supercomputerdata = pd.read_csv("Top500 Supercomputers.csv", sep=",", encoding='mac_roman')
#Convert the objects to float
supercomputerdata['Cores'] = supercomputerdata.Cores.str.replace(',', '').astype(float)
supercomputerdata['Rmax'] = supercomputerdata.Rmax.str.replace(',', '').astype(float)
supercomputerdata['Rpeak'] = supercomputerdata.Rpeak.str.replace(',', '').astype(float)
supercomputerdata['Power'] = supercomputerdata.Power.str.replace(',', '').astype(float)

#Summary Statistics for Cores
supercomputerdata['Cores'].describe()
#Visualisation for Cores
supercomputerdata.hist(column='Cores', bins=20, grid=True, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
                       
#Summary Statistics for Rmax                       
supercomputerdata['Rmax'].describe()
#Visualisation for Rmax
supercomputerdata.hist(column='Rmax', bins=20, grid=True, figsize=(12,8), color='#F08080', zorder=2, rwidth=0.9)
                       
#Summary Statistics for Rpeak                     
supercomputerdata['Rpeak'].describe()
#Visualisation for RPeak
supercomputerdata.hist(column='Rpeak', bins=20, grid=True, figsize=(12,8), color='#66CDAA', zorder=2, rwidth=0.9)
                       
#Summary Statistics for Power 
supercomputerdata['Power'].describe()
#Visualisation for Power
supercomputerdata.hist(column='Power', bins=20, grid=True, figsize=(12,8), color='#708090', zorder=2, rwidth=0.9)

#Scatter plot to determine the relationship between cores and Rpeak                      
plt.scatter(supercomputerdata['Cores'],supercomputerdata['Rpeak'], color='blue')
plt.title('Relationship between Cores and Rpeak', color='black')
plt.xlabel('Cores', color='black')
plt.ylabel('Rpeak', color='black')
plt.show()

#Scatter plot to determine the relationship between cores and Power 
plt.scatter(supercomputerdata['Cores'],supercomputerdata['Power'], color='purple')
plt.title('Relationship between Cores and Power', color='black')
plt.xlabel('Cores', color='black')
plt.ylabel('Power', color='black')
plt.show()