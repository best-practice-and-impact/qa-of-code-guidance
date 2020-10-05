# Structuring your project

When you're designing your analysis it can often be difficult to keep your thoughts tidy.
Analysis is often exploratory and subject to change.
This nature means that scripts and programs can become messy.
The messier the programs the harder they are to maintain and change.

A good directory structure and file hygiene can go a long way to mitigate this.
Not only will it help others read your code easier but you will write better code.
Some structures have been found to be pretty general through trial and error.
Others are more specific, and - as with all guidelines - should not be taken as mandatory.

## Scripts ★☆☆☆☆

As you begin developing your project it's a good idea to save your working code in a script file.
In R these are saved as `.R` files, and in python as `.py`.
Scripts can be used within an IDE (integrated development environment) like [Visual Studio Code](https://code.visualstudio.com/), [RStudio](https://rstudio.com/), or [pycharm](https://www.jetbrains.com/pycharm/).
Inside an IDE you can usually run through your script line-by-line, or run the whole file at once.
This can be an easier workflow than running code in the python or R console and then rewriting the same code in a script later.

Scripts serve as the basic units of saved code.
Often, we like to define functions or reusable bits of code in one file and then use these in another file.
For example we may write a few functions that help us to calculate `mean`, `mode`, and `median` of our dataset in the `functions.R` file.
Then we can use those functions in our main script, saved in `main.R`.

Outside of an IDE you can also run your scripts using the python or R interpreters from the command line.
This allows other programs to use your scripts.
For example you can use the `Rcmd <script-path>` command to run your R scripts or the `python <script-path>` command to run your python scripts.




## Clean directories ★☆☆☆☆


### Analysis is a DAG


### Raw data should be preserved


## Modules and packages ★★☆☆☆


## Cookiecutter ★★☆☆☆


## Repositories ★★☆☆☆