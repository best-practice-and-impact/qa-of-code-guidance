# Core programming practices

The principles outlined in this chapter represent good practices for general programming and software development.

However, they are tailored to a more analytical workflow and would benefit analysts with understanding of core programming concepts such as variables, functions and classes. You can find more information and helpful resources in the [resources](resources) section.

## Motivation

```{epigraph}
Code is read more often than it is written.

-- Guido van Rossum (creator of Python)
```

When writing non-trivial code it is wise to assume that at some point someone else will need to understand, use and adapt your code. It might be yourself in six months time - after you've forgotten how the code works, or its design intent. Therefore every time you write such code, it is incredibly important to empathise with these potential users and produce code that is tidy, understandable and does not add unnecessary complexity.

Common barriers to writing readable codebases include documentation that is hard to understand or absent, walls of code with repeating functionality that is hard to absorb in 'chunks' or overcomplicated solutions that solve the problem in ways that could be simplified. Avoiding these issues is essential to make sure that your analysis is reproducible, auditable and assured. Therefore it is our professional responsibility to avoid putting such barriers in place whenever possible.

This chapter highlights some good coding practices that will improve the readability and maintainability of your code.
Here, readability refers how easily another analyst can gain a decent understand of how your code works, within a reasonable amount of time.
Maintainability refers to how easily other analysts can understand your code well enough to modify and repair it.

(modular)=

## Modular code

Breaking your code down into smaller, more manageable chunks is a sensible way to improve readability. Regardless of the language, there are often methods to containerise your code into self-contained parts such as modules, classes or functions.

### Functions

When prototyping we often copy and paste code to 'make things work' but when time comes to wrap that work up, it is worth taking repetitivee code that can be easily parameterised and turning it into functions. Writing functions as well-sealed and reusable containers helps them be easily testable and readable.

When starting to write functions consider what is the right **level of abstraction**. Namely, can this large piece of code be turned into concise and readable function as it is, without having to pass too many arguments to the resulting function? If not, perhaps you need to break the code into smaller helper functions (that can also be reused in other places across the codebase) and then **use these smaller functions to build up a larger function that performs the actions you need**.

This helps you break the complexity down into small and easily comprehendible chunks that can be documented, tested and understood much easier.

Another thing to consider is the idea of `referential transparency`. Without going into that much detail, the core rule of thumb to follow is: **can I take my function and replace it by the value that it would return?**

In practice, this means your functions should try to completely **remove any effects they have on values that you have not explicitly fed into it as arguments**. For instance, adding columns in a lingering data table that is not passed explicitly as an argument. Avoiding such behaviour makes your code more transparent and users can quickly pick out which functions affect what data without being concerned about these hidden behaviours.

In cases where your function alters some external values to that it was not explicitly passed, running that function twice might even produce different results and will make issues harder to debug. Thus, **strive to make sure that running the same function twice with the same inputs produces the same results**.

However this is not always possible or practical in languages that are not designed in a way that encourages this type of programming. Sometimes you **want** a function to capture and affect values outside of the ones provided to it as arguments (i.e. adding data to a database or writing to file). Make sure to control this type of behaviour - ideally pass these values through as parameters to "name and shame" all dependencies and avoid this in the first place - otherwise signal to the end-user to expect these things to happen. This is usually communicated in documentation for end-users and also in comments for fellow developers.

Ultimately, if you do signal where these kind of things might happen, someone trying to debug issues that might be caused by this behaviour will know where to look.

**To summarise**:

- make sure functions are not too overcomplicated; break down the code into even smaller helper functions and build up your functionality with larger functions from these small building blocks
- minimise the 'side-effects' of functions where at all possible in order to make sure that your code is easy to debug and is transparent in its functionality
- similarly, strive to make sure that running your function with the same inputs will produce the same results every time

### Classes

Classes are fundamental parts of object-orientated programming (OOP). And although they exist in R, they are more widely used in Python (and other OOP enabling languages). Hence the following chapter and the examples presented will be less focused on R.

