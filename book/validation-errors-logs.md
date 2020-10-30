# Validation, errors and logging

How will you know if something goes wrong?
How will your pipeline react if there is an unexpected upstream change?
What diagnostics do you need?

In a perfect world, we would expect our data to come in on time, in the right shape, and with no new errors.
Unfortunately we live in the real world.
Data come in late or early, in the wrong form, with errors that make you go "how in hell did that happen".

Your program must be resistant.
