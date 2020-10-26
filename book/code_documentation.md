# Code Documentation

```{epigraph}
Documentation is a love letter that you write to your future self.

-- Damian Conway
```


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

```{code-tab} r R
# Set number_1 to 5
number_1 <- 5

# Set number_2 to 9
number_2 <- 9

# Set total to the sum of number_1 and number_2
total <- number_1 + number_2
```

````

Comments that describe exactly **what** is occurring in the code, as above, are often not necessary.
They may be redundant, if [good naming practices](naming) are followed to self-document the steps that occur in your code.
A developer or user can read your code and other more appropriate forms of documentation (see [Docstrings](docstrings) below) for more detailed description of the logic behind your code.
If it is difficult to understand your code without comments, then this can be an indicator that your code is overly complex and might benefit from being refactored into smaller units.

Comments can be used more effectively to explain **why** you might have written code in a certain way.
For example, explaining to other analysts/developers why a section of your code doesn't follow standard practices, perhaps because the typical method didn't work.
This type of comment may help to clarify your choice of logic, without needing to describe the individual steps taken.
Comments explaining **why** you made programming choices will help yourself and other developers to understand your intentions.

```{code-block}
# Tried solution X, but Y worked better because of Z

# Don't use function X here, because of Y

# Temporary work around for bug in function X
# TODO: fix function X, so that Y

# This section of code is commented out because of X
```

Comments can also be used effectively to divide long sections of code into sub-sections that relate to their overall functionality.
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

```{todo}
Add R example
```

But note that in simple cases, such as the example above, these steps may already be apparent from the code.

In summary, use comments sparingly but effectively.


(docstrings)=
## Docstrings ★★☆☆☆

When your code is structured as functions or classes, these functional units can be efficiently documented using docstrings.
Docstrings are multi-line comments that appear at the start of a function definition.
Use of these comments keeps the documentation of your code closely associated with the relevant sections of code.
Docstrings commonly describe:

- what the function or class does
- what parameters the function or class takes as arguments
- what the code returns
- how to use section of code
- references to other functions or classes that carry out similar tasks


````{tabs}

```{code-tab} py
def add_to_each(numbers, add):
    """
    Adds a number to each number in a list.

    Parameters
    ----------
    numbers : list
        Numbers to add `add` to.
    add : int or float
        Number to be added to each element of `numbers`.

    Raises
    ------
    TypeError
        if `numbers` is not a list.

    Returns
    -------
    list
       `numbers` with `add` added to each element.

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
#' Add a number to each element of a vector
#'
#' @param numbers A vector of numbers
#' @param add A float or integer to be added to each element of \code{numbers}
#'
#' @return \code{numbers} with \code{add} added to each element
#'
#' @seealso \code{\link{add}}
#' @examples
#' add_to_each(list(1, 2, 3), 5)
#'
#' @export
add_to_each <- function(numbers, add) {
  if (!(is.vector(numbers) & is.numeric(numbers)) {
    stop("'numbers' must be a numeric vector.")
  }
  numbers + add
}
```

````

In this example, the function docstring starts with a brief description of the overall function.
It then lists the parameters that our function takes, along with the suggested type of each and a brief description.
It also tells us that the function will raise an error if the wrong type is provided for the first parameter.
Then there is a description of the object that is returned from the function, followed by an example of the function in use.
Finally, it references a similar related function.

The Python example follows the [numpydocs style](https://numpydoc.readthedocs.io/en/latest/format.html), which is particularly readable in code files.
While the R example uses the [roxygen2 package](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) and follows the [tidyverse style guide](https://style.tidyverse.org/documentation.html).

You might find that writing function, class or package descriptions prior to writing their code helps you to focus on the task at hand.
The documentation should be a specification of what the code is expected to do.
As documentation tends to be user-focussed, this approach helps you to keep the user's needs in mind when developing code.

Other useful resource include:

- [Python docstring convention](https://www.python.org/dev/peps/pep-0257/)
- Guidance for [documenting objects and functions in R](http://r-pkgs.had.co.nz/man.html)


## Automatic Documentation Generation ★★☆☆☆

Sadly this section does not describe a tool that miraculously writes your documentation for you (though tools for [auto-completing your code](https://kite.com) do exist!).
It does, however, describe tools that automate generation of searchable, user-friendly HTML documentation.
You should ensure that the resulting documentation remains associated with the source code of your project.

Great, so you've embedded documentation into your code, in the form of [docstrings](docstrings).
These docstrings are ideal for technical users looking for a quick understanding of how to use your code.
However, this is not the nicest format to read documentation in and it may require users to navigate the files containing the code to find the relevant documentation.
Thankfully tools are available to extract this information from your code and reproduce it in HTML.


### Generating HTML documentation

For Python, we recommend the [Python package `sphinx`](https://www.sphinx-doc.org/en/master/) for generating HTML documentation.
Sphinx primarily uses the [reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) markup language, but can be extended to also support [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html).
Sphinx supports code highlighting for multiple programming languages within a project, however, other tools may be required to automatically collate documentation from code in languages other than Python.
You can format your documentation using an [existing theme](https://www.writethedocs.org/guide/tools/sphinx-themes/), or design your own.

Many [`sphinx` extensions](https://github.com/yoloseem/awesome-sphinxdoc) are available to add features to your documentation.
For example, the [doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) allows you to run examples that are found within [docstrings](docstrings).
These examples test that your documentation is accurate and up-to-date, but may also flag when your code does not work as expected.

For R projects, you may find [`pkgdown`](https://pkgdown.r-lib.org/) more suitable.
This package will create a HTML references section, containing your code documentation.
It uses your project's README file as a home page for the site and you can add additional content to the site in the form of [vignettes](https://r-pkgs.org/vignettes.html).
The [package's website](https://pkgdown.r-lib.org/) and [it's source code](https://github.com/r-lib/pkgdown/) provide a good demonstration of the package being applied.


### Hosting HTML documentation

Once built, the HTML files containing your documentation can be opened in any browser.
Rather than pass around copies of these files, you may want to host your documentation.

Your version control platform might support hosting documentation in the form of Wiki.
The GitHub platform provides this hosting via [GitHub Pages](https://pages.github.com/).
In many cases, you may be able to automatically update your hosted documentation using [](continuous-integration).

[Read the docs](https://readthedocs.org/) is a community-funded project that provides hosting for open source projects.
