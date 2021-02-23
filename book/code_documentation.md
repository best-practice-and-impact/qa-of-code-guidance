# Code documentation

```{epigraph}
Documentation is a love letter that you write to your future self.

-- Damian Conway
```

## Comments

> Use comments sparingly and with purpose

Comments are lines of text in source code files that typically aren't executed as part of the program. They are small notes or annotations written by those working on the code. Often, they provide context or explain the reasoning behind implementation decisions.

Comments are essential to help those working on the code in the future to understand any non-obvious details around how and why the code has been written in a particular way. As such, when it comes to providing relevant and perhaps higher-level documentation to the end consumer on the functionality of your code, there are much more appropriate solutions such as [docstrings](docstrings).

Although extremely useful, comments should be used sparingly. Excessive use of code comments often leads to redundancy and can, ironically, make your code harder to read. It is easy for comments to not be updated as changes are made to the code. Outdated, or irrelevant comments can confuse or mislead.

```{note}
**Remember**: the only point of 'truth' is the code that is executed - if the comments are out of date compared to the actual code, it may not be immediately apparent.
```

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

Comments that describe exactly **what** is occurring in the code, as above, are often not necessary. They may be redundant, if [good naming practices](naming) are followed to self-document the steps that occur in your code. For a more detailed description of **what** the code does, the developer can also read more appropriate forms of documentation (see [docstrings](docstrings) below).

If it is difficult to understand your code without comments, this can indicate that your code is overly complex and might benefit from being broken down, or 'refactored', into smaller units. That said, sometimes you will be faced with functions and classes that are complex for a reason. Stopping to reflect on why your documentation is so large is a good prompt to consider whether refactoring is in order.

````{note}
```{epigraph}
Simple is better than complex.
Complex is better than complicated.

-- Zen of Python
```
For complex methodologies, it is hard to completely eliminate complexity and it will eventually have to 'sit' somewhere. This is natural, as real-world problems can be complex. The key is to manage that complexity without adding to it.
````

Comments can be used more effectively to explain **why** you might have written code in a certain way. For example, you might explain to other analysts and developers why a section of your code doesn't follow standard practices, perhaps because the typical method didn't work. This type of comment can help to clarify your decision-making process, without needing to describe the individual steps taken.

In short, comments explaining **why** you made programming choices will help your future self and other developers to understand your intentions.

```{code-block}
# Tried solution X, but Y worked better because of Z

# Don't use function X here, because of Y

# Temporary work around for bug in function X
# TODO: fix function X, so that Y

# This section of code is commented out because of X
```

Comments are sometimes used to divide long sections of code into sub-sections that relate to their overall functionality. That said, the merit of doing so will depend on the value added. For example, the code below is already fairly self-documenting and therefore adding the section headings does not add much value.

````{tabs}

```{code-tab} py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## Get data
penguins = sns.load_dataset("penguins")

## Analyse
species_means = penguins.groupby("species").mean()

## Report
plt.plot(penguins.bill_length_mm)
species_means.to_csv("penguin_species_mean_measurements.csv")
```
```{code-tab} r R
library(palmerpenguins)
library(magrittr)


## Get data
penguins_data <- penguins

## Analyse
species_means <- penguins_data %>%
  dplyr::group_by(species) %>%
  dplyr::summarize(dplyr::across(where(is.numeric), mean, na.rm = TRUE))

## Report
plot(penguins_data$bill_length_mm)
write.csv(species_means, "penguin_species_mean_measurements.csv")
```

````

Leaving unused code in your scripts makes them more difficult to read and understand, as they add visual noise to anyone trying to understand your code at pace. Furthermore, relying on someone to comment and uncomment things to alter the functionality of the code is **highly discouraged**. Doing so reduces the reproducibility of your analysis.

````{tabs}

```{code-tab} py
print("Run me!")
# print("Don't run me...")
```
```{code-tab} r R
print("Run me!")
# print("Don't run me...")
```

````

