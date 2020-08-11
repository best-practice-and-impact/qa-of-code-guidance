# Core Programming Practices


## Introduction

The principles outlined in this chapter represent good practices in general programming and software development.

Before reading this chapter, you would benefit from having an understanding of basic programming. Awareness of functions and objects will help you code cleaner. These topics are lightly introduced, but we assume some familiarity with basic programming.

## Motivation 

```{epigraph}
Code is read more often than it is written.

-- Guido van Rossum (creator of Python)
```

You can't be available and responsible for long term maintenance of every piece of code that you write. 
In the future, others will inevitably need to use and adapt your code.
It is important that other programmers can quickly and easily understand the task that your code performs.
Many programs perform a task correctly, but are deemed to be "black boxes" because of the barrier to understanding them.
It is your responsibility to avoid putting this barrier in place.

Good code is easier to document, review and test.
These practices are necessary to make sure that your analysis is reproducible, auditable and assured.
Good code helps you with these ambitions.

This chapter highlights good coding practices that will improve the readability, and therefore maintainability, of your code.
However, if your code is well-tested, documented, and reviewed then you have already reached your goal and don't need to add more complexity to your project.



## Modular code ★☆☆☆☆

Breaking your code down into smaller, more manageable chunks is a sure fire way to improve readability.

Code comes in many shapes and sizes.
A few code abstractions are outlined below, which will be useful for understanding concepts throughout the rest of this chapter and book.

- Functions
    - a unit of code that performs a minimal number of tasks (one ideally)
    - can take inputs and can return outputs, though both are optional
    - used in functional programming


```{figure} ./_static/function.png
---
width: 50%
name: function_fig
---
Visual representation of a function
```

- Objects (often defined by classes)
    - can have associated attributes (variables that belong to the object)
    - can have associated methods (functions that belong to the object)
    - maintain association between data (stored in the object's attributes) and a particular set of tasks (the object's methods)
    - the basis of object-oriented programming (OOP)


```{figure} ./_static/class_pikachu.png
---
width: 70%
name: pikachu_class
---
Demonstration of a Pokémon class, with an example object (instance of the class)
```

- Scripts
    - text documents containing source code
    - may be broken down into sections or "chunks"
    - may contain functions, classes and/or lines of non-modular code

- Packages
    - collections of code that perform related tasks
    - may be sub-sectioned into modules that perform related, but lower level groups of tasks
    - contains other useful information about the code in the package (see Packaging)


## Clean code ★★☆☆☆

```{epigraph}
Programs are meant to be read by humans and only incidentally for computers to execute.

-- Donald Knuth, The Art of Computer Programming
```

Code with high readability is often referred to as "Clean Code".
Clean code helps us to understand the program faster.
Clean code often sounds quite natural when spoken aloud.

(naming)=
### Naming

```{epigraph}
There are only two hard things in Computer Science: cache invalidation and naming things.

-- Phil Karlton
```

The most important aspect of clean code is the naming of identifiers within your code. This includes variables, functions and classes.

Someone reading your code will benefit greatly if you use names that are:

- informative and not misleading
- concise but not cryptic


#### Naming variables

You may have previously come across code that contains variable names that are meaningless, or that infer an incorrect purpose:

````{tabs}

```{code-tab} py
x = "Sioban"

y = 42

z = Car()

my_favourite_number = "ssh, I'm a string"
```

```{code-tab} r
x <- "Sioban"

y <- 42

z <- new(Car)

my_favourite_number <- "ssh, I'm a string"
```

````

Another developer, or even future you, would be unable to correctly understand what you intended these variable names to represent.

Using single letters to name variables may be suitable when they are representing well-known mathematical entities (e.g. $y = mx + c$), but should otherwise be avoided.


```{figure} ./_static/dirty_code_gandalf.png
---
width: 40%
name: gandalf
---
Gandalf regrets writing poor quality code
```


Using variable names that contain a few (3 or so) informative words can drastically improve the readability of your code:


````{tabs}

```{code-tab} py
# Defining variables
first_name = "Sioban"

number_of_attendees = 42

my_car = Car()


# Using variables
print("Hi " + user_name)

number_of_attendees += 1

my_car.clean()
```

```{code-tab} r
# Defining variables
first_name <- "Sioban"

number_of_attendees <- 42

my_car <- new(Car)


# Using variables
print(paste("Hi" + user_name))

number_of_attendees <- number_of_attendees + 1

my_car <- clean(my_car)
```

