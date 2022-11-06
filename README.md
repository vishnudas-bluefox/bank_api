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
* To run the API server [Have to ensure the default port :8000 was free]
```
cd backend
python3 manage.py runserver
```



### For display the bank_name using id number
_____________
```
http://localhost:8000/api/<bank_id>
```
Eg:
![postman_screenshot](https://raw.githubusercontent.com/vishnudas-bluefox/bank_api/master/Screenshots/bank_name_by_id.png)

### Display all details of bank using IFSC number
______________
```
http://localhost:8000/api/details/ABHY0065001
```
Eg:
![Postman Screenshot](https://raw.githubusercontent.com/vishnudas-bluefox/bank_api/master/Screenshots/details_by_ifsc.png)

### List all the banks and their ID
______________
```
http://localhost:8000/api/list/
```
Eg:
![Postman_Screenshot](https://raw.githubusercontent.com/vishnudas-bluefox/bank_api/master/Screenshots/list_name_and_id.png)
### List all the details from branches table
__________________
```
http://localhost:8000/api/list_all/
```
![Postman Screenshot](https://raw.githubusercontent.com/vishnudas-bluefox/bank_api/master/Screenshots/list_all_details_of_all_banks.png)

### List the complete details of banks using branch name
__________________

```
http://localhost:8000/api/bank_branch/RTGS-HO
```
![Postman_Screenshot](https://raw.githubusercontent.com/vishnudas-bluefox/bank_api/master/Screenshots/list_all_detail_by_branch_name.png)

The project completed by November 6

