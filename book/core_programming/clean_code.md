# Clean code ★★☆☆☆

```{epigraph}
Programs are meant to be read by humans and only incidentally for computers to execute.

-- Donald Knuth, The Art of Computer Programming
```

Code with high readability is often referred to as "Clean Code".
Clean code helps us to understand the program faster.
Clean code often sounds quite natural when spoken aloud.

(naming)=
## Naming

```{epigraph}
There are only two hard things in Computer Science: cache invalidation and naming things.

-- Phil Karlton
```

The most important aspect of clean code is the naming of identifiers within your code. This includes variables, functions and classes.

Someone reading your code will benefit greatly if you use names that are:

- informative and not misleading
- concise but not cryptic


### Naming variables

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


```{figure} ../_static/dirty_code_gandalf.png
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


### Naming functions

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


### Naming classes and objects

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
## Code style

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


```{figure} ../_static/code_quality.png
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


### Checking code style

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
