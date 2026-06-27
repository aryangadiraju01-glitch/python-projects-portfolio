\# Excel Automation Tool



\## Overview



The Excel Automation Tool is a Python application that automates price calculations for transaction spreadsheets. It reads an Excel workbook, applies a user-defined discount to every product price, generates a new column containing the discounted prices, creates a bar chart, and saves the processed workbook as a new file.



This project was built to practice Python automation, working with Excel files, user input validation, and using third-party Python libraries.



\---



\## Features



\* Processes Excel `.xlsx` workbooks

\* Accepts a user-defined discount percentage

\* Validates Excel file extensions

\* Validates discount percentage input

\* Calculates discounted prices automatically

\* Rounds prices to two decimal places

\* Creates a new \*\*Discounted Prices\*\* column

\* Generates a bar chart from the discounted prices

\* Saves the processed workbook as a new Excel file



\---



\## Technologies Used



\* Python

\* openpyxl



\---



\## Project Structure



```text

Python Excel Automation Tool/

│── main.py

│── transactions.xlsx

└── README.md

```



\---



\## How to Run



1\. Install the required package:



```bash

pip install openpyxl

```



2\. Place your Excel workbook in the project folder.



3\. Run the program:



```bash

python main.py

```



4\. Enter:



&#x20;  \* The Excel workbook name (must be a `.xlsx` file)

&#x20;  \* The desired discount percentage



5\. The program generates a new workbook containing the discounted prices and chart.



\---



\## Skills Demonstrated



\* Python programming

\* Excel automation

\* User input validation

\* File handling

\* Data processing

\* Working with external Python libraries

\* Spreadsheet chart generation



