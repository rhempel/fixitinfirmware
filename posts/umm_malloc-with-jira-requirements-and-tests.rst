.. title: umm_malloc With Jira Requirements and Tests
.. slug: umm_malloc-with-jira-requirements-and-tests
.. date: 2024-11-23 12:00:00 UTC-05:00
.. status: draft
.. tags: development, embedded, requirements, testing, automation
.. category: Development
.. link: 
.. description: 
.. type: text

{{% glossary_image "Flight Director Emily Nelson" %}}

In the `first post of this series <requirements-tests-and-automation_>`_ of
this series we covered some background on requirements and tests for embedded
systems development, and introduced the idea of using `Jira`_ together with
the `Xray`_ and `R4J - easeRequirements`_ to manage this task.

The `second post of this series <next-steps-for-jira-requirements-and-tests_>`_
post decribed how to set up Jira with some minimal requirements and tests, and
how to verify that the API for uploading test results works.

Now we can go into more detail and demonstrate a real world example - a test and
requirement setup for `umm_malloc`_. I have worked on this memory manager for
embedded systems over the last decade or so, and have added an extensive set of
off-target unit tests during a reorganization of the library using TDD.

That means I have a set of tests already - and if your team is using TDD they
will be generating tests on a regular basis. If they are practicing TDD well,
then these tests are verifying new functionality or covering an error condition
that has produced a bug.

Either way, it's almost trivial to turn this daily work into requirements and
test cases in JIRA - let's get started.

.. TEASER_END

Which Tests Do We Already Have?
-------------------------------

The `umm_malloc`_ respository is set up for use with `adaptabuild`_ and has a
set of unit tests that are based on `CppUTest`_. These tests are organized
into suites. The suites are executed as a group when the CI ppeline  


As a reminder, this is not a step-by-step tutorial. The documentation teams
at `Jira`_, `Xray`_, and `R4J - easeRequirements`_ have done a great job
putting together guides and API references - so use them. There are a few
things you want to know before setting up a Jira project for requirements and
tests that will make your life easier.

The notes below are probably more confusing than they should be - I ended
up having to "explore" the UI more than I would have liked to get things
into the correct state.

#. Avoid customizing any issue schemas or workflows until you have had some
   experience with Jira in its default configuration. No matter what your
   current development workflow is, we are focusing on the bottom of the
   `V Model`_ - and we have to keep things simple.

#. Create a blank Company Managed project, not Team Managed if you want 
   access to issue schemas and workflows. Jira has a number of bundled project
   templates to choose from, but I'm not sure that any of them are
   really set up for requirements management.

   The easeRequirements application sets up new issue types for requirements,
   but they are not easily available to Team Managed projects, so stick
   with COmpany Managed for now. 

#. Use the `easeRequirements default configuration`_ for requirement types.
   There is a setup assistant in the "Getting Started" section of the Ease
   Requirements app menu. It sets up 4 basic issue types and I suggest you
   stick with them for now. You can also open your JIRA instance setting
   menu and navigate to Issue Types menu and add the following types:

   - Customer Requirement
   - Functional Requirement
   - Non-Functional Requirement
   - Test Case

   You also need to specify a Folder issue type for organizing requirements. The 
   docs say to avoid "Epic" so I created a new issue type called "Requirement Folder"
   to make its purpose clear.

#. Open your JIRA instance setting menu and navigate to Issue Type Scheme. Create an
   Issue Type Scheme called "Requirements" and pull in the 4 basic issue
   types for requirements plus the "Requirements Folder" type. Assign this scheme
   to your Jira project that you will use for requirements.

   I suggest keeping a separate project for requirements, depending on
   how many products you have and the commonality between them, you might have
   one project for all requirements, or you can split them up. For now
   stick with one project for all requirements until it's a problem.

#. In your Requirements project, consider editing the Issue Layout and removing
   all the fields that are not relevant for requirements. For example, Priority
   and Start Date don't make much sense for requirements.

#. Create a separate project for your tests, test sets, and test plans. Create
   an issue Type scheme that includes:

   - Test
   - Precondition
   - Test Set
   - Test Plan

   Do not include Test Execution as an issue type, we probably want a separate
   project for test executions because that's typically a lot of data and often
   makes sense to be separated by product or even project.

#. In the Requirements project, go to the Project Settings and then to the
   Xray Settings. Under the Test Coverage tab, move the 4 Requirement Types
   to the Coverable Issue Types. This is needed to allow the Xray Test Coverage
   report to work.