With a more complex system, OOP can help to reduce complexity by hiding low-level details from the developer (which they don't need to know) such as internal `state`.

```{note}
The `state` of an object is usually a set of variables that are particular to a given instance of a class. To illustrate imagine a bank account and a `Account` class. You can have many _instances_ of this class (many unique bank accounts), each defined by the following internal state:
- owner name
- account number
- balance
```

Since the end user, does not need to know all of the state associated with an object, when writing classes consider you to marking such state as `private` and only accessing it from the class `methods` (functions defined with the class).

````{admonition} Method vs Function
When talking about methods software engineers mean functions that are strictly 'attached' to a given class. The following example illustrates the difference between the two:

```python
class Car:
    "A car class"
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

    def diagnose(self):
        ...

# versus

def diagnose(car, ...):
    "A car diagnosis function"
    ...

# calling a method on a class holding the state
cadillac = Car(brand="Cadillac")
cadillac.diagnose()


# calling a function
# note: here for the sake of variety the information about the car is a dictionary
diagnose({"brand":"Cadillac", "wheels":4})

```

````

In some languages private state is in-built in the language while in Python [private instance variables do not exist](https://docs.python.org/3/tutorial/classes.html#private-variables). You can however mark them with underscores and they will be less noticable and mildly harder to accidentally use. You can also add "private" methods as helper methods which aren't exposed to users, to enable reuse of code within an object, analogous to breaking down larger functions.

```python
class BankAccount:
    def __init__(self, balance, credentials):
        self._balance = balance # note: single underscore
        self.__balance = balance # note: double underscore
        # both of these make these values 'private' but the second one also
        # mangles the name of the method

        self.__credentials = credentials

    def __private_withdraw(self, amount):
        "Private withdrawal helper"
        self.__balance -= amount

    def withdraw(self, credentials, amount):
        "Public withdrawal method."
        if check(self.__credentials, credentials):
            self.__private_withdraw(amount)
```

```{note}
The notion of private does not mean secure in Python. The main goal is to _expose less information to the other developers using your class_.
```

Different implementations can be used by the end user - if the classes support the same methods. In Python, this is known as **duck typing** (if it looks like a duck, and quacks like a duck - it must be a duck); here, if a class has the same methods that you require as another class, you can use either class. In the above example, if we created a class `LoyaltyAccount` with the same methods of withdrawing points, we could foreseeably slot that class in instead of the `BankAccount` class.

With other languages `interfaces` are defined to record exactly what a class should supply to be considered equivalent. Perhaps we need a class to store data - it could have several "write" methods; one implementation could deal with storing data into a database, but you also have a variant that stores data in local CSV files instead. In your code, you could switch which class you provide to your functions - the functions don't need to know if they are updating CSV or SQL files, they'll work regardless. Python does not support explicit interfaces by default but we can illustrate the concept in the following example:

```python
# Interface: My Classes Should have these methods:
# write(data: [int]) -> bool
# read(str) -> [int]

class CsvHandler:
    ...
    def write(self, data):
       return write_to_file(data, self.filename)

    def read(self, query):
       data = read_csv(self.filename)
       data = parse(data)
       data = process(query, data)
       return data

class SqlHandler:
    ...
    def write(self, data):
       connect_to_database(self.connection_url)
       return write_to_database(data)

    def read(self, query):
       data = read_from_database(self.connection_url)
       data = process(query, data)
       return data
```

If objects have a similar API (i.e. the methods they supply), then you can easily switch between them; a good real-world example of this is `scikit-learn`, where the different linear model types are represented by different classes that all support a common set of methods. Any model can then be used in a library pipeline and swapped out with minimal effort - they all have methods `fit()` and `predict()`. **Therefore, when thinking about how to break you code up into classes consider the use of standardised methods across similar objects to make them interchangeable.**

(class-responsibilities)=

```{note}
A word of caution, however, when creating classes; it is very easy to start to mapping nouns in system descriptions to classes, and any adjectives applied to the nouns as methods. For example: "the model loads the data" would imply "model" is a class, and it should have a "load_data" method. This will work fine for small systems, but you will find one of your classes gains all of the underlying logic with many methods, whilst other classes just store data with few methods. This can be considered **Data Driven Design**; a better approach is **[Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design)**.

If a single class is responsible for too much, then most of your code will be in one class; it can become overly complex and hence difficult to maintain, and any changes to requirements will cause this one class to change. You need your classes to know as little as possible to reduce dependencies on other systems and requirements - so small classes with a focussed responsibility - and hence avoid being affected if other systems change. The challenge is to trade maintainability and reuse against complexity.
```

**Responsibility Driven Design** makes objects that are normally "passive" become "active" - for example, with a banking system, rather than having an overly complex object representing a bank account (and handling all money movements), instead objects representing "cheques" and "cash" gain payment methods. Hence a cheque knows how to pay itself into an account; if we later needed to add new payment methods, the existing classes will unlikely to be affected. The bank account's responsibility is holding money, receiving it and paying it out. A cheque's responsibility is to pay itself in to a bank account and retrieve money from its associated account.

```{note}
Many **[Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern)** are available with OOP - reusable solutions to common problems. An example is if you have an `Orange` class, and an `OrangePeeler` class. You've been given an `Apple` class, but would really love to be able to peel it - use an **adapter pattern**. Create an `OrangeAdapter` class that has the same methods as an `Orange` but accepts an `Apple` at construction. `OrangeAdapter` then takes all the `Orange` methods and translates them into equivalent method calls to the `Apple` class it was told about at construction. The `Apple` now looks like an `Orange`.

```

Object-Orientated Programming introduces the concept of **inheritance** - where a class can "inherit" its methods from another class. This enables extension of existing classes, but can cause problems for the unwary. Its an in-depth topic, but be aware that inheritance locks you in to the object you inherit from - if this object changes, you are dragged along with it. If you're using inheritance to reuse code from another class, prefer **encapsulation** instead. This means keep a private instance of the class you wish to re-use, and delegate the work down to it within your own methods - rather than inheriting the methods and directly using the other class. Now, if you change your mind about using this reused object - you aren't tied in to it, as no-one outside your class knows you've used it.

Finally, be wary when using classes to "chain" items together; for instance, if a "book" has a "publisher" and the publisher has an "address", you could: `book.publisher().address().postcode()`. However, chains like this are fragile as they depend on multiple parts of the system not changing. The "Demeter" research project found that this style of code produce a high proportion of bugs, resulting in the **(Law of Demeter)[https://en.wikipedia.org/wiki/Law_of_Demeter]**: "Only talk to your immediate friends". Namely, only access the objects you know about directly within a class - delegate the refined knowledge to the class you know about. Your code is then exposed to fewer opportunities to get damaged by a change in the codebase. There is a penalty for this - you replace with `book.publisherPostcode()` which internally would call `publisher.postcode()`, so we've added a method to `publisher` as well as `book`; we're trading maintainability for complexity, so consider if it is worthwhile.

**To summarise**:

- classes hide implementation detail from developers, enabling implementation to be changed without affecting users and reducing visual noise
- look to use consistent methods in a group of related classes to enable switching between them without affecting the code using it (consider Python **duck typing** or other languages' **interfaces**)
- avoid all logic arriving in a single class, surrounded by minimal holding classes - distribute logic around to ease maintenance (changes will affect smaller areas of code)
- be aware of trading maintainability for complexity - too many classes can be hard to understand
- **Design Patterns** have solutions to many common problems and are a useful toolbox - a shared design language
- prefer encapsulation over inheritance, especially with code reuse (see **Liskov Substitution Principle** in the **SOLID** guidance)

### Scripts

Scripts are simply files containing code that you would like to execute. In Python you commonly have a `main.py` script that orchestrates part of your codebase to achieve an outcome. In machine-learning projects, you sometimes have `train.py` and `test.py` which are scripts that train the model and produce performance metrics.

Scripts, if written well, are reproducible. In languages like R and Python, when executed using commands like `python main.py` they are read top to bottom and executed line by line. This is in contrast to other ways of running code such as an interactive interpreter or notebooks, where the human has control of the order of execution allowing for a slew of errors when things are run in the wrong order.

Ultimately for pipelining code and processes you will need to have some way of running your code and the humble script is the primary way of orchestrating your functions and classes in a pipeline fashion.

```{note}
Having something that is not reproducible in a script will not make it more reproducible. The script is simply a tool to run code in the same fashion across multiple runs.
```

**To summarise**:

- scripts are a good way to orchestrate your functions and classes in order to build a simple, yet effective pipeline
- are text documents containing source code which makes them easily human readable and auditable
- may be broken down into sections using comments for readability

(modules)=

### Modules

Simply put, **modules are scripts which house the functions that you want to use in other scripts**. As you write your code and find opportunities to create classes or functions that reduce repetition and promote easier code comprehension, you might eventually decide that you want these functions to sit outside of your `main.py` script and you might decide that they would fit into consistent groupings. This is where modules come in; an example will help comprehend how this might work in practice.

```{note}
We will be using Python for the illustration, however the same principles apply in R.
```

Imagine a project where an analyst has created a massive script in a pipeline and then upon reflection split up their data analysis pipeline into functions relating to `data processing`, `data modelling` and `result presentation`. They might decide they want to have a pipeline script called `main` but they also might want to keep it readable and simple. First they create 3 files: `processing.py`, `modelling.py` and `reporting.py`. Their directory now looks something similar to:

```
project
| main.py
| modelling.py
| processing.py
| reporting.py
| README.md
| LICENSE
```

They then import the relevant functions into `main.py` from their modules as follows:

```python
import pandas as pd

from modelling import predict_results
from processing import clean, preprocess
from reporting import generate_report, export

data = pd.read_csv("data/path.csv")
data = preprocess(clean(data))
results = predict_results(data)
report = generate_report(results)
export(report)
```

```{note}
This is not the de facto example of a main script and it is just to illustrate how you could import from other modules. This `main.py` lacks the ability to configure things like the path to the data from a central configuration file, requiring users to dig around the code and replace paths manually which is highly discouraged.
```

````{admonition} A step further
Another step that can be taken to introduce clarity is to further wrap these modules into their own folder like so:

```
project
| library
  | __init__.py
  | modelling.py
  | processing.py
  | reporting.py
| LICENSE
| main.py
| README.md
```

And the expected python code then can be structured as follows:

```python
import pandas as pd

# Import required modules from functions
from library.modelling import predict_results
from library.processing import clean, preprocess
from library.reporting import generate_report, export

# With some extra work that we will not cover in this section, you reduce it into (Python)
# from library import predict_results, clean, preprocess, generate_report, export

data = pd.read_csv("data/path.csv")
data = preprocess(clean(data))
results = predict_results(data)
report = generate_report(results)
export(report)
```

````

(packages)=

### Packages

Programming languages often ship with quite a few in-built functions and procedures available to the end-users. However, when it comes to solving specialised problems, these in-built functions are often not enough and you will have to build functionality to address a given problem from scratch. If the solutions you build are useful you can then wrap them up in a package and allow other users to install it. They can then reuse the work you have put in within their own code to solve similar problems.

In short, packages are **self-contained collections of code written by someone else to achieve some purpose**. For example, packages like `dplyr` and `pandas` are essential when performing data wrangling and contain a myriad of functions that allows us to avoid rewriting this functionality from scratch every time. Inside these packages is likely to be a set of [modules](modules) containing relevant functions, classes and other code that someone has written and wrapped up in a particular way that the programming language you use can understand, install and make available to you for import.

```{note}
This section will not cover the practices required to package and distribute your code as a package. However if you would like to know more please seek out the packaging guides for your respective language.
```

It is useful to keep in mind the question: **is my code solving a problem that someone else has not provided a solution to in my language?**
If the answer is 'Yes' then perhaps it is worth considering wrapping up your code and distributing it wider.

```{note}
**Packaging code up properly will involve applying a lot of the recommendations from this book.**

You will have to consider how to test, document and lay out your code for it to be usable and packagable. In the end, high quality packages are the cornerstone of open-source package ecosystems, however it is not trivial to be a maintainer and developer of well-regarded open-source packages.

If you feel like you are writing code that you might consider turning into a package, consult this book and strive to apply as many of the recommendations as you go. This will make the final polish and packaging much simpler and will produce packages that are easier for third-parties to trust and use.
```

### Modularised analysis and layout

With all the other guidance in mind, it is worth considering how these tips can be applied in structuring your codebase and enhancing your end-user experience.

In practice throughout exploratory development it is hard to know what the final product will look like, but often the following pattern is sufficiently flexible for final publication:

1.  Explore the data or problem space in either notebooks or scripts
2.  Once results and outputs become clearer, extract the core parts of the experiments into their own set of modules.

    ```{admonition} Example
    After working on a computer vision problem, an analyst notices that acquiring the images from some form of online source is a common function used in many places in the exploratory notebooks.
    <br><br>She then extracts that functionality into the `loaders.py` module of her Python project, documents it, decides to write a simple test for it and imports it back into her notebook to be used down the line.
    ```

3.  Decide what is the appropriate output of this analysis.

    ```{admonition} Example
    The same analyst from the previous example, decides that she is done solving her computer vision problem. The code works in a notebook and she is confident that it is ready to be used as a pipeline. <br><br>She then uses the modules and functions she has built up from her analysis to create a final script that she calls `process.py` that she can configure using a configuration file and re-run as needed to produce required results.

    ```

Ultimately, our example analyst might decide that she wants to guide the user through what is happening in her pipeline, so she might grab a copy of the exploratory notebook she used and adapt it into a step by step explanation (written in Markdown cells) of what the method she developed does alongside the Python code driven examples.

This sort of approach allows for a collection of modules to be testable and easily documentable, allows for a reproducible single script to orchestrate the whole process and also allows for more in-depth and interactive presentations using notebooks or rendered notebooks to the end-user for methods that feel like they need extra explanation.

In short, writing analysis like this is akin to bootstrapping yourself from scratch. You explore what you need to do, write the code to do it, when the code is ready you extract it from your experimental environment into your own [module](modules), test it and document it.

Once you're done, you then use your own code to further your analysis. This one-off cost of refactoring is likely to be absorbed by the time savings of having more robust code during further exploration.

## Notebooks

It is worth touching upon using Jupyter or other kinds of Notebooks that allow running of your code.

Although individual notebooks could seem like a good way to containerise your analysis for distribution, for larger projects this is perhaps not the best idea.

Notebooks are inherently opaque to version control software like `git`. Simple text files like scripts can be version controlled easily as you can see which lines changed from one version to another. Notebooks store their internal workings in a much more complicated form, hence seeing the changes from one notebook to another as differences line by line is not possible in common version control tools.

Furthermore, defining and keeping functions within notebooks is prohibitive to testing. It is not really possible to test individual cells of a notebook with standard external tooling.

Lastly, one of the key issues with notebooks when they are used as methods for running a pipeline is the ability to run cells out of order. In practice this means a user can accidentally execute steps in the wrong order causing issues and different results.

However the great strength of notebooks is their flexibility in displaying results while you are exploring data and their ability to present final research code alongside a narrative written in markdown. Therefore the top 2 reasons to use notebooks in the project lifecycle is to:

- explore and 'play' with the data while developing your methods
- turn notebooks into HTML reports to show end users as a way of reporting

In short, **notebooks are not a great way to modularise your code** however they are a great way to do research analytics and to present results. Therefore as the exploratory part of the analytical project draws to a close or when the notebooks become incredibly large due to function definitions, it is wise to stop and refactor the notebooks. Here are a few suggestions to consider:

- review the repetitive cells and assess which of them can be turned into reusable functions
- extract all the existing function definitions into their own modules
- test, document and further refactor these functions and modules following the guidance laid out in this book
- import the required functionality from the modules you have just made into the notebook
- use the notebook as an orchestrator for the functions you just imported and outline your analytical thinking by mixing clear markdown descriptions and the code as well as its outputs

What you do after this, either turn the notebooks into HTML to send to stakeholders or save them as is so qualified analysts can re-run your notebooks, the steps you've taken will make your code much easier to comprehend and less likely to be bloated.

That said, unless you store only the rendered HTML versions, the notebooks can still be run out of order by some other analysts and **they should not be used as the main method of actually generating outputs**. That orchestration is better placed in scripts that do not have human input as a factor during runtime.

## Clean code

```{epigraph}
Programs are meant to be read by humans and only incidentally for computers to execute.

-- Donald Knuth, The Art of Computer Programming
```

Code with high readability is often referred to as "clean code".
Clean code helps us understand a program faster as it tries to remove points of confusion and ambiguity.

```{admonition} Key Learning
:class: admonition-learning

These concepts are also applied in the [self-led learning course on clean code](https://learninghub.ons.gov.uk/enrol/index.php?id=537) (government analysts only).
```

The following sections will present some key aspects of writing clean code that are fairly widely applicable. That said each individual programming language has idiomatic ways of writing code that are specific to its features and each language usually has some form of accepted style guides for it.

**Make sure to consult the style guides for your language as first point of call.** This is an important point to stress as these guides will capture the most up to date guidance for your language of choice and will usually provide in-depth guidance that is not going to be available in this document.

```{admonition} Be careful!
While reviewing your own or other peoples code it is often tempting to focus on the code style as the first point of call to provide easy feedback. However, the approach of pointing out the deviations between the code and the style guide for the language only addresses the fundamental question - would you say this code is tidy?

What it does not do is ask - does this code do what it needs to and how well is it managing the complexity of the problem?

Always **make sure to not get tunnel vision on clean code as the only source of feedback** for the codebase. Reflect first and foremost on the functionality of the code and how it solves a given problem. Then address the issues that make it less readable.
```

(naming)=

### Naming

The most important aspect of clean code is the naming of identifiers within your code. This includes variables, functions and classes and any other code constructs that can be assigned a name.

Someone reading your code will benefit greatly if you use names that are:

- informative and not misleading
- concise but not cryptic

(naming-variables)=

#### Naming variables

You may have previously come across code that contains variable names that are meaningless, or that imply an incorrect purpose:

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

Another developer, or even "future you", would be unable to correctly understand what you intended these variable names to represent. Therefore **strive to avoid cryptic and single letter identifiers**.

That said, there are situations where some seemingly cryptic identifiers make sense. Using single letters to name variables is suitable when implementing methodologies from underlying mathematical notation.

However, even in these cases one must make sure that the formulas being implemented are clear, readily available to the reader and are consistently reflected in the code throughout the implementation of the mathematical portion. Citing the source o

In other cases, using variable names that contain a few (3 or so) informative words can drastically improve the readability of your code. How these words are separated (be it `CamelCase` or `snake_case`) will depend on your language of choice.

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

Ideally, the **purpose of variables should be clear from just reading their names**.
In addition, the variable names **should make logical sense in the context that they are used later on in the code**. This removes the need for explanatory comments, as your intentions can be interpreted from the code itself - `self-documenting` code.

Naming is important for distinguishing between similar variables. A first instinct might be to assign numerical suffixes or other similar tags to differentiate these variables, however unless the suffix itself is meaningful within the context of the rest of the code, it will not make the code more understandable.

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

With more informative names, we obviously lose the brevity of variable names:

```
letters_first_three_reversed_plus_t_minus_a_converted_to_greek
```

There is a clear trade-off between the usability and informativeness of variable names.
You'll need to use your best judgement to adapt variable names in order to keep them informative but reasonably concise.

```{note}
In a language like Python where indentation is part of the syntax to denote code blocks, you will be much more aware of this trade-off. <br><br>In practice the PEP8 style guide for Python recommends line widths of 79 characters and having overly descriptive names might impact your compliance with a style guide like that.
```

(naming-functions)=

#### Naming functions

Naming functions should respect the best practices already covered in the [Naming variables](naming-variables), however there are a few other points worth raising that are exclusive to function and method names.

Firstly, your user should be able to infer the purpose or action of the function from its name.
If you can't describe the overall task performed by the function in a few words, then it may be that your function is overly complex or it might require further detail in its documentation.

Where a function performs a specific task, it can be effective to describe this task in the function name, starting with a verb:

````{tabs}

```{code-tab} py
def process_text(data):
    ...
text = process_text("The following document was handled using...")
```

```{code-tab} r R
process_text <- function(data) {
    ...
}

text = process_text("The following document was handled using...")
```

````

This is often a nice and tidy way to structure your high-level functions in your pipeline. Well defined, verb based names often lead to clear pipelines such as:

```python
datapath = "path/to/data"

# in short
report_data = generate_report( model( clean( load( datapath ))))

# or, more explicitly
data = load(datapath)
clean_data = clean(data)
model_results = model(clean_data)
report_data = generate_report(model_results)
```

In cases where a function responds with a BOOLEAN (True/False) value, it is often useful to name this function in the form of a question.

````{tabs}

```{code-tab} py
def is_clean(data):
    if mean(data) > 0:
        return True
    else:
        return False
```

```{code-tab} r R
is_clean <- function(data) {
  if (mean(data) > 0){
      TRUE
  } else {
      FALSE
  }
}
```

````

This improves the readability of code that applies these functions.

````{tabs}
```{code-tab} py
if is_clean(data):
   model(data)
```

```{code-tab} r R
if (is_clean(data)) {
    model(data)
}
```
````

#### Naming classes

Class names are usually started with a capital letter, and in `CamelCase`, as this differentiates them from `variableNames` and `variable_names`. The names follow the same advice as for [Naming functions](naming-functions) - namely, is it obvious from the class name what it does? If its too complex to name concisely, it is an indication of too many **(responsibilities)[class-responsibilities]** and you should refactor your design to use more classes that are smaller.

Method names in a class closely follow the requirements for [Naming functions](naming-functions), as methods are just functions that are tied to a class. The method names ideally need to read clearly when called from a class instance - such as `bookParser = TextParser(...some book dataset...)` followed with `bookParser.getNextWord()`. Compare this against `bp = Reader(..some book dataset...)` then `bp.fetch()` - there isn't enough context.

(code-style)=

### Code style

Programming languages can differ in a myriad of ways. One way R and Python differ for example is their use of indentation. Indentation is part of the well defined syntax of Python while it is not in the case of R. This does not mean that you shouldn't use indentation in R to make your code more readable. If in doubt it is often wise to consult how to use formatting to write more readable code by finding the style guidelines for your language.

Generally, code style guides provide a standard or convention for formatting and laying out your code. The purpose of these style guides is to increase consistency across the programming community for a given language.

They might include how to appropriately:

- comment or document your code
- name your functions, variables or classes
- separate elements of your code with whitespace
- use indentation to make sure your code is readable
- other useful guidance regarding formatting

The existence of such style guides does not necessarily mean that each individual or team will apply these conventions when writing their code to the letter. Institutions and developer teams often have needs that might not be addressed in a guidance document aiming to capture the needs of such a diverse group of developers. Therefore, these guides are **more useful as starting points** in a discussion on **'how should our team be consistent internally in the way we write code?'**.

```{figure} ./_static/code_quality.png
---
width: 80%
name: code_quality
alt: Comic strip describing a brutal code review.
---
Code Quality, from [xkcd](https://xkcd.com/1513/)
```

The core idea to remember about these guides is that individual teams have to either adopt them or adapt them and then **use them** while writing code. The goals are **readability and consistency**.
This intra-developer consistency will most likely aid speed of development and review as well as the ability of one developer to comprehend code written by their colleagues.

```{note}
That last point is particularly important when a team member might suddenly become unavailable and the work needs to picked up.
```

Even if others take a dislike to your use of whitespace or `mixedCase`, as long as you follow a consistent style within a project other programmers will soon get used to it.

```{admonition} Common Style Guides
[PEP8](https://www.python.org/dev/peps/pep-0008/) is an official Python style guide, which is widely used.
The [Google](https://google.github.io/styleguide/Rguide.html) and [tidyverse](https://style.tidyverse.org/) style guides are commonly used for R.
```

#### Pythonic and R-esque - idiomatic code

There is perhaps a misconception that following style guidelines and formatting your code accordingly is the fundamental goal of writing good code in a given language.

In reality, not only do the guidelines sometimes force code-reviews to tunnel vision style over more fundamental problems with the code, they also detract from assess whether the code is make the best use of a given language.

We can expand the notion of style to go beyond simple spacing or capitalisation. In the same way that knowing and using common idioms such as 'over the moon' or 'cold feet' make you seem like a more fluent speaker of English, a part of being fluent in a programming language is being able to write idiomatic code. Idiomatic stands for - _using, containing, or denoting expressions that are natural to a native speaker_.

This might mean simplifying complex and perhaps hard to read patterns into a simpler, but well established alternative. In Python for example these two pieces of code are equivalent:

```python
# example 1 - very unpythonic
i = 0
my_data = []
while i < 100:
  my_data += [i * i / 356]
  i += 1

# example 2 - more use of python features such as range and append
my_data = []
for i in range(100):
  my_data.append(i**2 / 356)

# example 3 - making full use pythonic idioms - range * list comprehension
my_data = [i**2 / 356 for i in range(100)]
```

The ability to write idiomatic code in a given language comes with time. However it is important to think about it while looking at a given codebase and the way it is written - is it leveraging everything language `X` has to offer?

```{note}
Prefer readability over using highly complex idioms - think KISS (refer to (Software Ideas for Analysts)[software-ideas-for-analysts] later in this document). Don't obfuscate the meaning behind your code.
```

#### Checking code style

Someone who is able and keen on making sure their code is readable would have hopefully addressed this during the process of writing it; hence codebases that have not had this treatment from the ground up might be difficult to read and will be laborious to check through in detail by hand. Hence, more automated support might be required to speed up such tedious work either by providing suggestions as the code is written or by outright reformatting your work to comply with some style.

Two main types of tool exist for these tasks are known as:

- linter - these analyse your code to flag stylistic errors (and sometimes bugs or security issues too)
- formatter - these not only detect when you have diverged from a style, but will automatically correct the formatting of your code to conform to some predefined style

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

If you're considering these tools as part of a project, see [Continuous Integration](continuous-integration) for advice on automating them or explore other options such as [pre-commits](https://pre-commit.com/) that do the formatting and checking prior to a git commit.

(software-ideas-for-analysts)=

## Software ideas for Analysts

Over many years software engineering teams have followed practices such as KISS (Keep it Simple, Stupid) and SOLID.
These practices allow for more robustly written code and provide other benefits such as easier maintenance of software projects.
Analysts using code as a means to perform analysis could heavily benefit from at least partially applying such practices in their own codebases.

This chapter will try to condense some key messages and guidelines from these practices for use by code writing analysts.
That said, reading and learning more about these practices is likely to benefit the quality of your code and is **highly encouraged**.

### Simplicity

The ability to convey information in simple and clear way matters.

This is particularly true when exchanging information that is already complex.
When writing code you are often trying to solve problems that are complex in nature.
You should **avoid introducing extra complexity** to the problem.
A good guideline to achieve this would be to seek out the simplest solution wherever possible.

More generally here are a few tips to make sure you keep your project nice and simple:

- solve the problem - do not get distracted and make sure you have a clear outcome in mind that you are trying to reach with a given piece of code
- try not to 'reinvent the wheel' - use available packages when they solve the problem, they will most likely be better documented and won't need extra maintenance
- split your code into understandable parts - consider how to lay out your [code into self-contained parts](modular)
- solve the problem without over-engineering - if it is understandable and works, refrain from over-complicating it to make it 5% faster...

It is worth picking up and expanding on that later point around over-engineering.
If your project has potential to be reused as a third party library by someone else or in cases where you have time and resource to add more features to your project
it is often tempting to keep adding more 'bells and whistles' to your code.

However every new 'bell' and every new 'whistle' means you will have to write one more test, one more docstring and it will be one more thing your future self or someone else
will have to read to understand your code.

Really consider if adding these extras in a resource constrained environment will make your code more or less maintainable, user-friendly and correct.
After all, with more to check, there is always more to go wrong.
In other words, make sure to **focus on what needs to be done**, implement that and make sure to keep it simple.

```{note}
**You ain't gonna need it (YAGNI)**

It's important to capture the requirements of your code before writing it.
This includes when your code needs to be adapted to meet changing needs.

You should then aim to meet these requirements in the functionality that your code provides.
Developing anything more than this may not be beneficial.
It can be tempting to try to account for every eventuality in your program.
As there's a good chance that many cases that you account for will never occur, you should try to prioritise based on what you're certain is needed from your code.
```

Lastly it is worth stressing that in the end you are still solving complex problems that might require complex solutions.
In those cases make sure to introduce complexity only where needed and be aware that any complexity you add will be reflected somewhere else (more documentation, more tests etc.). For instance, if the code is execution time critical, then making the code more complex to achieve a faster runtime may be an acceptable trade-off.

### Don't Repeat Yourself (DRY)

As you can see from the section on [modular code](modular), you are encouraged to refactor your code into more self contained components for ease of testing, reproducibility and other nice properties of such code.
However, it is worth stressing that often times 'quick and dirty' solutions involve copy-pasted and tweaked code in several places that is functionaly identical.
This is expected and natural in the initial stages of a project, however repetition not only wastes your time if the code in question keeps getting copied further into the code, but it also makes your code more difficult to read.

Consider a script that contains three copies of a similar piece of code.
If the code that is used to perform the repetitive task is found to be incorrect, or if a developer wishes to modify the task being performed by this code, they must implement a similar change in each of the three copies. If only two copies were spotted and amended, there is now a bug sleeping in the code waiting to be triggered...

Furthermore imagine yourself in a situation where you are reading a codebase you have never seen before.
Having to validate that each similar section of code has the same functionality as the ones you have already seen adds a noticeable mental strain to the reader.

To put this in context, let us use an example where the developer wants to get the odd numbers from three different lists of numbers.

````{tabs}

```{code-tab} py
first_ten_numbers = list(range(1, 11))
second_ten_numbers = list(range(10, 21))
third_ten_numbers = list(range(20, 31))

odd_first = []
for number in first_ten_numbers:
    if number % 2 == 1:
        odd_first.append(number)

odd_second = []
for number in second_ten_numbers:
    if number % 2 == 1:
        odd_second.append(number)

odd_third = []
for number in third_ten_numbers:
    if number % 2 == 0:
        odd_third.append(number)
```

```{code-tab} r R
first_ten_numbers = 1:10
second_ten_numbers = 11:20
third_ten_numbers = 21:30

odd_first <- c()
for (number in first_ten_numbers) {
  if (number %% 2 == 1) {
    odd_first <- c(odd_first, number)
  }
}


odd_second = c()
for (number in second_ten_numbers) {
  if (number %% 2 == 1) {
    odd_second <- c(odd_second, number)
  }
}

odd_third = c()
for (number in third_ten_numbers) {
  if (number %% 2 == 0) {
    odd_third <- c(odd_third, number)
  }
}
```

````

In the example the third repeated snippet of code actually collects the even numbers, but assigns them to the `odd_third` variable.
A developer may assume that all copies of the similar code are performing the same task.
Even if they are aware of the difference, they may be unable to tell if a difference between these copies is intentional or a mistake without explicit comments.
Generally, the example above has several issues, however it shows how **repetition can add to confusion** in circumstances like this.

Modifying multiple copies of a code snippet is laborious and presents a risk - **some copies of the repeated code may be modified while others erroneously remain the same**.
This is analogous to modifying the formula in individual cells of a spreadsheet.
If you refactor repetitive code into functions or classes, then bug fixes or modifications need only be carried out once to change all implementations.
New, intended behaviour is then consistently given by each call of the function or method.

The following presents how one could change the previous example for the better:

````{tabs}

```{code-tab} py
def get_odd(numbers):
    "Get only the odd numbers"
    return [number for number in numbers if number % 2 == 1]

first_ten_numbers = list(range(1, 11))
second_ten_numbers = list(range(20, 21))
third_ten_numbers = list(range(20, 21))

odd_first = get_odd(first_ten_numbers)
odd_second = get_odd(second_ten_numbers)
odd_third = get_odd(third_ten_numbers)
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
second_ten_numbers = 11:20
third_ten_numbers = 21:30

odd_first = get_odd(first_ten_numbers)
odd_second = get_odd(second_ten_numbers)
odd_third = get_odd(third_ten_numbers)
```

````

If the functionality of `get_odd` needs to be modified, it now need only be done once.
Additionally, this code is more concise and its purpose is easier to interpret.

`````{note}
If two slightly different tasks must be carried out, as in you need both the odd and the even numbers, you might approach this in one of two ways:

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
    "Get only the odd numbers"
    return [number for number in numbers if number % 2 == 1]

def get_even(numbers):
    "Get only the even numbers"
    return [number for number in numbers if number % 2 == 0]


# More concise, but also more complex - not always best
def get_numbers_with_parity(numbers, parity):
    if parity not in ["odd", "even"]:
        raise ValueError("parity must be 'odd' or 'even'")
    remainder = 1 if parity == "odd" else 0:
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

`````

It can be difficult to decide when repetition warrants refactoring of code into reusable functions/classes.
The "Rule of Three" suggests that if similar code has been written more than two times, then it is worth extracting its operation to a reproducible procedure like a function or class.
However, consider if you have already written the code twice or are about to write it for the second time, whether it is a piece code you might use a lot in future. If the answer is yes,
turn it into something more modular and reusable.

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
In Python and R, 0 will also evaluate to False.
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

SOLID is an acronym that encompasses five software design principles that are intended to increase the readability and extensibility of software source code.
These principles are designed to improve object-oriented programs, but can be roughly applied to functional programs too.

```{todo}
Extend SOLID subsections with analytical examples.

Not necessarily code-based.

[#21](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/21)
```

### Single responsibility

> An object should have a single responsibility.
> Only changes to one part of the software's specification should be able to affect the specification of the class.

This principle suggests that a single element of your code (a function or class) should be responsible for a single part of your software's functionality. Consider a "responsibility" as an "axis of change" - you want one reason for the code to be changed.
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
They should extend their usefulness, but retain their original functionality. In terms of OOP, if class B inherits from class A, it is said consider "B is an A"; Liskov substitution strengthens this to "B is interchangeable with an A".

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

# Resources

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
