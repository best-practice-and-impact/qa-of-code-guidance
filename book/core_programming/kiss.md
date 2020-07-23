# KISS ★★☆☆☆

**K**EEP **I**T **S**IMPLE AND **S**TRAIGHTFORWARD

```{epigraph}
Make everything as simple as possible, but not simpler.

-- Albert Einstein, probably
```

The KISS principle applies to all forms of communication, including coding.
You are aiming to communicate a complex series of steps to your reader.
Keeping the overall design of your code simple will improve the clarity of this communication.
Many principles that support good programming practices share this common theme - **simplicity**.

Simple programs are more likely to run, while any bugs in their code will be easier to track down.

While you should strive towards simplicity, this should not compromise the usability of your code.
It should still perform the desired task, just in a way that is no more complex than necessary.


## Don't Repeat Yourself (DRY)

Repetition not only wastes your time, writing redundant lines of code, but it makes code more difficult to read and maintain.
Modular code can be used to tackle repetition.

Consider a script that contains three copies of a similar piece of code.

If the code that is used to perform the repetitive task is found to be incorrect, or if a developer wishes to modify the task being performed by this code, a similar change must be implemented in each of the three copies.


````{tabs}

```{code-tab} py
first_ten_numbers = list(range(1, 11))

odd_first_ten_numbers = []
for number in first_ten_numbers:
    if number % 2 == 1:
    odd_first_ten_numbers.append(number)

second_ten_numbers = list(range(20, 21))
odd_second_ten_numbers = []
for number in second_ten_numbers:
    if number % 2 == 1:
    odd_second_ten_numbers.append(number)

third_ten_numbers = list(range(20, 21))
odd_third_ten_numbers = []
for number in third_ten_numbers:
    if number % 2 == 1:
    odd_third_ten_numbers.append(number)
```

````

Modifying multiple copies of a code snippet is laborious and presents a risk - some copies of the repeated code may be modified while others erroneously remain the same.
A naive user or developer may assume that all copies of the similar code are performing the same task.
Even if they are aware of the difference, they may be unable to tell if a difference between these copies is intentional or a mistake.

**Refactoring** is the process of restructuring code without changing its behaviour.
For example, converting a few lines of code with a common overall task into a function or class.

If you refactor repetitive code into functions or classes then bug fixes or modifications can only be carried out once to change all implementations.
New, intended behaviour is then consistently given by each call to the reusable function or class.
The intended functionality can be reflected by the functions name.

````{tabs}

```{code-tab} py
def get_odd(numbers):
    odd_numbers = []
    for number in first_ten_numbers:
        if number % 2 == 1:
        odd_first_ten_numbers.append(number)
    return odd_numbers

first_ten_numbers = list(range(1, 11))
odd_first_ten_numbers = get_odd(first_ten_numbers)

second_ten_numbers = list(range(20, 21))
odd_second_ten_numbers = get_odd(second_ten_numbers)

third_ten_numbers = list(range(20, 21))
odd_third_ten_numbers = get_odd(third_ten_numbers)
```

````

If the functionality of `get_odd` needs to be modified, it now need only be done once. 
In addition, this code is now more concise and it's purpose is easier to interpret.


If two slightly different tasks must be carried out, you might approach this in one of two ways:

- develop two functions containing the different elements of code, with names that express the difference in their purpose
- add a parameter to your function that will allow a user to differentiate between the two tasks


````{tabs}

```{code-tab} py
# Simple and modular
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

def get_odd(list_of_numbers):
    odd_numbers = []
    for number in list_of_numbers:
        if is_odd(number):
            odd_numbers.append(number)
    return odd_numbers

def get_even(list_of_numbers):
    even_numbers = []
    for number in list_of_numbers:
        if not is_odd(number):
            even_numbers.append(number)
    return even_numbers


# More concise, but also more complex - not always good
def get_numbers_with_parity(list_of_numbers, parity):
    numbers_with_parity = []
    if parity == "odd":
        remainder = 1
    elif parity == "even":
        remainder = 0
    else:
        raise ValueError("parity must be 'odd' or 'even'")
    return [number for number in list_of_numbers if number % 2 == remainder]
```

````

You should use your best judgement to decide which is most appropriate in a given situation.

It can be difficult to decide when repetition warrants refactoring of code into reusable functions/classes.
The "Rule of Three" suggests that if similar code has been written more than two times, then it is worth extracting its operation to a reproducible procedure (i.e. a function or class).


## You Ain't Gonna Need It

Try to capture your users needs in the functionality that your software provides.
Developing anything more than this may not be beneficial.
It can be tempting to try to account for every eventuality in your program, or dive down an interesting rabbit hole.
As there's a good chance that many cases that you account for will never occur, you should try to prioritise based and what you're certain is needed from your code.

## Be Explicit

In the literary sense of the word!

```{epigraph}
Explicit is better than implicit

-- The Zen of Python (`import this`)
```


In some programming languages, it is possible to perform a task or decision by relying on an implied parsing of your code.

To make your intentions clear, you should explicitly state your intentions in the code.

````{tabs}

```{code-tab} py
coconut_count = None

# Relying on falseness of None
if coconut_count:
    print("There are " + coconut_count + " coconuts!")
```

````

In the example above, the coconut count is not printed because None is evaluated to False.
In python and R, 0 will also evaluate to False.
It is unclear whether the programmer intended that the statement is printed when the count is 0.
If a count of 0 should be printed, then this lack of specificity has created a bug.

To perform the same decision explicitly, you could specify the exact condition under which the coconut count should be printed.

````{tabs}

```{code-tab} py
coconut_count = 0

# Explicitly only print if not None
if coconut_count is not None:
    print("There are " + coconut_count + " coconuts!")
```

````