````


The purpose of these variables is clear from their name alone.
In addition, the variable names make logical sense in the context that are used later on in the code.
This removes the need for explanatory comments, as your intentions can be interpreted from the code itself.

Naming is important for distinguishing between similar variables.
It can be tempting to use a number or character to reflect these differences.
However, these identifiers are not informative.

For instance, in:

````{tabs}

```{code-tab} py
letters_1 = ["a", "b", "c"]
letters_2 = ["x", "y", "z"]
```

```{code-tab} r
letters_1 <- list("a", "b", "c")
letters_2 <- list("x", "y", "z")
```

````

Here we can infer what the lists contain, but it is not apparent what makes `letters_1` different to `letters_2`.

Variable names can be used to document differences between variables, or to incrementally describe changes made to a variable.

````{tabs}

```{code-tab} py
letters_first_three = ["a", "b", "c"]
letters_last_three = ["x", "y", "z"]

letters_first_three_reversed = reversed(first_three_letters)
```

```{code-tab} r
letters_first_three <- list("a", "b", "c")
letters_last_three <- list("x", "y", "z")

letters_first_three_reversed <- rev(first_three_letters)
```

````

Here the naming convention indicates that both lists are similar, but also describes the differences between them.
It is also clear how the third, new list relates to the first list that was used to create it.

Now, you're probably thinking that this could rapidly extend to something like:

```
letters_first_three_reversed_plus_t_minus_a_converted_to_greek
```

You're not wrong, and longer variable names can make it more awkward to use them further down the line.
There is a clear trade-off between the usability and informativeness of variable names.
You'll need to use your best judgement to adapt variable names in order to keep them informative but reasonably concise.


#### Naming functions

When naming functions, you should consider your user's point of view, even if the user is future you.
Your user should be able to infer the purpose or action of the function from the name of the function.
If you can't describe the overall task performed by the function in a few words, then it may be that your function is overly complex.
In this case, you could consider breaking the function down into a number of smaller functions that perform individual tasks.

Where a function performs a specific task, it can be effective to describe this task in the function name, starting with a verb like so:


````{tabs}

```{code-tab} py
def peel_potato(vegetable):
   if vegetable == "potato":
       return "peeled_potato"
   else:
      raise ValueError("That's not a potato!")
      
prepared_potato = peel_potato("potato")
```

````

Sometimes a function might be used to provide a Boolean response to a decision.
In this case, it cam be helpful to name a function as a question that is being posed.


````{tabs}

```{code-tab} py
def is_clean(car):
    if car.cleanliness > 5:
        return True
    else:
        return False

if is_clean(my_car):
    print("Nice!")
```

````

This improves the readability of code that applies these functions, as seen in this example.


#### Naming classes and objects

Class and object names should be concise and descriptive, like variable names.

````{tabs}

```{code-tab} py
class SportsCar(Car):

    def clean(self):
        self.cleanliness = 10
        print("Squeak")

    def drive(self):
        print("VROOOOM!")


my_fast_car = SportsCar()
```

````
(code-style)=
### Code style

When the syntax of a programming language is not strict (as with python and R), it's difficult to know how to "correctly" format  code.
Code style guides provide a standard or convention to work towards, with the intention of increase consistency across a programming community.
Agreed (within a team, for example) style guides might improve your ability to read other peoples code and vice versa.
Guides might include how to appropriately:

- comment or document your code
- separate elements of your code with whitespace
- follow naming conventions

Don't code in fear of breaching style guidance or showing a little flair in your programming style.
Guides cannot account for every possibility and may decrease readability of code in some cases.
In any case, use your best judgement.


```{figure} ./_static/code_quality.png
---
width: 80%
name: code_quality
---
Code Quality, from [xkcd](https://xkcd.com/1513/)
```


Strive to be **consistent** in your style.
Even if another programmer takes a dislike to your use of whitespace or `mixedCase`, as long as you follow a consistent style within a project others will soon get used to it.

```{admonition} Common Style Guides
[PEP8](https://www.python.org/dev/peps/pep-0008/) is an official Python style guide, which is widely used.
The [Google](https://google.github.io/styleguide/Rguide.html) and [tidyverse](https://style.tidyverse.org/) style guides are commonly used for R.
```


#### Checking code style

Manually checking that code complies with a given style is laborious and a waste of your time - programmers like to automate things after all. 
Two main types of tool exist for this task, which automate validation and repair of code style:

