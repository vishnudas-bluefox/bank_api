# Bank_api
___________
Simple API can display all the the bank details 

Tools used
* DjangoRestFramework 
* POSTMAN [for testing]
* psql database 


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

