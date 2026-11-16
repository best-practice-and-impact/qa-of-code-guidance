# Logging in Reproducible Analytical Pipelines

Logging is part of the software observability, and provides a structured record of events during a code or pipeline execution. Logging doesn't replace any RAP principles but works alongside them, in particular logging supports the auditable principle providing execution level evidence. 

You might be familiar with console print statements for pipeline observability to provide essential information for code execution. While these can be useful, they lack of structure, they are harder to maintain/extend and the print output can disappear. Pipelines should use a logging framework, where an execution record can be retained, searched or monitored. It also allows logging to become more comprehensive as the complexity and business needs of the pipeline increase. 

If an error arises, logging should provide all the information needed to identify the root cause the error without the need to rerun the pipeline or perform further analysis to find the error. 

## Minimum logging standard for a basic pipeline

Not everything needs to be logged, you must understand the users and the downstream processes in order to create effective logs. At minimum you should include events which might effect the functionality of the pipeline and any misuse or failure in the code produces informative error messages. In addition, if the pipeline uses a configuration or has any other user actions it should be recorded when the code is run.

## More complicated RAP

As the complexity and business criticality increases the above aren't any more sufficient, the logging must be  proportional to the complexity. As the project becomes more complex you might need to add more depth and structure in the logs. Even if the pipeline is not complex other factors like the pipeline being automated and/or handling big data the below fields are critical for code observability.

- severity level (`INFO`, `WARN`, `CRITICAL`,`DEBUG`)
- timestamp and time zone
- pipeline, module and stage
- unique run or identifier
- environment, such as development, test or production
- code release or commit identifier
- input dataset versions, extract dates or checksums where appropriate
- parameter values that materially affect results, provided they are not sensitive
- output versions or checksums
- log retention
- monitoring (failed or incomplete runs, repeated retries)

For validation checks you might need to include fields like:
- schema and type checks
- expected row-count ranges
- uniqueness and referential-integrity checks
- missing-value thresholds
- rejected or quarantined record counts
- whether other checks passed or failed.

For automated or pipelines which run frequently from multiple users you might need to analyse the logs, in this scenario a machine readable structure (like `json`) might be helpful. The logging ideally should provide all the required information for users to understand what happened during the pipeline lifecycle.

For more complex projects doesn't mean you must implement all the above, don't consider these fields as a checklist, instead understand the business needs and create effective logs.

> [!WARNING]  
> Do not log any sensitive information, if it is necessary then you must ensure access controls are appropriate to the sensitivity of the information.
