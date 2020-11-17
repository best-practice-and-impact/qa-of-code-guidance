# Core programming practices

The principles outlined in this chapter represent good practices for general programming and software development.

However, they are tailored to a more analytical workflow and would benefit analysts with understanding of core programming concepts such as variables, functions and classes. You can find more information and helpful resources in the [resources](resources) section.

## Motivation

```{epigraph}
Code is read more often than it is written.

-- Guido van Rossum (creator of Python)
```

When writing non-trivial code it is wise to assume that at some point someone else will need to understand, use and adapt your code. Therefore everytime you write such code, it is incredibly important to empathise with these potential users and produce code that is tidy, understandable and does not add unecessary complexity.

Common barriers to writing redable codebases include documentation that is hard to understand or absent, walls of code with repeating functionality that is hard to absorb in 'chunks' or overcomplicated solutions that solve the problem in ways that could be simplified. These practices are necessary to make sure that your analysis is reproducible, auditable and assured. Therefore it is our professional responsibility to avoid putting such barriers in place whenever possible.

This chapter highlights some good coding practices that will improve the readability and maintainability of your code.
Here, readability refers how easily another analyst can gain a decent understand of how your code works, within a reasonable amount of time.
While maintainability refers to how easily another analysts can understand your code well enough to modify and repair it.

## Modular code

Breaking your code down into smaller, more manageable chunks is a sensible way to improve readability. Regardless of the language, there are often methods to containerise your code into self-contained parts such as modules, classes or functions.

### Functions

When prototyping we often copy paste code to 'make things work' but when time comes to wrap that work up, it is worth taking repetative code that can be easily parametrised and turning it into functions. Writing functions as well-sealed and reusable containers helps them be easily testable and readible.

When starting to write functions consider what is the right **level of abstraction**. Namely, can this large piece of code be turned into concise and readible function as it is, without having to pass the resulting function too many arguments? If not, perhaps you need to break the code into even smaller helper functions (that can also be reused in other places across the codebase) and then **use these smaller functions to build up a larger function that performs the actions you need**.

This helps you break the complexity down into small and easily comprehendable chunks that can be documented, tested and understood much easier.

Another thing to consider is the idea of `referential transparency`. Without going into that much detail, the core rule of thumb to follow is: **can I take my function and replace it by the value that it would return?**

In practice, this means your functions should try to completely **remove any effects they have on values that you have not explicitly fed into it as parameters**. For instance, adding columns in a lingering data table that is not passed explicitly as a parameter. Avoiding such behaviour makes your code more transparent and users can quickly pick out which functions affect what data without being concerned about these hidden behaviours. In cases where your function alters some external values to that it was not explicitly passed, running that function twice might even produce different results and might make issues harder to debug. Thus, **strive to make sure that running the same function twice with the same inputs produces the same results**.

