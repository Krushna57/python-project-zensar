# Feedback and Complaints Analysis System
The project involves developing a RESTful API using only python's core libraries without relying on external frameworks. The API facilitates
interaction with a database to perform CRUD operations. The API is tested and verified using postman to ensure its functionality and reliability.

This project is designed to analyze customer feedback and complaints. It provides various functionalities to analyze trends, summarize complaints, and aggregate feedback. The system supports operations like:
- Most common complaints
- Complaint summary by product and region
- Aggregation of feedback by product, rating, and region
- Analysis of feedback trends over time

## Features
- **Complaints Analysis**: 
  - Most common complaints
  - Complaint summary by product
  - Complaint summary by region

- **Feedback Analysis**:
  - Aggregate feedback by product
  - Aggregate feedback by rating
  - Aggregate feedback by region
  - Feedback trends by date

## Technologies Used
- **Python 3.12.7**: The core language used to develop the project.
- **MySQL**: The database used for storing feedback and complaint data.
- **MySQL Connector**: Python library to connect to the MySQL database and execute queries.

## Installation

### Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x: [Download Python](https://www.python.org/downloads/)
- MySQL: [Download MySQL](https://dev.mysql.com/downloads/installer/)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/feedback-complaints-analysis.git
   ```

2. **Install required Python packages**:
   You can install the necessary Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database**:
   - Ensure that you have a MySQL database set up with the appropriate tables (`Feedback`, `Complaints`, etc.).
   - Update the database connection settings in the Python code (e.g., `host`, `port`, `user`, `password`).

4. **Run the application**:
   You can now run the program with the following command:
   ```bash
   python main.py
   ```
## Project Structure
```bash
customer-feedback-analysis/
│
├── models/
│   ├── customer.sql              # SQL file for customer table
│   ├── feedback.sql              # SQL file for feedback table
│   ├── product.sql               # SQL file for product table
│   ├── region.sql                # SQL file for region table
│   └── schema.sql                # SQL file for schema setup
│
├── service/
│   ├── complaints.py             # Complaints analysis functionality
│   └── feedback_analysis.py      # Feedback analysis functionality
│
├── trigger/
│   └── trigger.sql               # SQL file for triggers
│
├── utils/
│   └── DBConnection.py           # Database connection utility
│
├── main.py                       # Main script to run the application
├── requirements.txt              # List of project dependencies
└── README.md                     # Project documentation

```
## Usage

1. When you run the program, you will be presented with a menu-driven interface.
2. You can select an option by entering the corresponding number:
   - `1`: Most Common Complaints
   - `2`: Complaint Summary by Product
   - `3`: Complaint Summary by Region
   - `4`: Aggregate Feedback by Product
   - `5`: Aggregate Feedback by Rating
   - `6`: Aggregate Feedback by Region
   - `7`: Feedback Trends by Date
   - `8`: Exit the system

3. The system will execute the selected function and print the results.

## Example

When you select `1` for "Most Common Complaints," the system will show a list of the most common complaints, including details like the complaint type and count.


## Author
- Name: krushna sahane
- College Name: AVCOE Sangamner
- Departments: Computer Engineering
- Email: krushnasahane57@gmail.com
