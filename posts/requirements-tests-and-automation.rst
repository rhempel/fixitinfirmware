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

**Jira**.

Yes, that `Jira`_, along with the `Xray`_ and `R4J - easeRequirements`_ plugins.

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

By the end of this series, it will be clear that Jira gives you answers to all
of these questions if you and the team have the discipline to keep using the tool.
In my experience, once you have things running smoothly, your team won't want
to lose their new capability.

I have set up a `public instance of Jira`_ that you can follow along with. I will
be adding requirements for `umm_malloc`_ - a heap memory management library for 
embedded systems. Unless absolutely necessary, I will avoid making any changes
to the default configuration of Jira and its plugins. If I do make changes, there
will be an explanation for why it was necessary.

This is not a step-by-step handholding tutorial for using Jira, Xray, and R4J. There
are many online resources on how to get things done with these applications, starting
at the product's own website. I will assume you have the ability search for anything
that I am assuming you already know. Do feel free to reach out if you have suggestions
fo improvements.

Finally, you will need your own Jira instance to actually make queries against. The
good news is that `Atlassian`_ is very generous with open source projects (like this site)
and offers an `Open Source Cloud Subscription`_ to qualifying projects.

Let's get started!

Verify the Jira REST API Is Working
-----------------------------------

The first thing we need to do is get a Personal Access Token (PAT) for your scripts
to use as the authentication method to interact with Jira and its plugins. You might
consider creating a virtual user for automation that is authenticated with their own
user. That will make it easier to restrict what your scripts can do and lets you know
whether a change came from automation or a human.

In Jira navigate to user account and then to ``Security`` | ``API Tokens`` | ``Create and manage API tokens``
to create a new token. You will need to save this token and treat it like a password.
It will be used to identify any HTTPS requests as coming from you.

Once you have the API token you should make a ``curl`` query against your project,
like this:

{{% listing curl_access_token_test.sh bash %}}

If everything is working, you will get back a chunk of JSON text that can be parsed
with a number of different libraries. Personally I prefer using Python for this
as there is good support for HTTPS requests, JSON parsing, and test automation in
general.

You can find more details on the `Jira REST API Authentication`_ process and the `Jira Cloud REST API`_
if you want to explore in depth.

The Big Picture
---------------

Now that we have programmatic access to Jira, we need to add some requirements,
create a few tests or test sets, add them to a test plan, and finally execute
that plan.

Resist the urge to dive in and just start writing requirements and tests until
you are clear on what is needed to make these artifacts useful.

Unless you already have a functional CI/CD pipeline, and you can answer the
big "How close are we to done?" question confidently, do *not* import your existing
requirements and tests into Jira. They are probably not very good requirements, and
you will actually have MORE work sorting out the good requirements from the bad.

Your organization probably has some form of the 'V Model'_ for systems engineering.
It probably looks a lot like the one on the 'V Model'_  Wikipedia page - with the
Implementation at the bottom of the V shown as a vague yellow blob.

That's where we will be putting our focus, and we don't really care what the rest
of the organization's requirements tool is. We need to ba able to leverage the
power of Jira and those plugins ourselves, because almost everything above that blob
will involve coordination with other teams, and our goal here is to be sure
our part of the system works properly before integration.

Let's start with a brief section on each kind of artifact.

Requirements
============

There are *many* resources online for requirements management - and I don't have
original thoughts on this topic in general. For embedded systems development
specifically, there are a few things that I can share with you.

What makes a good embedded systems requirement, and what are some "requirement
smells" that hint at potential improvements?

Specific
  A functional requirement should be specific, which means it describes
  a small (ideally one) part of the system operation under specific conditions.
  A helpful notation is the `EARS syntax`_ - a guide to writing better
  requirements. You want to be able to write one or at most a handlful
  of tests to fulfill the requirement.
  
  You know when your requirement is too broad becuase you will have a dozen or more
  tests to fulfill the requirement, and those tests each link link to multiple
  requirements.

Measureable
  Requirements for embedded systems are measureable - and that means that you
  can probably run an automated test and programmatically pass or fail the
  test without human intervention.

  It's usually pretty easy to figure out if a requirement needs to be improved by
  asking the question "How will the test system decide if the test has passed?".

  If it's not automatic, then figure out a way to make it so.

Tests
=====

There are also *many* resources online for test cases, and I'll just share some
thoughts for embedded systems specifically.

