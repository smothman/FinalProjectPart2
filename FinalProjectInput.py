#Sam Othman
#1991756



import pandas as pd 
# Important Libraries that is used to read the csv files and manuplulations



MANF=pd.read_csv("ManufacturerList.csv",header=None)
# Reading the ManufacturerList file




PRCL=pd.read_csv("PriceList.csv",header=None)
## Read the price list file




SDL=pd.read_csv("ServiceDatesList.csv",header=None)
## Read the ServiceDatesList file




MANF.columns=['item ID','manufacturer name', 'item type','optionally a damaged indicator']
## Column names so that we can combine files later




PRCL.columns=['item ID','the item price. ']
## Column names for price lists




SDL.columns=['item ID','servicedate']
## Column names for service dates




COMBINE=pd.merge(pd.merge(MANF,PRCL,on='item ID'),SDL,on='item ID')
## Combining dates based on items ID




COMBINE=COMBINE.sort_values("item type")
## The item attributes must appear in this order.




COMBINE=COMBINE.sort_values("manufacturer name").reset_index(drop=True)
## The items should be sorted alphabetically by manufacturer. 


# In[11]:


COMBINE=COMBINE[['item ID','manufacturer name','item type','the item price. ','servicedate','optionally a damaged indicator']]
## Each row should contain item ID, manufacturer name, item type, price, service date, and list if it is damaged. 


# In[12]:


COMBINE=COMBINE.sort_values("item ID")
## The items should be sorted by their item ID.



COMBINE['servicedate']=pd.to_datetime(COMBINE['servicedate'])
## datetime needed so we can compare with today




COMBINE=COMBINE.sort_values("servicedate")
## The items must appear in the order of service date from oldest to most recent.¶



COMBINE=COMBINE.sort_values("the item price. ",ascending=False)
## . If there is more than one item, provide the most expensive item. 



not_dam=COMBINE[COMBINE['optionally a damaged indicator']!='damaged'] # not damage

## Do not provide items that are past their service date or damaged.



import datetime




not_past=not_dam[not_dam['servicedate']>datetime.datetime.today()] # not past


# ##  Do not provide items that are past their service date or damaged.



not_past['manufacturer name']=not_past['manufacturer name'].str.lower().str.strip()
not_past['item type']=not_past['item type'].str.lower().str.strip()


## taking user input
hereitis=input("Please Enter the item and manufacturer name\n")
userinput=hereitis.lower().split(" ")



ORG_ITEM=not_past[(not_past['manufacturer name'].isin(userinput)) & (not_past['item type'].isin(userinput))].reset_index(drop=True)
## ) if either the manufacturer or the item type are not in the inventory
## gnore any other words, so “nice Apple computer” is treated the same as “Apple computer”. 



another=not_past[(not_past['item type'].isin(userinput))].reset_index(drop=True)
## Also print “You may, also, consider:” and print information about the same item type from another manufacturer that closes in price to the output item


if(len(another)>1):
    another=another[~another['manufacturer name'].isin(userinput)].reset_index(drop=True)



ORG_ITEM['item type'].nunique()




while (hereitis!='q'):
    userinput=hereitis.lower().split(" ")
## ## ) if either the manufacturer or the item type are not in the inventory
## gnore any other words, so “nice Apple computer” is treated the same as “Apple computer”. 
    ORG_ITEM=not_past[(not_past['manufacturer name'].isin(userinput)) & (not_past['item type'].isin(userinput))].reset_index(drop=True)
    another=not_past[(not_past['item type'].isin(userinput))].reset_index(drop=True)
## Also print “You may, also, consider:” and print information about the same item type from another manufacturer that closes in price to the output item
    if(len(another)>1):
        another=another[~another['manufacturer name'].isin(userinput)].reset_index(drop=True)
    ## Print a message(“No such item in inventory”)
    ## the combination is not in the inventory
    if(len(ORG_ITEM)<1): # if either the manufacturer or the item type are not in the inventory
        print("“No such item in inventory”") 
    ## ) if either the manufacturer or the item type are not in the inventory
    elif(ORG_ITEM['item type'].nunique()>1):
        print("“No such item in inventory”")
        print("\nReason Multiple Item")


    ## more than one of either type is submitted

    elif(ORG_ITEM['manufacturer name'].nunique()>1):
        print("“No such item in inventory”")
        print("\nReason Multiple Item")

    else:
    # Print “Your item is:” with the item ID, manufacturer name, item type and price on one line.
        print("\nYour item is. ID",ORG_ITEM['item ID'][0]," Manufacturer ",ORG_ITEM['manufacturer name'][0].title()," item ",ORG_ITEM['item type'][0].title()," Price ",ORG_ITEM['the item price. '][0])
        if(len(another)>0):
    ## ## Also print “You may, also, consider:” and print information about the same item type from another manufacturer that closes in price to the output item
    ## Only print this if the same item from another manufacturer is in the inventory and is not damaged nor past its service date. 

            print("\nYou may, also, consider:",another['item ID'][0]," Manufacturer ",another['manufacturer name'][0].title()," item ",another['item type'][0].title()," Price ",another['the item price. '][0])
    
    hereitis=input("\nPlease Enter the item and manufacturer name\n enter 'q' to quit\n")




