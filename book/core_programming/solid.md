# SOLID ★★★☆☆

SOLID is an acronym that encompasses 5 software design principles that are intended to increase the readability and extensibility of software source code.
These principles are designed to improve object-oriented programs, but can be roughly applied to functional programs.

## Single responsibility

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


```{figure} ../_static/separation_of_concerns.png
---
width: 80%
name: separation_of_concerns
---
Representation of concerns and responsibilities within a piece of software
```


As such, separate sections of your software should be responsible for each of the concerns.
Within each section of your software, distinct functions or classes should be responsible for each task that is required for that sections overall functionality.

## Open-closed

> Objects and functions should be open for extension, but closed for modification

This means that it should be possible to extend the functionality of classes or functions, without modifying their source code or how they work.
For example, extension of a class or function could be carried out through sub-classing or wrapper functions and decorators, respectively.

This makes managing dependencies much easier between packages and projects.

In functional programming we can use the concepts of function composition and higher-order functions to enact the open-closed principle.

## Liskov substitution

> Objects should be replaceable with instances of their subtypes, without altering the correctness of that program
> Functions should be replaceable with similar functions that observe the same interface contract.

Subclasses should not damage the functionality of their parent class in their implementation.
They should extend their usefulness, but retain their original functionality.

If you were to increase the domain and range of a function to account for new cases then this function should observe the same interface as the previous function.

## Interface segregation

> Many client-specific interfaces are better than one general-purpose interface

As you add more and more functionality into a single interface, it becomes more difficult to extend or maintain. 
Separating these into multiple interfaces increases simplicity and maintainability.


## Dependency inversion

> Depend on abstractions, not concretions

High level modules should not depend on low-level modules. 
Both should depend on interfaces - i.e. be built with this interaction in mind.
Abstractions should not depend on specific details.
Concrete implementations should depend on abstractions.

Specify parameters to a function (or a higher order function to retrieve them) rather than hard coding the function to get some value.
The function should not look outside of its own environment for data.
