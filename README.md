# Customers and Orders
- 
## Frontend
- 
## Backend
- 
## Unit Testing and Coverage checking
- Unit testing is done using Django's inbuilt TestCase library together with **pytest**.
- Simple test cases are written for the Customer and Order APIs and run using **coverage**.
    - *coverage run --source='/customers' manage.py test*
- The coverage report is generated using **coverage** library
    - *coverage report*
        ![alt text](image-3.png)
        ![alt text](image-4.png)
    - *coverage html*
        Files: ![alt text](image-5.png)
        Functions:![alt text](image.png) ![alt text](image-1.png)
        Classes: ![alt text](image-2.png) ![alt text](image-6.png)
## CI + Automated CD 