What makes a good embedded systems test, and what are some "test
smells" that hint at potential improvements?

Fast
  There are a few cases where we need to run tests for extended periods of time
  but in general you want your tests to be fast. That means using off target
  tests to ensure your modules work well before you build a firmware image to
  test fuctionality on real hardware.

  You want developers to run the off target tests automatically, ideally
  every time they save a file. You want your CI/CD system to run the same
  tests when building a potential release. You want to be able to deploy a
  firmware image to hardware and test its functionality without having to
  put it in a bigger system needing human intervention to control it.

Specific
  Just as your requirements are specific, your tests should also cover as
  few requirements as possible.
  
  When a test does too many things it tends to become brittle. Small changes
  in requirements can break complex tests, and that reduces confidence in
  developers because they blame the "complicated testing setup" when it's
  the tests that are too complex.

Non-Invasive
  For embedded systems you do not want to test the implementation - that
  means you avoid tests that need special code to reach into the system to
  check state or data structures.

  Test the interfaces. What is the expected output or system state when this
  API is called with these parameters. Sometimes you will need to look at an
  output buffer or data structure to verify an API, but this should be the
  exception rather than the rule, and it should be self-contained in case the
  implementation changes.

  You will know when you have broken this rule the first time you change
  an implementation and multiple tests break.

Requirement, Test, Sets Set, Test Plan, Execution - Oh My!
----------------------------------------------------------

I have used all these terms at some poinnt in this document, and now it's
time to do a very bierf overview of what they mean:

A **Requirement** is a specific description of something that your API, or
subsystem, or firmware has to do to fulfil a customer level requirement. It
is not a description of how that functionality is implemented.

A **Test** is a specific description of one or more preconditions, operations,
and expected outputs of the interface or API that is implemented in firmare. It
is not a test of the implementation, it is a test of the operation.

A **Test Set** is simply a group of one or more tests that cover a related
bit of functionality. A test may exist in more than one test set.

A **Test Plan** is a collection of test sets and/or tests that cover a product
variant or version. Tests and Test Sets can exist in multiple Test Plans.

A **Test Execution** is the result of running a Test Plan with optional
variables for version, environment, product variant.

The Xray documentation is very good, and a good place to start is with
the 'Xray Terms and Concepts'_ page.

Next Steps
----------

In subsequent posts, I'll go over how we can set up a minimal proof of concept
in Python for all of the ideas in this post. We will:

#. Create a simple requirement in Jira
#. Create a test, test set, and test plan in Jira 
#. Write a Python script to fulfil the requirement
#. Write a pytest script to test the Python script
#. Write a Python program to parse the test results and report to the Jira REST API
#. Verify in Jira that the test has been executed and the requirement is satisfied

That sounds like a lot of steps, and it is. Would you rather track requirements
and test cases and executionss manually? I didn't think so.

If you are unfamiliar with Python, then I recommend you get Al Sweigart's book
'Automate the Boring Stuff WIth Python'_. Invest some time in learning because
using a scripting language like Python will up your embedded development game
by making many of your tasks much easier.

I hope you are ready for a transformative journey!

.. _`public instance of Jira`: https://fixitinfirmware.atlassian.net
.. _`umm_malloc`: https://github.com/rhempel/umm_malloc

.. _Atlassian: https://www.atlassian.com/
.. _Open Source Cloud Subscription: https://www.atlassian.com/software/views/open-source-license-request
.. _Jira: https://www.atlassian.com/software/jira
.. _Xray: https://marketplace.atlassian.com/apps/1211769/xray-test-management-for-jira
.. _R4J - easeRequirements: https://marketplace.atlassian.com/apps/1213064/easerequirements-requirements-management-for-jira-r4j

.. _Xray Terms and Concepts: https://docs.getxray.app/display/XRAYCLOUD/Terms+and+Concepts

.. _Automate the Boring Stuff With Python: https://automatetheboringstuff.com/

.. _EARS syntax: https://alistairmavin.com/ears/
.. _V Model: https://en.wikipedia.org/wiki/V-model 

.. _Jira REST API Authentication: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
.. _Jira Cloud REST API: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#version

.. _Perforce: https://www.perforce.com/ 
.. _Jazz: https://jazz.net/
.. _DOORS: https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/doors
.. _HPQC: https://www.opentext.com/products/application-quality-management
.. _Wikipedia page for Requirements analysis: https://en.wikipedia.org/wiki/Requirements_engineering_tools

