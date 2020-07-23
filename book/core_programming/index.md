# Core Programming Practices


## Introduction

The principles outlined in this chapter represent good practices in general programming and software development.

Before reading this chapter, you would benefit from having an understanding of basic programming. Awareness of functions and objects will help you code cleaner. These topics are lightly introduced, but we assume some familiarity with basic programming.

## Motivation 

```{epigraph}
Code is read more often than it is written.

-- Guido van Rossum (creator of Python)
```

You can't be available and responsible for long term maintenance of every piece of code that you write. 
In the future, others will inevitably need to use and adapt your code.
It is important that other programmers can quickly and easily understand the task that your code performs.
Many programs perform a task correctly, but are deemed to be "black boxes" because of the barrier to understanding them.
It is your responsibility to avoid putting this barrier in place.

Good code is easier to document, review and test.
These practices are necessary to make sure that your analysis is reproducible, auditable and assured.
Good code helps you with these ambitions.

This chapter highlights good coding practices that will improve the readability, and therefore maintainability, of your code.
However, if your code is well-tested, documented, and reviewed then you have already reached your goal and don't need to add more complexity to your project.
