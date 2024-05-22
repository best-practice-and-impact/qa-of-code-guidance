# Configuration

Configuration describes how your code runs when you execute it.

In analysis, we may want to run our analysis code using different inputs or parameters.
And we likely want other analysts to be able to run our code on different machines, for example, to reproduce our results.
This section describes how we can define analysis configuration that is easy to update and can remain separate from the logic in our analysis.


## Basic configuration

Configuration for your analysis code should include high level parameters (settings) that can be used to easily adjust how your analysis runs.
This might include paths to input and output files, database connection settings and model parameters that are likely to be adjusted between runs.

In early development of our analysis, lets imagine that we have a script that looks something like this:

````{tabs}

```{code-tab} python
# Note: this is not an example of good practice
# This is intended as example of what early pipeline code might look like
data = read_csv("C:/a/very/specific/path/to/input_data.csv") 

variables_test, variables_train, outcome_test, outcome_train = train_test_split(data["a", "b", "c"], data["outcome"], test_size=0.3, random_seed=42)

model = Model()
model.fit(variables_train, outcome_train)

# prediction = model.predict(variables_test, constant_a=4.5, max_v=100)
prediction = model.predict(variables_test, constant_a=7, max_v=1000)

prediction.to_csv("outputs/predictions.csv")

```

```{code-tab} r R
# Note: this is not an example of good practice
# This is intended as example of what early pipeline code might look like
data <- read.csv("C:/a/very/specific/path/to/input_data.csv") 

set.seed(42)
split <- caTools::sample.split(data, SplitRatio = .3)

train_data <- data[split, ]
test_data <- data[!split, ]

model <- glm(formula = outcome ~ a + b + c, family = binomial(link = "logit"), data = train_data, method = "model.frame")
# model <- glm(formula = outcome ~ a + b + c, family = binomial(link = "logit"), data = train_data, method = "glm.fit")


prediction <- predict(model, test_data, type = "response")

write.csv(prediction, "outputs/predictions.csv")

```

````

Here we're reading in some data and splitting it into subsets for training and testing a model.
We use one subset of variables and outcomes to train our model and then use the subset to test the model.
Finally, we write the model's predictions to a `.csv` file.

The file paths that are used to read and write data in our script are particular to our working environment.
These files and paths may not exist on an other analyst's machine.
As such, other analysts would need to read through the script and replace these paths in order to run our code.
As we'll demonstrate below, collecting flexible parts of our code together makes it easier for others to update them.

When splitting our data and using our model to make predictions, we've provided some parameters to the functions that we have used to perform these tasks.
Eventually, we might reuse some of these parameters elsewhere in our script (e.g. the random seed)
and we are likely to adjust these parameters between runs of our analysis.
To make it easier to adjust these consistently throughout our script, we should store them in variables.
We should also store these variables with any other parameters and options, so that it's easy to identify where they should be adjusted.

Note that in this example we've tried our model prediction twice, with different parameters.
We've used comments to switch between which of these lines of code runs.
This practice is common, especially when we want to make a number of changes when developing how our analysis should run.
However, commenting sections of code in this way makes it difficult for others to understand our code and reproduce our results.
Another analyst would not be sure which set of parameters was used to produce a given set of predictions, so we should avoid this form of ambiguity.
Below, we'll look at some better alternatives to storing and switching our analysis parameters.

````{tabs}

```{code-tab} python
# Note: this is not an example of good practice
# This is intended as an example of basic in-code configuration. 

# Configuration
input_path = "C:/a/very/specific/path/to/input_data.csv"
output_path = "outputs/predictions.csv"

test_split_proportion = 0.3
random_seed = 42

prediction_parameters = {
    "constant_a": 7,
    "max_v": 1000
}

# Analysis
data = read_csv(input_path)

variables_test, variables_train, outcome_test, outcome_train = train_test_split(data["a", "b", "c"], data["outcome"], test_size=test_split_proportion, random_seed=random_seed)

model = Model()
model.fit(variables_train, outcome_train)

prediction = model.predict(variables_test, constant_a=prediction_parameters["constant_a"], max_v=prediction_parameters["max_v"])

prediction.to_csv(output_path)
```

```{code-tab} r R
# Note: this is not an example of good practice
# This is intended as an example of basic in-code configuration. 

# Configuration
input_path <- "C:/a/very/specific/path/to/input_data.csv"
output_path <- "outputs/predictions.csv"

random_seed = 42
test_split_proportion = .3
model_method = "glm.fit"

#analysis
data <- read.csv(input_path) 

set.seed(random_seed)
split <- caTools::sample.split(data, SplitRatio = test_split_proportion)

train_data <- data[split, ]
test_data <- data[!split, ]

model <- glm(formula = outcome ~ a + b + c, family = binomial(link = "logit"), data = train_data, method = model_method)

prediction <- predict(model, test_data, type = "response")

write.csv(prediction, output_path)
```

````

Separating configuration from the rest of our code makes it easy to adjust these parameters and apply them consistently throughout the analysis script.
We're able to use basic objects (like lists and dictionaries) to group related parameters.
We then reference these objects in the analysis section of our script.

Our configuration could be extended to include other parameters, including which variables we're selecting to train our model.
However, it is important that we keep the configuration simple and easy to maintain.
Before moving aspects of code to the configuration it's good to consider whether it improves your workflow.
If it is something that is dependent on the computer that you are using (e.g. file paths) or is likely to change between runs of your analysis,
then it's a good candidate for including in your configuration.


## Use separate configuration files

