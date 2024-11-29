.. title: Requirements, Tests, and Automation
.. slug: requirements-tests-and-automation
.. date: 2024-11-23 12:00:00 UTC-05:00
.. status: draft
.. tags: development, embedded, requirements, testing, automation
.. category: Development
.. link: 
.. description: 
.. type: text

{{% glossary_image "787 Wing Load" %}}

So, what's the current status of the firmware?

That's a  most developers and their leaders really dislike
- because they probably don't know the real answer.

Early in the project
it's pretty clear that there is a lot to do, so it's easy to say "We're
just getting started with writing the code, the design is almost finished".

Sometime later your team has run into some obstacles, and when they are
finally moving forward again, the design docs don't get updated because
- well, because you're probably behind schedule.

By the tie firmware is due for final testing before release to production
you're just hoping nothing major happens because you *think* you're done,
but if you're honest, the code reviews and tests have been deprioritized
and you're not really sure if all the corner cases are covered.

If this sounds familiar, keep reading. I'm going to help you and your
team improve your own visibility and confidence in your "done-ness", but
there is no magic silver bullet. It's going to take some up-front work
and team discipline, but I promise the results are worth it.

.. TEASER_END

Use the Tools at Hand
---------------------

The classic requirements management tools like `Perforce`_, `Jazz`_, `DOORS`_,
and whatever `HPQC`_ is called now are big, expensive suites that require more
than a little expertise to set up and maintain. If you are part of a relatively
small organization or even a solo developer, it just doesn't make sense
to use these suites.

On the other hand, there are very few open source alternatives that are up
to a level of usablity and maintainability that I would recommend.

For an overview of Requirements Management tools see this
`Wikipedia page for Requirements analysis`_

So what do I suggest for getting started with Requirements, Tests, and CI/CD
automation?

JIRA.

Yes, that `JIRA`_, along with the `Xray`_ and `R4J - easeRequirements`_ plugins.

As you will see, this is "good enough" for what many organizations need, and it
lets you introduce better requirements management without breaking the bank.

Bare Minimum Requirements for Managing Requirements and Tests
-------------------------------------------------------------

Before we get too far ahead, it's helpful to take a step back and reflect on *why*
we want to take on this extra work of managing tests and requirements. What is
the payoff for you and your team?

#. How close is the team to being done?
#. Is this requirement covered by a test?
#. Have we run all the tests for firmware version x.y.x?
#. Have we covered all the requirements for product variants A and B?
#. When did we run this test for version x.y.z for variant B?
#. Can we link automated test results to test cases?
#. Can we get the tests, requirements, and executions OUT of the database?

The common theme is that automating and linking your test runs to test cases and
requirements gives you and the team the ability to answer these questions quickly
and with confidence, and it can help to give leadership confidence in your team.

By the end of this series, it will be clear that JIRA gives you answers to all
of these questions if you and the team have the discipline to keep using the tool.
In my experience, once you have things running smoothly, your team won't want
to lose their new capability.

I have set up a `public instance of JIRA`_ that you can follow along with. I will
be adding requirements for `umm_malloc`_ - a heap memory management library for 
embedded systems. Unless absolutely necessary, I will avoid making any changes
to the default configuration of JIRA and its plugins. If I do make changes, there
will be an explanation for why it was necessary.

This is not a step-by-step handholding tutorial for using JIRA, Xray, and R4J. There
are many online resources on how to get things done with these applications, starting
at the product's own website. I will assume you have the ability search for anything
that I am assuming you already know. Do feel free to reach out if you have suggestions
fo improvements.

Finally, you will need your own JIRA instance to actually make queries against. The
good news is that `Atlassian`_ is very generous with open source projects (like this site)
and offers an `Open Source Cloud Subscription`_ to qualifying projects.

Let's get started!

First Steps
-----------

The first thing we need to do is get a Personal Access Token (PAT) for your scripts
to use as the authentication method to interact with JIRA and its plugins. You might
consider creating a virtual user for automation that is authenticated with their own
user. That will make it easier to restrict what your scripts can do and lets you know
whether a change came from automation or a human.

In JIRA navigate to user account and then to ``Security`` | ``API Tokens`` | ``Create and manage API tokens``
to create a new token. You will need to save this token and treat it like a password.
It will be used to identify any HTTPS requests as coming from you.

Once you have the API token you should make a ``curl`` query against your project,
like this:

{{% listing curl_access_token_test.sh bash %}}

If everything is working, you will get back a chunk of JSON text that can be parsed
with a number of different libraries. Personally I prefer using Python for this
as there is good support for HTTPS requests, JSON parsing, and test automation in
general.

You can find more details on the `JIRA REST API Authentication`_ process and the `JIRA Cloud REST API`_
if you want to explore in depth.

Next Steps
----------





.. _`public instance of JIRA`: https://fixitinfirmware.atlassian.net
.. _`umm_malloc`: https://github.com/rhempel/umm_malloc

.. _Atlassian: https://www.atlassian.com/
.. _Open Source Cloud Subscription: https://www.atlassian.com/software/views/open-source-license-request
.. _JIRA: https://www.atlassian.com/software/jira
.. _Xray: https://marketplace.atlassian.com/apps/1211769/xray-test-management-for-jira
.. _R4J - easeRequirements: https://marketplace.atlassian.com/apps/1213064/easerequirements-requirements-management-for-jira-r4j

.. _JIRA REST API Authentication: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
.. _JIRA Cloud REST API: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#version

.. _Perforce: https://www.perforce.com/ 
.. _Jazz: https://jazz.net/
.. _DOORS: https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/doors
.. _HPQC: https://www.opentext.com/products/application-quality-management
.. _Wikipedia page for Requirements analysis: https://en.wikipedia.org/wiki/Requirements_engineering_tools

