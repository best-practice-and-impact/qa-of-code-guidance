### Modular code

#### Lower
- Individual pieces of logic are written as functions. Classes are used if more appropriate.
- Repetition in the code is minimalised. For example, by moving reusable code into functions or classes.

#### Moderate

- Code is grouped in themed files (modules) and is packaged for easier use.
- Main analysis scripts import and run high level functions from the package.
- Low level functions and classes carry out one specific task. As such, there is only one reason to change each function.

#### Higher

- Objects and functions are open for extension but closed for modification; functionality can be extended without modifying the source code.
- Subclasses retain the functionality of their parent class while adding new functionality. Parent class objects can be replaced with instances of the subclass
 and still work as expected.

### Good coding practices

#### Lower

- Names used in the code are informative and concise.
- Code logic is clear and avoids unnecessary complexity.
- Code follows a standard style, e.g. [PEP8 for Python](https://www.python.org/dev/peps/pep-0008/) and [Google](https://google.github.io/styleguide/Rguide.html) or [tidyverse](https://style.tidyverse.org/) for R.

#### Moderate

- Names used in the code are explicit, rather than implicit.

#### Higher

- nothing new in higher - what do we want in this scenario?

 ### Checklists

 <details>
    <summary>Checklist</summary>
<!-- AUTO-TABLE:START -->
<!-- AUTO-TABLE:END -->
</details>


















 