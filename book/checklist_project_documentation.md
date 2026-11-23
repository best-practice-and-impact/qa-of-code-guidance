# Project Documentation

Documentation for your project helps create a resource that will help future users navigate and understand the project in front of them.
While the project might make sense to you and easy to navigate and run, a person without your experience and knowledge might have a very different experience. 
The documentation left behind is a way to share that knowledge and experience.

Not every project is the same and as such you shouldn’t expect to have every single document recommended created for it. 
As long as you can provide the necessary information for a person to set up, run, and update the coding project you have left them, 
then it can be in as many or few documents you want.

Below are some the standards to help guide your decision (both advanced and basic).

More details are [here][book/project_documentation.md]


## Minimum Standards

By ensuring these steps you are ensuring you are hitting the standard requirements for effective project documentation:

- Create a README document (within the project repo), as this is industry standard makes it easy people to find the correct information about the project
- The README should contain a basic 'How to...' guide, leading a new user on what to do run the code include set up and any installation advice (such as installing .venv)
- You should also include guidance to users who might want to make their own changes, this could be design philosophy or even areas that be problematic to update.
- Explaining the validation and verification steps you use. This helps reassure the user (and reader) what you are doing to keep the results accurate and reproducable.
- Finally explaining who does/did what in the project means if there are any questions, they can be sent to the right person, same reason why you should include succession plans.

## Advanced Techniques 

More advanced techniques can also be used such as:
- While we have already discussed about validation and verification, it might be more useful to create a dedicated section about contributing to the project.
  The extra details will explain the process on timelines and generic tests that need to be passed before a contribution will be accepted.
  This will help any contributors understand what to expect and ensure the correct process is followed.
- Some features and packages can even be set up to help with documenting your project.
  It’s important to decide at the beginning of the project to use these so that correct process are kept.
  For example, you could use a package called sphinx, which can pull doc strings from functions and then publishes to a live document,
  as a sort of dictionary for your code base. This file could hosted on either GitHub using GitHub Pages or using readthedocs service.
  This makes documentation automatic and simpler but does require some set up at the beginning of a project.


- Using continuous integration (CI) pipelines to automatically run tests when creating a merge request  
