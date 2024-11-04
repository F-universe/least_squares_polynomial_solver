Polynomial Model Matrix Calculation
This project provides a web-based tool to calculate the coefficients for a second-degree polynomial model that best fits a given dataset. Through a user-friendly interface, users can input their dataset, and the program will perform matrix calculations to generate the coefficients for a polynomial function that closely represents the provided data points.

Project Overview
The application, built with Flask, includes two main components:

Backend Calculations: Using matrix operations, the program calculates the coefficients that best fit the dataset with a second-degree polynomial model.
Frontend Display: It shows each calculation step in detail on an HTML page, from initial matrix setup to the final results, helping users understand how each value is derived.
Features
Dataset Input: Users enter a small dataset by specifying pairs of x and y values directly on the HTML page.
Matrix Calculations: The program performs a series of matrix operations, including:
Constructing the initial matrix for the polynomial model
Calculating matrix transposition, matrix products, and determining invertibility
Using either the matrix inverse or pseudoinverse to complete the calculations
Detailed Step-by-Step Display: Each matrix calculation step, including products, determinants, and inverses, is displayed in an easy-to-read format on the HTML page.
Coefficient Results: The program presents the final coefficients needed to create the best-fitting polynomial model for the input data.
Usage Instructions
Enter the Dataset: On the main HTML page, input the x and y values for each data point in the dataset.
Submit the Data: Click Calculate to start the matrix calculation process.
Review the Calculations: After submission, the page displays each step, including:
The generated matrix, transposed matrix, and their products
Determinant results and chosen inversion method
The final coefficients that define the polynomial model
Requirements
Python 3.x
Flask
NumPy
Installation
Clone the repository.
Install the required libraries:
bash

pip install flask numpy
Run the application:
bash

python app.py
Open a web browser and go to http://127.0.0.1:5000.
Future Improvements
Higher-Degree Models: Add support for higher-degree polynomial models.
Enhanced Error Handling: Improve handling of non-invertible matrices.
Visualization: Add graphical plots to visually represent the polynomial model alongside the dataset points.
