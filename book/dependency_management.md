# Dependency Management

A key part of creating reproducible pipelines is recording external dependencies.
This allows others to easily replicate the environment we have setup to run the pipeline and reproduce our results.

## Minimum Standards

To meet the minimum standards for dependency management we expect all dependencies for the codebase to
be noted in a file at the bare minimum (requirements.txt or other equivalent file).
Developer requirements must also be stored in an equivalent file.

## Advanced Techniques

More advanced users may also consider:

- Use of virtual environments to seperate package requirements for different projects
- Packaging your codebase and using `pyproject.toml` for python or `DESCRIPTION` file in R to store dependencies.
- Utilising dependency management packages (UV, Poetry, etc.) to streamline development processes.
- Use of Containers to further isolate the environment and ensure consistent running environment,  
 see [Docker summary for more details][docker-container-description] [^1]


[^1]: Note this may not be possible depending on your organisations IT policy

[docker-container-description]: https://www.docker.com/resources/what-container/
