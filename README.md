# Customer Management
- This is a simple application consisting of a Django web REST service and a React frontend
- The application provides a simple dashboard for adding customers and orders. A customer has:
    - a name
    - a phone number
    and an order has:
    - item
    - amount
    - time added
- The order is matched to a specific user, and an SMS is sent to the user's phone number when a matching order has been added.

## Frontend
- The frontend has been built using **ReactJS** using **Vite** and **pnpm** as the node package manager.
- To run the application locally follow the following steps:
    1. Clone the repository - [customer-management](https://github.com/JJFelix/customer-management.git) by running *git clone https://github.com/JJFelix/customer-management.git*
    2. Run *cd customer_management_frontend* to switch to the frontend directory
    3. Run *pnpm install* (Ensure **pnpm** is installed in your local environment) - [Click here](https://pnpm.io/installation) to learn about installing pnpm
    4. Run *pnpm run dev* to start the **Vite** development server
    5. You should see the following page:
    ![alt text](image-8.png)


## Backend
- https://customer-management-api-grx3.onrender.com/api/test?format=json

- Africastalking SMS gateway
![alt text](image-7.png)
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