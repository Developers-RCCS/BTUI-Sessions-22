# Demo - Microservices Architecture

Now we look at our Student Management System using a microservices architecture. Here we only split the frontend and backend code.
</br></br>

Run the code below in the main project folder.
1. Create your virtual environment for this project. </br>
`python -m virtualenv .venv`

2. Activate your virtual environment for this project. </br>
`.\.venv\Scripts\activate`

3. Install the necessary packages. </br>
`python -m pip install -r .\requirements.txt`


Run the code below in the backend project folder.
4. Run the backend application. </br>
`python -m uvicorn api:app`

5. Visit the URL displayed on the terminal. </br>
6. Type "/docs" at the end of the URL to visit the API documentation. </br>


Run the code below in the frontend project folder.
7. Run the backend application. </br>
`python -m streamlit run .\app.py`

8. Visit the URL displayed on the terminal. </br>