However this is not always possible or practical in languages that are not designed in a way that encourages this type of programming. And sometimes you **want** a function to capture and affect values outside of the ones provided to it as arguments (adding data to a database or writing to file. Make sure to control this type of behaviour and to signal to the end-user to expect these things to happen. This is usually communicated in documentation for end-users and also in comments for fellow developers. Ultimately, if you do signal where these kind of things might happend, someone trying to debug issues that might be caused by this behaviour will know where to look.

**To summarise**:

- make sure functions are not too overcomplicated and break down the code into even smaller helper functions and build up your functionality and larger functions from these small building blocks
- make sure minimise the 'side-effects' of functions where at all possible in order to make sure that your code is easy to debug and is transparent in its functionality
- similarly, strive to make sure that running your function with the same inputs will produce the same results every time.

### Classes

TODO: IAN

### Scripts:

Scripts are simply files containing code that you would like to execute. In Python you commonly have a `main.py` script that orchestrates part of your codebase to achieve an outcome. In machine-learning projects, you have `train.py` and `test.py` which are scripts that train the model and produce performance metrics.

Scripts, if written well, are reproducible. In languages like R and Python, when executed using commands like `python main.py` they are read top to bottom and executed line by line. This is in contrast to other ways of running code such as an interactive interpreter or notebooks, where the human has control of the order of execution allowing for a slew of errors when things are run in the wrong order.

Ultimately for pipelining code and processes you will need to have some way of running your code and the humble script is the primary way of orchestrating your functions and classes in a pipeline fashion.

```{note}
Having something that is not reproducible in a script will not make it more reproducible. The script is simply a tool to run code in the same fashion across multiple runs.
```

**To summarise**:

- scripts are a good way to orchestrate your functions and classes in order to build a simple, yet effective pipeline
- are text documents containing source code which makes them easily human readible and auditable
- may be broken down into sections using comments for readability

### Modules

### Packages

Programming languages often ship with quite a few in-built functions and procedures available to the end-users. However, when it comes to solving specialised problems, these in-built functions are often not enough and you will have to build functionality to address a given problem from scratch. If the solutions you build are useful you can then wrap it up in a package and allow other users to install it. They can then reuse the work you have put in within their own code to solve similar problems.

In short, packages are _self-contained collections of code written by someone else to achieve some purpose_. For example, packages like `dplyr` and `pandas` are essential when performing data wrangling and contain a myriad of functions that allows us to avoid rewriting this functionality from scratch every time.

This section will not cover the practices required to package up and distribute your code as a package. However if you would like to know more please seek out the packaging guides for your respective language. That said, do keep in mind the question: is my code solving a problem that someone else has not provided a solution in my language? If the answer is 'Yes' then perhaps it is worth considering wrapping up your code and distributing it wider.

```{note}
**Packaging code up properly will involve applying a lot of the recommendations from this book.**

You will have to consider how to test, document and lay out your code for it to be usable and packagable. In the end, high quality packages are the cornerstone of open-source package ecosystems, however it is not trivial to be a maintainer and developer of well-regarded open-source packages.

If you feel like you are writing code that you might consider turning into a package, consult this book and strive to apply as many of the recommendations as you go. This will make the final polish and packaging much simpler and will produce packages that are easier for third-parties to trust and use.
```

### Notebooks

It is worth touching upon using Jupyter or other kinds of Notebooks that allow running of your code.

Although individual notebooks could seem like a good way to containerise your analysis for distribution, for larger projects this is perhaps not the best idea.

Notebooks are inherantly opaque to version control software like `git`. Simple text files like scripts can be version controlled easily as you can see which lines changed from one version to another. Notebooks store their internal workings in a much more complicated form, hence seeing the changes from one notebook to another as differences line by line is not possible in common version control tools.

Furthermore, defining and keeping functions within notebooks is prohibitive to testing. It is not really possible to test individual cells of a notebook with standard external tooling.

However the great strength of notebooks is their flexibility in displaying results while you are exploring data and their ability to present final research code alongside a narrative written in markdown. Therefore the top 2 reasons to use notebooks in the project lifecycle is to:

- explore and 'play' with the data while developing your methods
- turn notebooks into HTML reports to show end users as a way of reporting

TODO: once the data exploration is done

### Modularised analysis

With all the other guidance in mind, it is worth considering how these tips can be applied in structuring your codebase and enhancing your end end-user experience.

In practice throu

## Clean code

```{epigraph}
Programs are meant to be read by humans and only incidentally for computers to execute.

-- Donald Knuth, The Art of Computer Programming
```

Code with high readability is often referred to as "Clean Code".
Clean code helps us to understand a program faster.
The code itself often sounds quite natural when spoken aloud.

```{admonition} Key Learning
:class: admonition-learning

These concepts are also applied in the [self-led learning course on clean code](https://learninghub.ons.gov.uk/enrol/index.php?id=537) (government analysts only).
```

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
import pandas as pd

x = "Sioban"

y = 42

z = pd.DataFrame()

my_favourite_number = "ssh, I'm a string"
```

```{code-tab} r R
x <- "Sioban"

y <- 42

z <- data.frame()

my_favourite_number <- "ssh, I'm a string"
```

````

Another developer, or even "future you", would be unable to correctly understand what you intended these variable names to represent.

Using single letters to name variables is suitable when they are representing well-known mathematical entities (e.g. $y = mx + c$), but you should avoid them in other situations.

```{figure} ./_static/dirty_code_gandalf.png
---
width: 40%
name: gandalf
alt: Gandalf the wizard saying that he can't remember writing this code.
---
Gandalf regrets writing poor quality code
```

Using variable names that contain a few (3 or so) informative words can drastically improve the readability of your code:

````{tabs}

```{code-tab} py
import pandas as pd

# Defining variables
first_name = "Sioban"

number_of_attendees = 42

empty_dataframe = pd.DataFrame()


# Using variables
print("Hi " + first_name)

number_of_attendees += 1

empty_dataframe.empty
```

```{code-tab} r R
# Defining variables
first_name <- "Sioban"

number_of_attendees <- 42

empty_dataframe <- data.frame()


# Using variables
print(paste("Hi" + first_name))

number_of_attendees <- number_of_attendees + 1

plyr::empty(empty_dataframe)
```

````

The purpose of these variables is clear from just reading their names.
In addition, the variable names make logical sense in the context that they are used later on in the code.
This removes the need for explanatory comments, as your intentions can be interpreted from the code itself.

Naming is important for distinguishing between similar variables.
It can be tempting to use a number or character to reflect these differences.
However, this results in identifiers that are not informative.

For instance, in:

````{tabs}

```{code-tab} py
letters_1 = ["a", "b", "c"]
letters_2 = ["x", "y", "z"]
```

```{code-tab} r R
letters_1 <- c("a", "b", "c")
letters_2 <- c("x", "y", "z")
```

````

Here we can infer what these lists and vectors contain, but it is not apparent what makes `letters_1` different to `letters_2`.

Variable names can be used to document differences between variables, or to incrementally describe changes made to a variable.

````{tabs}

```{code-tab} py
letters_first_three = ["a", "b", "c"]
letters_last_three = ["x", "y", "z"]

letters_first_three_reversed = reversed(first_three_letters)
```

```{code-tab} r R
letters_first_three <- c("a", "b", "c")
letters_last_three <- c("x", "y", "z")

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

When naming functions, you should consider a user's point of view.
Your user should be able to infer the purpose or action of the function from its name.
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

```{code-tab} r R
peel_potato <- function(vegetable) {
  if (vegetable == "potato") {
    "peeled_potato"
  } else {
    stop("That's not a potato!")
  }
}

prepared_potato = peel_potato("potato")
```

````

Sometimes a function might be used to provide a Boolean response to a decision.
In this case, it can be helpful to name a function as a question that is being posed.

````{tabs}

```{code-tab} py
def is_clean(cleanliness):
    if cleanliness > 5:
        return True
    else:
        return False

if is_clean(6):
    print("Nice!")
```

```{code-tab} r R
is_clean <- function(cleanliness) {
  if (cleanliness > 5){
      TRUE
  } else {
      FALSE
  }
}

if (is_clean(6)) {
    print("Nice!")
}
```

````

This improves the readability of code that applies these functions, as seen in this example.

#### Naming classes and objects

Class and object names should be concise and descriptive, like variable names.

````{tabs}

```{code-tab} py
class SportsCar(colour):

    def __init__():
        self.colour = colour

    def drive(self):
        print("VROOOOM!")


fast_car = SportsCar("yellow")
fast_car.colour
fast_car.drive()
```

```{code-tab} r R (S3 class)
drive <- function(x) {
  UseMethod("drive", x)
}
drive.SportsCar <- function(x) {
  print("VROOOOOOM!")
}


fast_car <- list(colour = "yellow")
class(fast_car) <- "SportsCar"
fast_car$colour
drive(fast_car)
```

```{code-tab} r R (S4 class)
setClass(
  "SportsCar",
  slots = list(colour = "character")
)
drive <- function(object) {
  print("VROOOOM!")
}
setMethod(
  "drive",
  signature("SportsCar"),
  function(object) {print("VROOOOM!")}
)


fast_car <- new("SportsCar", colour = "yellow")
fast_car@colour
drive(fast_car)
```

````

(code-style)=

### Code style

When the syntax of a programming language is not strict (as with python and R), it can be difficult to know how to "correctly" format code.
Code style guides provide a standard or convention to work towards, with the intention of increase consistency across a programming community.
Agreed style guides (within a team or project) might improve your ability to read other peoples code and vice versa.
Guides might include how to appropriately:

- comment or document your code
- follow naming conventions
- separate elements of your code with whitespace

Don't code in fear of breaching style guidance or showing a little flair in your programming style.
Guides cannot account for every possibility and may decrease readability of code in some cases.
In any case, use your best judgement.

```{figure} ./_static/code_quality.png
---
width: 80%
name: code_quality
alt: Comic strip describing a brutal code review.
---
Code Quality, from [xkcd](https://xkcd.com/1513/)
```

Strive to be **consistent** in your style. This is especially important when working in a coding team where you need to develop code as a group or when you are developing your own code that others might re-use.
Even if others take a dislike to your use of whitespace or `mixedCase`, as long as you follow a consistent style within a project other programmers will soon get used to it.

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

If you're considering these tools as part of a project, see [Continuous Integration](continuous-integration) for advice on automating them.

## KISS <span role="image" aria-label="difficulty rating: 2 out of 5">★★☆☆☆</span>

**K**eep **I**t **S**imple and **S**traightforward

```{epigraph}
Make everything as simple as possible, but not simpler.

-- Albert Einstein, probably
```

The KISS principle applies to all forms of communication, including coding.
You are aiming to communicate a complex series of steps to your reader.
Keeping the overall design of your code simple will improve the clarity of this communication.
Many principles that support good programming practices share this common theme - **simplicity**.

Simple programs are more likely to run. Bugs in the code will be easier to track down.

While you should strive towards simplicity, this should not compromise the usability of your code.
It should still perform the desired task, just in a way that is no more complex than necessary.

### Don't Repeat Yourself (DRY)

Repetition not only wastes your time, writing redundant lines of code, but it makes code more difficult to read and maintain.
You can use modular code to tackle repetition.

Consider a script that contains three copies of a similar piece of code.
If the code that is used to perform the repetitive task is found to be incorrect, or if a developer wishes to modify the task being performed by this code, they must implement a similar change in each of the three copies.
In the example below, we want to get the odd numbers from three different lists of numbers.

````{tabs}

```{code-tab} py
first_ten_numbers = list(range(1, 11))
odd_first_ten_numbers = []
for number in first_ten_numbers:
    if number % 2 == 1:
    odd_first_ten_numbers.append(number)

second_ten_numbers = list(range(10, 21))
odd_second_ten_numbers = []
for number in second_ten_numbers:
    if number % 2 == 1:
    odd_second_ten_numbers.append(number)

third_ten_numbers = list(range(20, 31))
odd_third_ten_numbers = []
for number in third_ten_numbers:
    if number % 2 == 0:
    odd_third_ten_numbers.append(number)
```

```{code-tab} r R
first_ten_numbers = 1:10
odd_first_ten_numbers <- c()
for (number in first_ten_numbers) {
  if (number %% 2 == 1) {
    odd_first_ten_numbers <- c(odd_first_ten_numbers, number)
  }
}


second_ten_numbers = 11:20
odd_second_ten_numbers = c()
for (number in second_ten_numbers) {
  if (number %% 2 == 1) {
    odd_second_ten_numbers <- c(odd_second_ten_numbers, number)
  }
}

third_ten_numbers = 21:30
odd_third_ten_numbers = c()
for (number in third_ten_numbers) {
  if (number %% 2 == 0) {
    odd_third_ten_numbers <- c(odd_third_ten_numbers, number)
  }
}
```

````

In the example the third repeated snippet of code actually collects the even numbers, but assigns them to the `odd_third_ten_numbers` variable.
A naive user or developer may assume that all copies of the similar code are performing the same task.
Even if they are aware of the difference, they may be unable to tell if a difference between these copies is intentional or a mistake.

Modifying multiple copies of a code snippet is laborious and presents a risk - some copies of the repeated code may be modified while others erroneously remain the same.
This is analogous to modifying the formula in individual cells of a spreadsheet.

**Refactoring** is the process of restructuring code without changing its behaviour.
For example, converting a few lines of code with a common overall task into a function or class.

If you refactor repetitive code into functions or classes, then bug fixes or modifications need only be carried out once to change all implementations.
New, intended behaviour is then consistently given by each call to the reusable function or class.
The intended functionality should be reflected in the function name.

````{tabs}

```{code-tab} py
def get_odd(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 == 1:
        odd_numbers.append(number)
    return odd_numbers

first_ten_numbers = list(range(1, 11))
odd_first_ten_numbers = get_odd(first_ten_numbers)

second_ten_numbers = list(range(20, 21))
odd_second_ten_numbers = get_odd(second_ten_numbers)

third_ten_numbers = list(range(20, 21))
odd_third_ten_numbers = get_odd(third_ten_numbers)
```

```{code-tab} r R
get_odd <- function(numbers) {
  odd_numbers = []
  for (number in first_ten_numbers) {
    if (number % 2 == 1) {
      odd_first_ten_numbers.append(number)
    }
  }
  return odd_numbers
}


first_ten_numbers = 1:10
odd_first_ten_numbers = get_odd(first_ten_numbers)

second_ten_numbers = 11:20
odd_second_ten_numbers = get_odd(second_ten_numbers)

third_ten_numbers = 21:30
odd_third_ten_numbers = get_odd(third_ten_numbers)
```

````

Here we've refactored the repetitive code into a function to get odd numbers, called `get_odd`.
If the functionality of `get_odd` needs to be modified, it now need only be done once.
Additionally, this code is more concise and it's purpose is easier to interpret.

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

def get_odd(numbers):
    odd_numbers = []
    for number in numbers:
        if is_odd(number):
            odd_numbers.append(number)
    return odd_numbers

def get_even(numbers):
    even_numbers = []
    for number in numbers:
        if not is_odd(number):
            even_numbers.append(number)
    return even_numbers


# More concise, but also more complex - not always best
def get_numbers_with_parity(numbers, parity):
    if parity == "odd":
        remainder = 1
    elif parity == "even":
        remainder = 0
    else:
        raise ValueError("parity must be 'odd' or 'even'")
    return [number for number in numbers if number % 2 == remainder]
odd_numbers = get_numbers_with_parity(list(range(1, 11), "odd"))
```

```{code-tab} r R
# Simple and modular
is_odd <- function(number) {
  if (number %% 2 == 1) {
    TRUE
  } else {
    FALSE
  }
}

get_odd <- function(numbers) {
  odd_numbers = c()
  for (number in numbers) {
    if (is_odd(number)) {
      odd_numbers = c(odd_numbers, number)
    }
  }
  return(odd_numbers)
}

get_even <- function(numbers) {
  even_numbers = c()
  for (number in numbers) {
    if (!is_odd(number)) {
      even_numbers = c(even_numbers, number)
    }
  }
  return(even_numbers)
}


# More concise, but also more complex - not always best
get_numbers_with_parity <- function(numbers, parity) {
  numbers_with_parity = c()
  if (parity == "odd") {
    remainder = 1
  } else if (parity == "even") {
    remainder = 0
  } else {
    stop("parity must be 'odd' or 'even'")
  }
  numbers[numbers %% 2 == remainder]
}
odd_numbers <- get_numbers_with_parity(1:10, "odd")
```

````

You should use your best judgement to decide which is most appropriate in a given situation.

It can be difficult to decide when repetition warrants refactoring of code into reusable functions/classes.
The "Rule of Three" suggests that if similar code has been written more than two times, then it is worth extracting its operation to a reproducible procedure like a function or class.

### You ain't gonna need it

It's important to capture the requirements of your code before writing it.
This includes when your code needs to be adapted to meet changing needs.

You should then aim to meet these requirements in the functionality that your code provides.
Developing anything more than this may not be beneficial.
It can be tempting to try to account for every eventuality in your program.
As there's a good chance that many cases that you account for will never occur, you should try to prioritise based on what you're certain is needed from your code.

### Be explicit

In the literary sense of the word!

```{epigraph}
Explicit is better than implicit

-- The Zen of Python (`import this`)
```

In some programming languages, it is possible to perform a task or decision by relying on an implied interpretation of your code.
For example, in Python `1`, `100`, `["A list of text"]` and many other objects evaluate to `True`, while `0`, `[]` and `None` evaluate to `False`.

To make your intentions clear, you should explicitly state your intended comparison in the code.

````{tabs}

```{code-tab} py
coconut_count = None

# Relying on falseness of None
if coconut_count:
    print("There are " + coconut_count + " coconuts!")
```

```{code-tab} r R
coconut_count <- FALSE

# Relying on falseness of FALSE
if (coconut_count) {
  print("There are " + coconut_count + " coconuts!")
}
```

````

In the example above, the coconut count is not printed because `None` and `FALSE` evaluate to false.
In python and R, 0 will also evaluate to False.
Therefore, it is unclear whether the programmer intended that the statement is printed when the count is 0.
If a count of 0 should be printed, then this lack of specificity has created a bug.

To perform the same decision explicitly, we should specify the exact condition under which the coconut count should be printed.

````{tabs}

```{code-tab} py
coconut_count = 0

# Explicitly print only if more than 0
if coconut_count >= 0:
    print("There are " + coconut_count + " coconuts!")
```

```{code-tab} r R
coconut_count = 0

# Explicitly only print if more than 0
if (coconut_count >= 0) {
  print("There are " + coconut_count + " coconuts!")
}
```

````

Now the count is printed if it is more than or equal to 0.
It's clear that we intend for this to be the case.

## SOLID <span role="image" aria-label="difficulty rating: 4 out of 5">★★★★☆</span>

SOLID is an acronym that encompasses 5 software design principles that are intended to increase the readability and extensibility of software source code.
These principles are designed to improve object-oriented programs, but can be roughly applied to functional programs too.

```{todo}
Extend SOLID subsections with analytical examples.

Not necessarily code-based.

[#21](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/21)
```

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

- Presenting information to the customer, to allow them to select a product.
- Taking payment from the customer.
- Arranging dispatch and delivery of the product.

Within the section of you software that is responsible for taking payment, you might have multiple responsibilities:

- Collect the users input, to capture payment details.
- Pass the payment information on to a third party, to process the payment.
- Report the status of the payment to the user.

```{figure} ./_static/separation_of_concerns.png
---
width: 80%
name: separation_of_concerns
alt: Representation of concerns and responsibilities within a piece of software.
---
Representation of concerns and responsibilities within a piece of software
```

As such, separate sections of your software should be responsible for each of the concerns.
Within each section of your software, distinct functions or classes should be responsible for each task that is required for that sections overall functionality.

### Open-closed

> Objects and functions should be open for extension, but closed for modification.

This means that it should be possible to extend the functionality of classes or functions, without modifying their source code or how they work.
For example, extension of a class or function could be carried out through sub-classing or wrapper functions and decorators, respectively.

This makes managing dependencies much easier between packages and projects.

In functional programming we can use the concepts of function composition and higher-order functions to enact the open-closed principle.

### [Liskov substitution](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> Objects should be replaceable with instances of their subtypes, without altering the correctness of that program
> Functions should be replaceable with similar functions that observe the same interface contract.

Subclasses should not damage the functionality of their parent class in their implementation.
They should extend their usefulness, but retain their original functionality.

If you were to increase the domain and range of a function to account for new cases then this function should observe the same interface as the previous function.

### Interface segregation

> Many client-specific interfaces are better than one general-purpose interface.

An interface describes the interaction between multiple elements of code.
This might be a piece of your code that uses another piece of your code or someone else's.

As you add more and more functionality into a single interface, between parts of a program or from the program to customers, it becomes more difficult to extend or maintain.
Separating these into multiple interfaces increases simplicity and maintainability.

It can be tempting to generalise your program to as many use cases as possible.
However, this can overwhelm your users.
It is better that each user persona gets an interface that is meant for them rather than a complicated one which doesn't satisfy any user persona.

### Dependency inversion

> Depend on abstractions, not concretions.

High level modules should not depend on low-level modules.
Both should depend on interfaces - i.e. be built with this interaction in mind.

Abstractions should not depend on specific details, but should outline a general concept.
Concrete implementations should depend on these abstractions.

Specify parameters to a function (or a higher order function to retrieve them) rather than hard coding the function to get some value.
The function should not look outside of its own environment for data.

(resources)=

# Resoures

This section contains a few resources that might help understanding the concepts and guidance presented in this section.

```{admonition} Pre-requisites
:class: admonition-learning

You should look to these sources for introductory learning, before reading this guidance:
* Introduction to [Python](https://learninghub.ons.gov.uk/enrol/index.php?id=536) and [R](https://learninghub.ons.gov.uk/enrol/index.php?id=538) (government analysts only)
* Aggregation, functions and control flow in [Python](https://learninghub.ons.gov.uk/enrol/index.php?id=525) and [R](https://learninghub.ons.gov.uk/enrol/index.php?id=527) (government analysts only)
* Official Python [Getting Started Guide](https://www.python.org/about/gettingstarted/)
* [Learn Python](https://www.learnpython.org/) supported by DataCamp
* [R Basics](https://www.udemy.com/course/r-basics/?LSNPUBID=JVFxdTr9V80&ranEAID=JVFxdTr9V80&ranMID=39197&ranSiteID=JVFxdTr9V80-mzkL.lpta.ugiFro.8Oc_Q&utm_medium=udemyads&utm_source=aff-campaign) on Udemy
* [edx](https://www.edx.org/) and [freeCodeCamp](https://www.freecodecamp.org/) hosts many free online coding courses
* [DataCamp](https://www.datacamp.com/), [Codecademy](https://www.codecademy.com/) and [Coursera](https://www.coursera.org/) host a range of introductory courses, but more advanced courses are often not free.

Please note that non-government analysis learning may not follow good practices. However, exposure to a range of applied examples will still benefit your learning.
You should compare and contrast your learning to the good practices outlined in this section.
```

```{admonition} Further Learning
:class: admonition-learning

These resources cover more advanced topics, which are not essential for for this section:
* Dataframes, manipulation and cleaning in [Python](https://learninghub.ons.gov.uk/enrol/index.php?id=521) and [R](https://learninghub.ons.gov.uk/enrol/index.php?id=523) (government analysts only)
* [Introduction to Unit Testing](https://learninghub.ons.gov.uk/enrol/index.php?id=539) and other code quality assurance for Python and R (government analysts only)
* Python [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)
* [Python for Data Analysis](https://github.com/wesm/pydata-book)
* [R for Data Science](https://r4ds.had.co.nz/)
* [Advanced R](https://adv-r.hadley.nz/index.html)
* Harvard University's courses on [Python](https://online-learning.harvard.edu/subject/python) and [R](https://online-learning.harvard.edu/subject/r)
```