- Linters - these analyse your code to flag sylistic errors (and sometimes bugs or security issues too)
- Formatter - these not only detect when you have diverged from a style, but will automatically correct the formatting of your code


```{list-table} Packages that can be used for linting or formatting in Python and R
:header-rows: 1
:name: linters

* - Language
  - Linters
  - Formatters
* - Python
  - `flake8`, `pylint`, `Bandit`
  - `Black`, `Isort`
* - R
  - `lintr`
  - `formatR`, `styler`
```

Be sure to read the documentation for any of these tools, to understand what they are checking/changing in your code.
Some can be configured to ignore or detect specific types of formatting error.
You can run multiple of these, to catch a broader range of stylistic or programmatic errors.

If you're considering these tools as part of a project, see [Continuous Integration](link to continuous integration) for advice on automating them.



## KISS ★★☆☆☆

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


### Don't Repeat Yourself (DRY)

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


### You Ain't Gonna Need It

Try to capture your users needs in the functionality that your software provides.
Developing anything more than this may not be beneficial.
It can be tempting to try to account for every eventuality in your program, or dive down an interesting rabbit hole.
As there's a good chance that many cases that you account for will never occur, you should try to prioritise based and what you're certain is needed from your code.

### Be Explicit

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


## SOLID ★★★☆☆

SOLID is an acronym that encompasses 5 software design principles that are intended to increase the readability and extensibility of software source code.
These principles are designed to improve object-oriented programs, but can be roughly applied to functional programs.

### Single responsibility

> An object should have a single responsibility.
> Only changes to one part of the software's specification should be able to affect the specification of the class.

This principle suggests that a single element of your code (a function or class) should be responsible for a single part of your software's functionality.
It should take on one task and perform it well.

A piece of code is more robust if there are fewer reasons to change it in the future.
Code that is responsible for multiple aspects of your software's functionality might need modifying for several reasons.
Because of this multitasking design, it is also likely to be more difficult to modify this code without having an unintentional effect on other aspects of the software.

Applying this principle reduces the complexity of your code, as the task assigned to each function or class is clearly defined and is independent of other functions or classes.
This simplicity also increases usability, by minimising the number of parameters that each function or class might require.

The Separation of Concerns principle captures a similar concept to Single Responsibility, but on a higher level.
This principle suggests that your software should be separated into distinct sections that each address a single concern.

For example, if your software is responsible for managing sales of a product, then your concerns might include:

- Presenting information to the customer, to allow them to select a product
- Taking payment from the customer
- Arranging dispatch and delivery of the product

Within the section of you software that is responsible for taking payment, you might have multiple responsibilities:

- collect the users input, to capture payment details
- pass the payment information on to a third party, to process the payment
- report the status of the payment to the user


```{figure} ./_static/separation_of_concerns.png
---
width: 80%
name: separation_of_concerns
---
Representation of concerns and responsibilities within a piece of software
```


As such, separate sections of your software should be responsible for each of the concerns.
Within each section of your software, distinct functions or classes should be responsible for each task that is required for that sections overall functionality.

### Open-closed

> Objects and functions should be open for extension, but closed for modification

This means that it should be possible to extend the functionality of classes or functions, without modifying their source code or how they work.
For example, extension of a class or function could be carried out through sub-classing or wrapper functions and decorators, respectively.

This makes managing dependencies much easier between packages and projects.

In functional programming we can use the concepts of function composition and higher-order functions to enact the open-closed principle.

### Liskov substitution

> Objects should be replaceable with instances of their subtypes, without altering the correctness of that program
> Functions should be replaceable with similar functions that observe the same interface contract.

Subclasses should not damage the functionality of their parent class in their implementation.
They should extend their usefulness, but retain their original functionality.

If you were to increase the domain and range of a function to account for new cases then this function should observe the same interface as the previous function.

### Interface segregation

> Many client-specific interfaces are better than one general-purpose interface

As you add more and more functionality into a single interface, it becomes more difficult to extend or maintain. 
Separating these into multiple interfaces increases simplicity and maintainability.


### Dependency inversion

> Depend on abstractions, not concretions

High level modules should not depend on low-level modules. 
Both should depend on interfaces - i.e. be built with this interaction in mind.
Abstractions should not depend on specific details.
Concrete implementations should depend on abstractions.

Specify parameters to a function (or a higher order function to retrieve them) rather than hard coding the function to get some value.
The function should not look outside of its own environment for data.