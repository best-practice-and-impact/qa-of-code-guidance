# Peer Review

Peer review involves someone other than the code's author reviewing and testing the code.
It helps identify errors, improve code quality and assess whether the analysis is fit for purpose.

Review code throughout development, rather than waiting until the project is complete.
Keep changes small so that reviewers can give useful feedback and issues can be addressed early.
Make sure the scope of review is proportionate to the risks and complexity of the analysis.

Further details can be viewed in the [peer review chapter of this book][peer-review-chapter].

## Minimum Standards

To meet the minimum standard for peer review, we expect:

- Pull requests (called merge requests on some platforms) are used to review proposed code changes and record feedback.
  See [Google's guide to code review][google-code-review] for advice on reviewing changes and giving useful feedback.
- Pair programming is used to review code as it is written, with developers providing real-time feedback.
  See [GDS's guide to effective pair programming][gds-pair-programming] for practical advice.

## Advanced Techniques

More advanced users may also consider:

- Using a default peer review template to help reviewers apply consistent criteria.
  See [GitHub's guide to creating a pull request template][github-pr-template] for setup instructions.

[peer-review-chapter]: ./peer_review.md
[google-code-review]: https://google.github.io/eng-practices/review/reviewer/
[gds-pair-programming]: https://gds.blog.gov.uk/2018/02/06/how-to-pair-program-effectively-in-6-steps/
[github-pr-template]: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository
