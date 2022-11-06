# Bank_api
___________
Simple API can display all the the bank details 

Tools used
* DjangoRestFramework 
* POSTMAN [for testing]
* psql database 


## Guide to build locally
* clone the current repository
```
git clone https://github.com/vishnudas-bluefox/bank_api
```
* get in to the directory
```
cd bank_api
```
* Create and activate a virtualenvironment, for install the dependencies
  [Maybe you have to install venv in system] ``` pip install virtualenv```
```
python3 -m venv venv
source venv/bin/activate
```
* Install the dependencies 
```
pip install -r requirements.txt
```



### For display the bank_name using id number
_____________
```
http://localhost:8000/api/2
```

### Display all details of bank using IFSC number
______________
```
http://localhost:8000/api/details/ABHY0065001
```

### List all the banks and their ID
______________
```
http://localhost:8000/api/list/
```
### List all the details from branches table
__________________
```
http://localhost:8000/api/list_all/
```

### List the complete details of banks using branch name
__________________

```
http://localhost:8000/api/bank_branch/RTGS-HO
```


The project completed by November 6

