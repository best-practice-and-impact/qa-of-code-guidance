

### Modular code (LOWER)

- Individual pieces of logic are written as functions. Classes are used if more appropriate.
- Repetition in the code is minimalised. For example, by moving reusable code into functions or classes.

### Modular code (Moderate)

- Code is grouped in themed files (modules) and is packaged for easier use.
- Main analysis scripts import and run high level functions from the package.
- Low level functions and classes carry out one specific task. As such, there is only one reason to change each function.

### Modular code (Higher)

- Objects and functions are open for extension but closed for modification; functionality can be extended without modifying the source code.
- Subclasses retain the functionality of their parent class while adding new functionality. Parent class objects can be replaced with instances of the subclass
 and still work as expected.

 ### Modular Code  


<details>
    <summary>Modular Code Checklist</summary>

| Key Features                                                                                           | Level    | Status
|--------------------------------------------------------------------------------------------------------|----------|----|
| Individual pieces of logic are written as functions. Classes are used if more appropriate. | Lower / Moderate / Higher | [ ] |
| Repetition in the code is minimalised. For example, by moving reusable code into functions or classes. | Lower    | |
| Code is grouped in themed files (modules) and is packaged for easier use.                          | Moderate | |
| Objects and functions are open for extension but closed for modification; functionality can be extended without modifying the source code.     | Higher   | |

</details>

### Project Structure
<details>
    <summary>Project structure Checklist</summary>

| Key Features                                                                                           | Level    | Status
|--------------------------------------------------------------------------------------------------------|----------|----|
| Individual pieces of logic are written as functions. Classes are used if more appropriate. | Lower / Moderate / Higher | [ ] |
| Repetition in the code is minimalised. For example, by moving reusable code into functions or classes. | Lower    | |
| Code is grouped in themed files (modules) and is packaged for easier use.                          | Moderate | |
| Objects and functions are open for extension but closed for modification; functionality can be extended without modifying the source code.     | Higher   | |

</details>

widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)