We can use independent configuration files to take our previous example one step further.
We simply take our collection of variables, containing parameters and options for our analysis, and move them to a separate file.
As we'll describe in the following subsections, these files can be written in the same language as your code or other simple languages.

Storing our analysis configuration in a separate file to the analysis code is a useful separation.
It means that we can version control our code based solely on changes to the overall logic - when we fix bugs or add new features.
We can then keep a separate record of which configuration files were used with our code to generate specific results.
We can easily switch between multiple configurations, by providing our analysis code with different configuration files.

You may not want to version control your configuration file,
for example if it includes file paths that are specific to your machine or references to sensitive data.
In this case, you should include a sample or example configuration file, so that others can use this as a template to configure the analysis for their own environment.
It is key that this template is kept up to date, so that it is compatible with your code.


### Use code files for configuration

To use another code script as our configuration file, we can copy our parameter variables directly from our scripts.
Because these variables are defined in the programming language that our analysis uses, it's easy to access them in our analysis script.
In Python, variables from these config files can be imported into your analysis script.
In R, your script might `source()` the config file to read the variables into the R environment.


### Use dedicated configuration files

Many other file formats can be used to store configuration parameters.
You may have come across data-serialisation languages (including YAML, TOML, JSON and XML), which can be used independently of your programming language.

If we were to represent our example configuration from above in YAML, this would look like:

```yaml
input_path: "C:/a/very/specific/path/to/input_data.csv"
output_path: "outputs/predictions.csv"

test_split_proportion: 0.3
random_seed: 42

prediction_parameters:
    constant_a: 7
    max_v: 1000
```

Configuration files that are written in other languages may need to be read using relevant libraries.
The YAML example above could be read into our analysis as follows:

````{tabs}

```{code-tab} python
import yaml

with open("./my_config.yaml") as file:
    config = yaml.safe_load(file)

data = read_csv(config["input_path"])
...
```

```{code-tab} r R
config <- yaml::yaml.load_file(config_path)

data <- read.csv(config$input_path)
...
```

````

Configuration file formats like YAML and TOML are compact and human-readable.
This makes them easy to interpret and update, even without knowledge of the underlying code used in the analysis.
Reading these files in produces a single object containing all of the `key:value` pairs defined in our configuration file.
In our analysis, we can then select our configuration parameters using their keys.


## Use configuration files as arguments

In the previous example, we have stored our configuration options in a separate file and referenced this in our analysis script.
Although this allows us to separate our configuration from the main codebase, we have used a hard-coded path to the configuration file.
This is not ideal, as for the code to be run on another machine the configuration file must be saved on the same path.
Furthermore, if we want to switch the configuration file that the analysis uses we must change this path or replace the configuration file at the specified path.

To overcome this, we can adjust our analysis script to take the configuration file path as an argument when the analysis script is run.
This can be achieved in a number of ways, but we'll discuss a minimal example here:

````{tabs}

```{code-tab} python
import sys
import yaml

if len(sys.argv) < 2:
    # The Python script name is counted as the first argument
    raise ValueError("Configuration file must be passed as an argument.")

config_path = sys.argv[1]
with open(config_path) as file:
    config = yaml.safe_load(file)
...
```

```{code-tab} r R
args <- commandArgs()
if (length(args) < 1) {
  stop("Configuration file must be passed as an argument.")
}

config_path <- args[1]
config <- yaml::yaml.load_file(config_path)
...
```

````

When executing the analysis file above, we pass the path to our configuration file after calling the script.
If our script was named 'analysis_script', it would be called from the command line as:

````{tabs}

```{code-tab} sh Python
python analysis_script.py /path/to/my_configuration.yaml
```

```{code-tab} sh R
Rscript analysis_script.R /path/to/my_configuration.yaml
```

````

If we now want to run our analysis with a different configuration we can simple pass another configuration file to the script.
This means that we don't need to change our code to account for changes to the configuration.

```{note}
It is possible to pass configuration options directly as arguments in this way, instead of referencing a configuration file.
However, use of configuration files should be preferred as they allow us to document which configuration
has been used to produce our analysis outputs, for reproducibility.
```


(environment-variables)=
## Configure secrets as environment variables

Environment variables are variables that are available in a particular environment.
In most analysis contexts, our environment is the user environment that we are running our code from.
This might be your local machine or dedicated analysis platform.

If your code depends on credentials of some kind, these must not be written in your code.
Passwords and keys could be stored in configuration files, but there is a risk that these files may be included in [version control](version_control.md).
To avoid this risk, it is best to store this information in local environment variables.

Environment variables can also be useful for storing other environment-dependent variables.
For example, the location of a database or a software dependency.
This might be preferred over a configuration file if very few other options are required by the code.

In Unix systems (e.g. Linux and Mac), environment variables can be set in the terminal using `export` and deleted using `unset`:

```none
export SECRET_KEY="mysupersecretpassword"
unset SECRET_KEY
```

In Windows, the equivalent commands to these are:

```none
setx SECRET_KEY "mysupersecretpassword"
reg delete HKCU\Environment /F /V SECRET_KEY
```

These can alternatively be defined using a graphical interface under `Edit environment variables for your account` in your Windows settings.

Once stored in environment variables, these variables will remain available in your environment until they are deleted.

You can access this variable in your code like so:

````{tabs}

```{code-tab} python
import os

my_key = os.environ.get("SECRET_KEY")
```

```{code-tab} r R
my_key <- Sys.getenv("SECRET_KEY")
```

````

It is then safer for this code to be shared with others, as it is not possible to acquire your credentials without access to your environment.
