# Answer for python_test
It runs best with python 3.10. But it would be okay with python 3.6+.

## How to run

### Environment Setup
- Install and activate virtual env
  ```
  pip install virtualenv
  virtualenv env
  ```
  On windows
  ```
  source ./env/Script/activate
  ```
  On mac or unix
  ```
  source ./env/bin/activate
  ```
- Install dependency packages

  `pip install -r requirements.txt`

### Run the solutions
- Run `python solution_1.py` for the solution of the first problem
- Run `python solution_2.py` for the solution of the second problem
- Run `python test_2.py` for testing the solution of the second problem
- Run `python solution_3.py` for the solution of the third problem

## Answers for questions
### 2)
- If you had to generate a large number of rows (millions or more), is there anything you would do differently to handle this? 

  The biggest bottleneck is generating random data. So I make it to generate random data with numpy in advance. And I tried to minimize file operation.
  And if the number of rows is bigger than 10m, I used multi threads.

- If this script had to run in a production environment, what tests would you include to ensure it's running correctly? Add the tests.

  I think it is enough to test the number of rows and columns for the generated file.
  Added test file.

- If you were having this code reviewed, what else would you do with your code to ensure the code is clean and well-formatted?

  When I submit my code for code review, I check these things.
  Coding style, Meaningful names, Unnecessary comments, Readability, well organized structure, Single Responsibility Principle
