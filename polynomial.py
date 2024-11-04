from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Function to calculate the matrix X for a polynomial model of degree 2
def create_polynomial_matrix(x_values):
    n = len(x_values)
    X = np.zeros((n, 3))
    X_details = []
    for i in range(n):
        X[i, 0] = 1  # constant term
        X[i, 1] = x_values[i]  # linear term
        X[i, 2] = x_values[i] ** 2  # quadratic term
        X_details.append(f"Row {i+1}: [1, {x_values[i]}, {x_values[i] ** 2}]")
    return X, X_details

# Function to calculate each element of Theta with detailed calculations
def detailed_theta_calculation(matrix, vector):
    result = []
    details = []
    for i in range(matrix.shape[0]):
        sum_ = 0
        element_details = []
        for j in range(matrix.shape[1]):
            product = matrix[i, j] * vector[j]  # no rounding
            sum_ += product
            element_details.append(f"({matrix[i, j]:.6f} * {vector[j]:.6f}) = {product:.6f}")
        result.append(sum_)
        details.append(f"Element a_{i}: " + " + ".join(element_details) + f" = {sum_:.6f}")
    return np.array(result), details

# Function to calculate the product of X^T and Y with details for each multiplication
def detailed_XT_Y_calculation(X_T, Y):
    product_details = []
    product = np.dot(X_T, Y)
    for i in range(X_T.shape[0]):
        element_details = []
        for j in range(X_T.shape[1]):
            element_details.append(f"({X_T[i, j]:.6f} * {Y[j, 0]:.6f})")
        product_details.append(f"Element {i+1}: " + " + ".join(element_details) + f" = {product[i, 0]:.6f}")
    return product, product_details

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Receive dataset values from the HTML form
        x_values = [float(request.form[f"x_{i}"]) for i in range(3)]
        y_values = [float(request.form[f"y_{i}"]) for i in range(3)]

        # Create the X matrix for the polynomial model of degree 2
        X, X_details = create_polynomial_matrix(x_values)
        
        # Calculate the transpose of X and the product X^T * X
        X_T = np.transpose(X)
        X_T_X = np.dot(X_T, X)

        # Check if the determinant is different from zero to decide if we should use the inverse or the pseudoinverse
        det_X_T_X = np.linalg.det(X_T_X)
        if abs(det_X_T_X) > 1e-10:
            # Use the regular inverse
            inverse_X_T_X = np.linalg.inv(X_T_X)
            inverse_method = "Regular Inverse"
        else:
            # Use the pseudoinverse if the determinant is too small
            inverse_X_T_X = np.linalg.pinv(X_T_X)
            inverse_method = "Pseudoinverse"
        
        inverse_details = []
        for i in range(inverse_X_T_X.shape[0]):
            row_details = []
            for j in range(inverse_X_T_X.shape[1]):
                row_details.append(f"{inverse_X_T_X[i, j]:.6f}")
            inverse_details.append(" | ".join(row_details))

        # Calculate X^T * Y with details
        Y = np.array(y_values).reshape(-1, 1)
        X_T_Y, X_T_Y_details = detailed_XT_Y_calculation(X_T, Y)

        # Calculate Theta using the inverse or pseudoinverse
        theta, theta_details = detailed_theta_calculation(inverse_X_T_X, X_T_Y.flatten())

        # Organize results to display in the template
        steps = {
            "X": X,
            "X_details": X_details,
            "X_T": X_T,
            "X_T_X": X_T_X,
            "det_X_T_X": det_X_T_X,
            "inverse_method": inverse_method,
            "inverse_X_T_X": inverse_X_T_X,
            "inverse_details": inverse_details,
            "X_T_Y": X_T_Y,
            "X_T_Y_details": X_T_Y_details,
            "theta": theta,
            "theta_details": theta_details
        }

        return render_template("index.html", steps=steps, x_values=x_values, y_values=y_values)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
