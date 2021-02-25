import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
import ast

states = open("C:\\Users\\ritan\\Downloads\\usa.states.txt", "r")
print(states.read())

page = requests.get('https://codegolf.stackexchange.com/questions/64254/states-and-capitals')#https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210')
print(page.status_code)
page.content

soup = BeautifulSoup(page.content, 'html.parser')
capitalstate = str(list(soup.find('code').find_next('code').find_next('code')))
print(type(capitalstate))

capitalstatedictstr = capitalstate.replace(',', ':').replace('\\n', ',').replace('[', '').replace(']', '').rstrip("'").rstrip(",").lstrip("'")
print(capitalstatedictstr)

df = pd.DataFrame([x.split(':') for x in capitalstatedictstr.split(',')])
df.columns = ['Capital', 'State']
df = df[['State', 'Capital']]

print(df)
df.to_csv('C:\\Users\\ritan\\Downloads\\usa.states.csv',index=False)

'''capitalstatedata = StringIO("""Capital: State 
    Baton Rouge: Louisiana
    Indianapolis: Indiana 
    """)
df = pd.read_csv(capitalstatedata, sep=":")
print(df)'''
