# Code Documentation

Your scripts should contain enough documentation for other coders to be able to understand what each part of the code is intended to do.
However, there is such a thing as too much documentation.
Documentation inside the code should not repeat things that are documented elsewhere, for example in the README file.

All functions and classes should have sufficient documentation in docstrings.
The specific style of these can be an individual or team preference,
but should follow [PEP standards][pep-standard] or [Roxygen2 format][roxygen-link] for R.

Good function and class documentation reduces the need to clutter the code with comments and ensures you cover the most important information.
Always document what a function or class takes in as its inputs, what it does,
and what output it produces. If you can, provide an example of use.

Inline code comments should be used sparingly and should only tell you **why** the code does something, **not** how.
The how should be explained by the code its self.
More in depth explanations should instead be stored in the project documentation (LINK TO PROJECT DOCS LIST?)

[pep-standard]: https://peps.python.org/pep-0257/
[roxygen-link]: https://roxygen2.r-lib.org/