It is easy to forget which parts of code have been commented out and why they have been commented. It introduces a human factor into the equation, which might not be accounted for if someone in the future is not aware of the commented-out code. This is likely to produce inconsistent runs of the same piece of code. This code might quickly become out of sync with the rest of the changes in the codebase, as developers may not consider updating code that is commented out if they assume it is obsolete.

You should instead use appropriate control flow (such as `if/else` statements) to determine when these sections should be run. When changes are required between individual runs of your analysis, you should consider [defining these options in a dedicated configuration file](configuration.md).


In summary, you should use comments sparingly but purposefully. Make sure comments:

- explain **why** certain things are done, in order to provide context around the decisions that you have made
- do not echo what your code is already telling the reader
- are accurate and still relevant after code changes

(docstrings)=
## Docstrings

When your code is structured as functions or classes, these functional units can be efficiently documented using docstrings. Docstrings are specialised multi-line descriptions that appear at the start of a function definition and are the de facto way of documenting these individual components. In practice they can be either strings (as in Python docstrings) or comments (as in R). Note that module or script level docstrings are also commonly used (usually at the top of the module file in the case of Python). Use of docstrings keeps the documentation of your code closely associated with the relevant sections of code. This close association means it is easier to keep documentation up to date as changes are introduced to the code.

An end-user can access these docstrings by typing `help(function_name)` after they have imported your library, so they are handily available without needing to have the source code files open in another window. Other tools, like Jupyter for Python, allow users to easily access these docstrings for quick reference. Hence the focus on detail and comprehensiveness is key - this is the first point of call for an end-user trying to understand what a given function does.

Docstrings commonly describe:

- what the function or class does
- what parameters the function or class takes as arguments and their types
- what the code returns
- what common errors can occur and the exceptions they'll raise
- links to or descriptions of the methodology the function implements
- example usage of the function
- references to other functions or classes that are related to this function

