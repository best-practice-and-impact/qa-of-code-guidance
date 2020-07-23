
# Modular code ★☆☆☆☆

Breaking your code down into smaller, more manageable chunks is a sure fire way to improve readability.

Code comes in many shapes and sizes.
A few code abstractions are outlined below, which will be useful for understanding concepts throughout the rest of this chapter and book.

- Functions
    - a unit of code that performs a minimal number of tasks (one ideally)
    - can take inputs and can return outputs, though both are optional
    - used in functional programming


```{figure} ../_static/function.png
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


```{figure} ../_static/class_pikachu.png
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
