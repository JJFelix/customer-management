# Customers and Orders
- 
## Frontend
- 
## Backend
- https://customer-management-api-grx3.onrender.com/api/test?format=json
## Unit Testing and Coverage checking
- Unit testing is done using Django's inbuilt TestCase library together with **pytest**.
- Simple test cases are written for the Customer and Order APIs and run using **coverage**.
    - *coverage run --source='/customers' manage.py test*
- The coverage report is generated using **coverage** library
    - *coverage report*
        ![alt text](image-3.png)
        ![alt text](image-4.png)
    - *coverage html*
        - Files: ![alt text](image-5.png)
        - Functions:![alt text](image.png) ![alt text](image-1.png)
        - Classes: ![alt text](image-2.png) ![alt text](image-6.png)

## CI + Automated CD 
- Continuous Integration has been done using Github actions to automatically run tests and generate coverage reports on every push or pull request.
- Defined in the *.github/workflows/ci.yml* file

- Continuous Deployment has been done using Render, a freemium hosting platform that automatically deploys the application on push or pull request to the connected Github repository. 