But in general, there is scope to add any information that you consider relevant to an end-user of this particular function.

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
#'@title add_to_each
#'
#'@description Add a number to elements of a vector
#'
#'@details Cycles through a vector of numbers and adds a user-specified number to each element.
#'
#'@param numbers A vector of numbers
#'@param add A float or integer to be added to each element of \code{numbers}
#'
#'@return \code{numbers} with \code{add} added to each element
#'
#'@seealso \code{\link{add}}
#'@examples
#' add_to_each(list(1, 2, 3), 5)
#'
#'@export
add_to_each <- function(numbers, add) {
  if (!(is.vector(numbers) & is.numeric(numbers)) {
    stop("'numbers' must be a numeric vector.")
  }
  numbers + add
}
```

````

In this example, the function docstring starts with a brief description. It then lists the parameters that our function takes, along with the suggested type for each parameter and a brief description of what they control. It also tells us that the function will raise an error if the wrong type is provided for the first parameter. Note that the listed errors are the errors that are expected by the writer of the documentation, other unexpected issues can still occur if the function is not properly tested and will not be signposted in the docstring. Then there is a description of the object that is returned from the function, followed by an example of the functions use. Finally, it references a similar related function that might be of interest to the end-user.

You might find that writing function, class or package descriptions prior to writing their code helps you to focus on the task at hand. The documentation should be a specification of what the code is expected to do. As documentation tends to be user-focussed, this approach helps you to keep the user's needs in mind when developing code and provides a quick reference when more information on its capabilities are required.

Lastly, perhaps one of the key things to remember when writing docstrings is to **keep them up to date**. If these crucial bits of information no longer represent what the code actually does, the end-user will be misled. This might lead to various issues ranging from wasted time to serious methodological implications.

Therefore, write these docstrings early, preferably as you go along or even beforehand when you have a clear idea of what you want to implement. Make sure to update them as you change the functionality of the code. Good function or class level documentation is a good habit to develop for writing professional working code.

```{note}
**Docstrings conventions and styles**

The Python example above follows the [numpydocs style](https://numpydoc.readthedocs.io/en/latest/format.html) and is a common sight when using the `numpy` python package. However, there are various other standards such as [the Google style guides for docstrings](https://google.github.io/styleguide/) as well as official [docstring specification for Python](https://www.python.org/dev/peps/pep-0257/). The R example uses the [roxygen2 package](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) and follows the [tidyverse style guide](https://style.tidyverse.org/documentation.html).

In general, the core idea behind style is **consistency**. Whatever alterations to these conventions are in use for your particular area, it is much more important to keep them up to date and consistent between your collaborators than the exact choice of a style guide. However, as you will see in the section on [generating documentation](generating_docs), having a well-known standard in place helps you to find tools that can generate nice and hostable documentation automatically.

Other useful resources include:

- [Python docstring convention](https://www.python.org/dev/peps/pep-0257/)
- Guidance for [documenting objects and functions in R](http://r-pkgs.had.co.nz/man.html)
```

(generating_docs)=
## Automatic documentation generation

This section does not describe a tool that writes your documentation for you. It does, however, describe tools that automate generation of searchable, user-friendly HTML documentation that can really provide a great experience for end-users. Accurate, up to date and accessible documentation is one of the cornerstones of well-adopted, open-source packages.

Perhaps it is worth reflecting on truly how much we use well-rendered documentation for our favourite programming packages. It would be much harder it to adopt these packages to solve hard programming problems if they were not well-documented and their documentation was not easily accessible.

The information presented in this section seeks to inform you of how you can take your well-crafted [docstrings](docstrings) and turn them into more widely accessible hosted documentation.

### Generating HTML documentation

#### Python

For Python, we recommend the Python package [`sphinx`](https://www.sphinx-doc.org/en/master/) for generating HTML documentation. Sphinx primarily uses the [`reStructuredText`](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) markup language, which is similar to `markdown`. That said, for those more familiar with `markdown` and in teams/environments where learning a new markup language is not a top priority, [`sphinx` can be extended to also support `markdown`](https://www.sphinx-doc.org/en/master/usage/markdown.html).

Sphinx supports code highlighting for multiple programming languages within a project, however, other tools may be required to automatically collate documentation from code in languages other than Python. These are not addressed here.

Sphinx also supports theming, with a [myriad of themes](https://www.writethedocs.org/guide/tools/sphinx-themes/) available out of the box. With a little bit of extra time you can even develop and adapt the existing themes into a custom theme suitable for your work.

As well as theming support, `sphinx` allows users to develop extensions that extend its functionality. This GitHub repository provides a list of [useful ways to extend the functionality of `sphinx`](https://github.com/yoloseem/awesome-sphinxdoc) to suit your needs.

To illustrate how this can be extremely useful, we will introduce the [doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html). It searches your existing docstrings for the `Examples` section and runs all of the included snippets of code, warning you if they do not run successfully. This means that you can ensure that your examples written in the documentation run to completion. Although this can't replace thorough code testing, it may help you to spot a whole slew of issues stemming from potentially out of date documentation and examples that no longer apply when the code has been fundamentally altered.

#### R

For R projects, you might want to consider [`pkgdown`](https://pkgdown.r-lib.org/). This package will create a HTML references section, containing your code documentation. It uses your project's README file as a home page for the site and you can add additional content to the site in the form of [vignettes](https://r-pkgs.org/vignettes.html).

The [package's website](https://pkgdown.r-lib.org/) and [its source code](https://github.com/r-lib/pkgdown/) provide a good demonstration of how you would apply it in practice.

### Hosting HTML documentation

Once built, the HTML files containing your documentation can be opened in any browser. Usually this means looking for an `index.html` file in the output directory and opening it with your browser. This is sufficient for local usage, however, in order to improve the end-user experience and remove the need to browse the files looking for `index.html`, it is wise to host this documentation somewhere where it will be publicly available.

Your version control platform might support hosting web pages already. GitHub provides this hosting via [GitHub Pages](https://pages.github.com/) and is able to host not only documentation, but any web page virtually for free. The book that you're reading right now is hosted in this way. In many cases, you may also be able to automatically update your hosted documentation using [Continuous Integration](continuous-integration) practices.

[Read the docs](https://readthedocs.org/) is a community-funded project that provides hosting for open source projects and is a great place to host any rendered documentation.
