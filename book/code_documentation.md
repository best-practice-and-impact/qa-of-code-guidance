# Code Documentation

## Comments ★☆☆☆☆

A common form of documentation is code comments, which are found throughout source code files.

Comments are useful for explaining the logic behind sections of your code.
However, excessive use of code comments often leads to redundancy and can ironically make reading your code more effortful.

````{tabs}

```{code-tab} py
# Set number_1 to 5
number_1 = 5

# Set number_2 to 9
number_2 = 9

# Set total to the sum of number_1 and number_2
total = number_1 + number_2
```

````

Comments that describe exactly **what** is occurring in the code, as above, are often not necessary.
They may be redundant, if [good naming practices](naming) are followed to self-document the steps that occur in your code.
A developer or user can read your code and other more appropriate forms of documentation (see [Docstrings]) for more detailed description of the logic behind your code.
If it is difficult to understand your code without comments, then this can be an indicator that your code is overly complex and might benefit from being refactored into smaller units.

Comments can used more effectively to explain **why** you might have used a particular method.
For example, explaining to other analysts/developers why a section of your code doesn't follow standard practices, perhaps because the typical method didn't work.
This type of comment may help to clarify your choice of logic, without needing to describe the individual steps taken.
Comments explaining **why** you made programming choices will help yourself and other developers to understand your intentions when writing the code.

````{tabs}

```{code-tab} py
# Insert demo of useful comments here


# Works around bug in function X
# TODO: Fix function x!

```

````

Another use of code comments, is to divide long sections of code into sub-sections that relate to their overall functionality.
For example, an analysis script might be broken down into sections that describe each part of the analysis process:

````{tabs}

```{code-tab} py
import pandas as pd
import matplotlib.pyplot as plt


## Get data
time_series = pd.read_csv("time_Series_data.csv")

## Filter data
ten_years = time_series.loc["2010:2020"]
ten_years_price = ten_years.loc[:, "price"]

## Analyse data
median_price = ten_years_price.median()
print("Median price: " + median_price)

## Produce figures
plt.plot(ten_years_price)
```

````

## Docstrings ★★☆☆☆

When your code is structured as functions or classes, these functional units can be efficiently documented using docstrings.
Docstrings are multi-line comments that appear at the start of a function definition.
Use of these comments keeps the documentation of your code closely associated with the relevant sections of code.
Docstrings commonly describe:

- what the function or class does
- what parameters the function or class takes as arguments
- what the code returns
- how to use section of code
- references to other functions or classes carry out similar tasks


````{tabs}

```{code-tab} py
def add_to_each_in_list(numbers, to_add):
    """
    Adds a number to each number in a list.

    Parameters
    ----------
    numbers : list
        Numbers to add `to_add` to.
    to_add : int or float
        Number to be added to each element of `numbers`.

    Raises
    ------
    TypeError
        if `numbers` is not a list.

    Returns
    -------
    new_numbers : list
       `numbers` with `to_add` added to each element.

    Examples
    --------
    >>> my_numbers = [2, 4, 6, 8]
    >>> add_to_each_in_list(my_numbers, 3)
    [5, 7, 9, 11]
    
    See Also
    --------
    add : Adds two numbers 
   """
   if not isinstance(numbers, list):
       raise TypeError("numbers must be a list")
   new_numbers = [number + to_add for number in numbers]
   return new numbers
```

```{code-tab} r R
# Roxygen goes here!
```

````

In this typical example, the docstring starts with a brief description of the overall function.
It then lists the parameters that our function takes, along with the suggested type of each and a brief description.
It also tells us that the function will raise an error if the wrong type is provided for the first parameter.
Then there is a description of the object that is returned from the function, followed by an example of the function in use.
Finally, it references a similar related function.
This example follows the [numpydocs style](https://numpydoc.readthedocs.io/en/latest/format.html), which is particularly readable in code files.

You might find that writing function, class or package descriptions prior to writing their code helps you to focus on the desired task.
As documentation tends to be user-focussed, this approach also helps you to keep the user's needs in mind when developing code.


Other useful resource include:

- [Python docstring convention](https://www.python.org/dev/peps/pep-0257/)
- Guidance for [documenting objects and functions in R](http://r-pkgs.had.co.nz/man.html)

## Automatic Documentation Generation ★★☆☆☆

Sadly this section does not describe a tool that miraculously writes your documentation for you (though tools for [auto-completing your code](https://kite.com) do exist!).
It does, however, describe tools that automate generation of searchable, user-friendly HTML documentation.
You should ensure that the resulting documentation remains associated with the source code of your project.

Great, so you've embedded documentation into your code, in the form of docstrings (above).
These docstrings are ideal for technical users looking for a quick understanding of how to use your code.
However, this is not the nicest format to read documentation in and it may require users to navigate the files containing the code to find the relevant documentation.
Thankfully tools are available to extract this information from your code and reproduce it in HTML.

We recommend the python package [sphinx](https://www.sphinx-doc.org/en/master/) for generating HTML documentation.
Sphinx primarily uses the [reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) markup language.
Sphinx supports code highlighting for multiple programming languages within a project, however, other tools may be required to automatically collate documentation from code for some languages.
You can format your documentation using an [existing theme](https://www.writethedocs.org/guide/tools/sphinx-themes/), or design your own.

In addition to building elegant documentation from your code, these tools can also run examples that are found within docstrings (see example in Docstrings).
These examples test that your documentation is accurate and up-to-date, but may also flag when your code does not work as expected.
In sphinx, python code examples can be tested using the [doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html).

Tools for automatic documentation generation:

- The python package [sphinx](https://www.sphinx-doc.org/en/master/)
- The R package [Roxygen2](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) - generate classic R documentation (.Rd files)
- The R package [pkgdown](https://pkgdown.r-lib.org/articles/pkgdown.html) - generate web-based R documentation, using roxygen-style documentation
- [Natural Docs](https://www.naturaldocs.org/) - open source tool that supports 20 different programming languages
- [Doxygen](http://www.doxygen.nl/)
- [JavaDoc](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html)

Be sure to read the documentation for these tools, as you may need to use a particular docstring style or format that your choice of tool can detect.



