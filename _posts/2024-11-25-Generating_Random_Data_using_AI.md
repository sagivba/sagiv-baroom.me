---
layout: post
title:  "Generating Random Data for Tables Using LLMs [AI]"
author: "Sagiv Barhoom"
date:   2024-11-25
categories: ORACLE,AI
background: ''
---


# Generating Random Data for Tables Using LLMs [AI]

When testing or developing with databases, random data is often required. 
Beyond generating SQL scripts, we can use AI models like ChatGPT/Claude/CoPilot to produce actual random data.
Then we can then load into your database. 
This approach combines AI’s flexibility with traditional database tools for a powerful data generation workflow.

## Why Use LLM for Data Generation?

LLMs excels at:
- **Generating random yet meaningful data:** Names, emails, dates, etc.
- **Customizable formats:** Tailor data to your table structure.
- **Bulk generation:** Quickly create large datasets.

## Workflow: From LLM like ChatGPT to Oracle Database

### Step 1: Describe Your Table and Data Requirements
Clearly define the structure and type of data you need. For example:
```
> Hi, I have an Oracle table:
> - Table Name: `employees`
> - Columns: `id (number)`, `name (varchar2)`, `email (varchar2)`, `hire_date (date)`, `salary (number)`
```

### Step 2: Ask ChatGPT to Generate Random Data
Request ChatGPT to generate rows of data. For example:
> Generate 200 rows of random data for an `employees` table with the following columns: `id`, `name`, `email`, `hire_date`, `salary`.
> make Sure that names are in Hebrew, Hire date is at least year ago and salary is in the range 10000 to 60000
> Please provide data in a CSV format as file like this:
```csv
id,name,email,hire_date,salary
1,יוסי כהן,yossi@example.com,2022-01-15,5000
2,משה אבוטבול,moshea@example.com,2023-03-20,4500
...
```

### Step 3: Export and Prepare the Data
Save the generated data into a CSV file (`employees_data.csv`).

### Step 4: Load the Data into Oracle
Use Oracle tools like SQL*Loader or an external table to load the data.

#### Example Using SQL*Loader
1. Create a control file (`employees.ctl`):
   ```plaintext
   LOAD DATA
   INFILE 'employees_data.csv'
   INTO TABLE employees
   FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
   (id, name, email, hire_date DATE "YYYY-MM-DD", salary)
   ```

2. Run the SQL*Loader command:
   ```bash
   sqlldr userid=username/password control=employees.ctl
   ```

## Advantages of Using LLM
1. **Dynamic Data Creation:** Generate varied and realistic datasets.
2. **Quick Prototyping:** Produce test data without writing scripts.
3. **Format Flexibility:** Customize data for any schema.