We don't really want to get into heirarchies of requirements until we have
a good understanding of how all of this fits together, but we will cover it
in another article.

I've created the following artifacts in the `public instance of Jira`_ for this site.

=========== =====================================================================================================
Item        Link
=========== =====================================================================================================
Requirement `HelloWorld default value after Initialization Requirement <https://fixitinfirmware.atlassian.net/browse/REQ-1>`_
Test Case   `HelloWorld default value after Initialization Test Case <https://fixitinfirmware.atlassian.net/browse/TEST-1>`_
Test Set    `HelloWorld Test Set <https://fixitinfirmware.atlassian.net/browse/TEST-2>`_
Test Plan   `HelloWorld Test Plan <https://fixitinfirmware.atlassian.net/browse/TEST-3>`_
=========== =====================================================================================================

Upload Test Execution Results
=============================

Now that we have the groundwork in place for learning more about Requirements and Testing
using JIRA, we can once again do the simplest thing possible to prove that we can upload
a test result.

I'm going to skip the steps where we make an actual Python class library and a pytest suite
for it. Let's assume for now that we have these in place and need to upload a successful test run.

We are using Xray Cloud, which only supports the `Xray JSON Format`_. The Server and DataCenter
installs support many other formats, but we will stick with Xray JSON for flexibility.

The minimal JSON file for uploading a test execution result looks like this:

.. listing:: Requirements_And_Tests/HelloWorldTestResult.json

Note that for the JIRA Cloud Xray Plugin, the correct endpoint base URL is https://xray.cloud.getxray.app/api
and you will need to create a completely separate access token from the one you use to
connect with your Jira instance. The Xray token will have ClientID and ClientSecret fields so that
the Xray API knows which Jira instance the API call is for.

The minimal Python code for uploading a test result looks like this:

.. listing:: Requirements_And_Tests/PostTestResult.py

Of course you will substitute your own credentials and use your own instance of Jira.

You can have a look at 
`REQ-1 (HelloWorld default value after initialization) <https://fixitinfirmware.atlassian.net/browse/REQ-1>`_
on my Jira instance
and see that the Test Case linked to the Requirements was executed and it passed. 

Of course, this is just a toy example. All it proves is that it is possible to
do the simplest possible type of test and requirement management with Jira,
Xray, and easeRequirements.

More to Come
============

In the next article, we will go quite bit deeper and set up the requirements
for `umm_malloc`_, and then build and run the test suite using GitHub actions. We
will extend the existing action for the project to upload the test results to
our Jra instance.


.. _`public instance of Jira`: https://fixitinfirmware.atlassian.net
.. _`umm_malloc`: https://github.com/rhempel/umm_malloc

.. _Atlassian: https://www.atlassian.com/
.. _Open Source Cloud Subscription: https://www.atlassian.com/software/views/open-source-license-request
.. _Jira: https://www.atlassian.com/software/jira
.. _Xray: https://marketplace.atlassian.com/apps/1211769/xray-test-management-for-jira
.. _R4J - easeRequirements: https://marketplace.atlassian.com/apps/1213064/easerequirements-requirements-management-for-jira-r4j

.. _Xray Terms and Concepts: https://docs.getxray.app/display/XRAYCLOUD/Terms+and+Concepts

..  _Xray JSON Format: https://docs.getxray.app/display/XRAYCLOUD/Using+Xray+JSON+format+to+import+execution+results
.. _easeRequirements default configuration: https://easesolutions.atlassian.net/wiki/spaces/REQ4J/pages/5406896/easeRequirements+Installation#Project-Creation-Template

.. _Automate the Boring Stuff With Python: https://automatetheboringstuff.com/
.. _V Model: https://en.wikipedia.org/wiki/V-model 

.. _EARS syntax: https://alistairmavin.com/ears/
.. _V Model: https://en.wikipedia.org/wiki/V-model 

.. _Jira REST API Authentication: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
.. _Jira Cloud REST API: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#version

.. _Perforce: https://www.perforce.com/ 
.. _Jazz: https://jazz.net/
.. _DOORS: https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/doors
.. _HPQC: https://www.opentext.com/products/application-quality-management
.. _Wikipedia page for Requirements analysis: https://en.wikipedia.org/wiki/Requirements_engineering_tools

.. _requirements-tests-and-automation: link://slug/requirements-tests-and-automation
.. _next-steps-for-jira-requirements-and-tests: link://slug/next-steps-for-jira-requirements-and-tests

.. _adaptabuild: https://github.com/rhempel/adaptabuild
.. _CppUTest: http://cpputest.github.io/index.html
