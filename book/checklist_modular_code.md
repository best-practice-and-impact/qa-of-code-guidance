# Modular Code

When working on a large project you are likely to see patterns repeating, certain processes that used several times. 
To help deal with this and improve the quality of your code, you should implement modular coding practices. 
If a process is repeated several times (such as cleaning data or modifying it) repeating that code again and again is more likely to introduce human error. 
You can also reduce the size of your code by using modular code and make it far more readable and easier to check as well.
By utilising the standards below, you will improve your code base and can also make it easier to work on.

You can find more details [here][book/modular_code.md]


## Minimum Standards

Below are some simple points to achieve minimum standards using modular code:

- One of the basic blocks of code is functions. By creating custom functions,
  you can simply write it once and then call it several times instead.
  So instead of repeating several lines of code, all your doing is repeating several words.
  Also, if you only have to write the function once, it’s much easier to make sure it is documented correctly,
  making it easier to read and understand. 
- If you have many different functions you might want to start bundling them together based on use, on its own separate page in your project.
  This is called a module and helps solidify the strengths of using modular code.
  For one it makes it much easier to locate functions, and also to call those functions even if they are located on another page.
  There is also another advantage, sometimes a function requires a process that is already being used, so instead of repeating it, use it as a function.
  Soon you can have functions using other functions. The end result of this chain is called a wrapper, a small function which contains all the functions used.
  Here you are condensing a whole module of code into a small function, which in turn can be called as a single line.  
- It’s also important to be aware of classes, this is the end point of modular code, and gives much finer control than a wrapper can as well introduce new ideas and tools.
  These tools however can be quite advanced so simply understand what they are and their purpose is only needed at this level.


## Advanced Techniques 

Here are some advanced techniques to consider as well:

-	So as previous explained Classes are very similar to modules and wrappers but has more control.
  One of its main differences is encapsulating, with the module any changes with the data is treated in a regular way i.e. shared throughout the code base,
  with classes the changes only exist within the class itself and must be exported allowing finer control of changes.
  Theres also inheritance if you have several functions with similar stages,
  you can instead have a single function with the shared steps and have it inherited by the other functions within the class.
  This is useful as it can cut down on chains quite a lot, and makes it easier to read. While classes are powerful,
  they can also be complicated to implement effectively, and might not be suitable for every project.
