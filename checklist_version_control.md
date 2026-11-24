# Version Control

When working on an important project you want to ensure that development and work is as painless and clean as possible. 
This is were version control can help. By utilising different branches and using commits carefully you can ensure that work of the correct quality is utilised and becomes part of the main project. 
By following these techniques and standards you can ensure that your main branch (or the production ready code) stays working, while working on fixes and updates, 
as well ensuring you keep accountability within the project.

Below are some the standards to help utlise version control effectively (both advanced and basic).

More details are [here][book/version_control.md]


## Minimum Standards

By understanding and using these standards you will be utilising version control effectively:

- Commits are an easy way to keep a history on changes that have occurred.
  By adding regular commits you can make reviews smaller and easier,
  and if anything breaks it is easier to locate where it broke.
- With any commit you should not be using any sensitive data, only dummy data, as the project is likely to be open,
  to help keep things transparent and easier to review, any sensitive data would be shared.
  Commit only dummy data created for the task.
- Its useful when using commits to leave clear and concise messages with them.
  This means when someone is looking at the commit history,
  they quickly understand what has been completed and makes finding the wanted commit easier.
- Branch protection ensures that branches are only merged when requirements are met.
  This limits the chances that a damaging branch is merged onto production and causing down time while it’s repaired.
  These requirements could be certain tests being passed,
  age of the branch or even CI checks (which are discussed more in advanced techniques).
- Each time a new commit is pushed it is given a unique value or tag. You can also assign tags to commits as well.
  With this tag you can utilise some of GitHub’s features easier, you can remove unwanted commits,
  revert back to earlier ones amongst other uses,
  this is all possible with learning the tags of the commits you want to alter or utilise.


## Advanced Techniques 

Here are some advanced techniques to consider as well:

- While I have already highlighted some uses with tags, there are more complex uses as well.
  These however generally require set up at the beginning of the project to be useful and may not suit every project.
  However, if implemented correctly, you can automatically trigger specific tests based on tags,
  automatically set version numbers (and helping with documenting version history) as well query the commit history more specifically. 
- When you run the commit command, you can set it up so a script will run before the commit is start and completed. This is a pre-commit hook, and it can be very useful.
  This script can contain tests to ensure you are using the right config, can make minor changes to keep code consistent (such as trailing lines and linting) as well other minor changes.
  If such changes do occur or tests do fail, then the commit is cancelled allowing you to review things before it’s pushed on.
  So, pre-commit hooks act as a way to ensure the right standards are meet before being merged into production code.
- In branch protection I touched on CI (Continuous Improvement/ Continuous Delivery) so let’s go into more detail.
  CI/CD is the idea that when a new commit is pushed tests are automatically ran and integration is checked.
  CI/CD is a culmination of standards we have discussed here, and the purpose is to ensure that a lot of the work for checking and testing new changes can occur automatically,
  this helps save time as well limits human error which is common in these checks. It also helps maintain a high standard for your project.
