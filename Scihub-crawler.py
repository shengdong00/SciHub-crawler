import pandas as pd
from selenium import webdriver
import time
import os
import random

# table = pd.read_excel('Full record.xlsx',sheet_name='savedrecs')
table = pd.read_excel('savedrecs.xls')

dois = table['DOI'].copy(deep=True)
for i in dois.index:
    dois[i] = str(dois[i])
finished = [0 for i in range(len(dois))]

auths = table['Authors'].copy(deep=True)
for i in auths.index:
    name = auths[i].split(';')[0]
    auths[i] = name.split(',')[0]

years = table['Publication Year']

def scihub_get(dois, i):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : "D:/Chrome Downloads/Articles"} #NOTE: not working?
    chromeOptions.add_experimental_option("prefs",prefs)
    chrome_driver_path = "D:/Chrome Downloads/chromedriver.exe" #NOTE: where you put your Chrome driver
    wd = webdriver.Chrome(executable_path=chrome_driver_path) #, options=chromeOptions)

    scihub = ['https://sci-hub.ru/', 'https://sci-hub.st/', 'https://sci-hub.se/']  # put different domains of Sci-Hub
    root = scihub[random.randint(0,2)]
    
    # search by doi
    doi = dois[i]
    wd.get(root+doi)
    time.sleep(1)
    
    try:
        b = wd.find_element_by_xpath('//*[@id="buttons"]/button')
        b.click()
        flag = True
        time.sleep(20)
    except:
        print('access failed.    index = '+str(i)+'    doi = '+doi)
        flag = False
        time.sleep(5)
    
    wd.quit()
    return flag

def rename_file(dois, finished, auths, years, i):
    time.sleep(1)
    path = 'C:/Users/Admin/Downloads/'  #NOTE: your path
    dir_list = os.listdir(path)
    if len(dir_list)>0:
        found = 0
        for file in dir_list:
            if file[0:3]!='No_':
                found = 1
                break

        if found==0: #when didn't get the "save" button
            print('download failed.    index = '+str(i)+'    doi = '+dois[i])
        else: #when we get a new file
            l = file.split('.')
            if l[len(l)-1] != "pdf": #when the file was half downloaded
                print('download incomplete.    index = '+str(i)+'    doi = '+dois[i])
            else:
                old = path+ file
                auth = str(auths[i])
                try:
                    year = str(int(years[i]))
                except:
                    year = str(years[i])
                index = [str(i//100), str((i%100)//10), str(i%10)]
                    
                new = path+ 'No_' +index[0]+index[1]+index[2]+'_' +auth+'_'+year+'.pdf'
                os.rename(old, new)
                finished[i] = 1

def article_get(dois, finished, auths, years, i):
    # visit scihub
    if dois[i]=='nan':
        print('doi missing.    index = '+str(i))
    else:
        if scihub_get(dois, i):
            # rename
            rename_file(dois, finished, auths, years, i)
for i in range(0,3): #len(dois)):
    article_get(dois, finished, auths, years, i)

# try a new round for missing articles
path = 'C:/Users/Admin/Downloads/' #NOTE
dir_list = os.listdir(path)
for i in range(0,len(dois)):
    auth = str(auths[i])
    try:
        year = str(int(years[i]))
    except:
        year = str(years[i])
    index = [str(i//100), str((i%100)//10), str(i%10)]
    filename = 'No_' +index[0]+index[1]+index[2]+'_' +auth+'_'+year+'.pdf'
    
    if filename in dir_list:
        continue
    else:    
        article_get(dois, finished, auths, years, i)

# output information of all missing articles
path = 'C:/Users/Admin/Downloads/' #NOTE
dir_list = os.listdir(path)
count = 0
for i in range(0,len(dois)):
    auth = str(auths[i])
    try:
        year = str(int(years[i]))
    except:
        year = str(years[i])
    index = [str(i//100), str((i%100)//10), str(i%10)]
    filename = 'No_' +index[0]+index[1]+index[2]+'_' +auth+'_'+year+'.pdf'
    
    if filename in dir_list:
        continue
    else:    
        print(filename+"    doi: "+dois[i])
        if dois[i]=="nan":
            print("    title: "+table["Article Title"][i])
        count+=1
print(str(count)+" articles missing in total.")
