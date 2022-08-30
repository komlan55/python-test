# Descripton

Take your time implementing code that you are proud of. Quality over quantity.

# 1. Write some code, that will flatten an array of arbitrarily nested arrays containing some values into a flat array of all the values non-empty

In this exercise, test-all and flatten was added but are not complete. Flatten is to be used as a util file for a higher level of implementation, but the function to call is not implemented.
test-all.py will be used as your main to run, test and output.

Implement the flatten function (code/doc/tests) as you will do before sending it as a PR. Examples are provided in the test-all.py file.

# 2. Write Tracker class models

In this exercise, you need to implement class models. We want to have a Generic tracker class and a Temperature tracker class which will inherit from the Generic.

Generic tracker will need to have a 'insert' and 'mean' function to be used by any type of tracker.
Temperature tracker will have its own specific function such as "min" and "max".

In the test-all.py file, simply use your trackers. Examples are provided. 


# Developper section

### Personal additional changes

* Overall
  * I added pytest for the test, I think it's going to be easier. I took the exemple from test_all.py as test data
* TemperatureTracker
  * For the insertion of integer items, I overrode the insert function to handle the exception in case of non integer

### Setup
```
# once inside of the project

# activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# install libraries
pip3 install -r requirements 

# Run tests
pytest 
```