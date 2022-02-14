.. title: Coding Standards Are A Waste Of Time 
.. slug: coding-standards-are-a-waste-of-time
.. date: 2021-11-27 12:00:00 UTC-05:00
.. tags: maintenance, code
.. category: Roles
.. link: 
.. description: 
.. type: text

.. image:: /images/accent/GeneKranzAtConsole.thumbnail.jpg
    :alt: https://history.nasa.gov/SP-4223/p118.jpg
    :align: right

You've been working for hours to figure out why the system you are debugging
only fails very occasionally. When you get good bug reports that show it takes
about 25 days of continuous run time for the failure to occur, and it's
happened at 4 different sites now, you get a spidey sense that it might be
related to a timer. You pull out your phone and fire up Free-42_ (because you
like RPN calculators) and do the math for a 1 msec timer interval and figure
out that a 32 bit unsigned int should be good for about 50 days ...

When you find the place where someone did a bit of math with the clock using
signed instead of unsigned values, you say "I wish that we had a coding
standard to catch this".

Said nobody. Ever.

What you really needed was a developers guide for this project, a test-driven
development mindset, and a review process that could work together to have a
better chance at catching the problem.

If you take a few minutes and Google "are coding standards useful" you will get
many articles and blog posts promoting the same basic benefits:

- The code will be easy to read
- The code will be easy to understand
- The code will be easy to maintain
- The code will be easy to debug

This is exactly the kind of fluff that management likes to read after yet
another difficult project delivery. Sometimes consultants are brought in to
review the development process and they comment on the lack of a coding standard
(among other things). If only we stuck to a coding standard our problems would
go away.

The thing is, a coding standard is the easiest document to write and to have
meetings about. Everyone has an opinion about how to write pretty code, how
variables and functions should be named, and whether to use camel-case or
underlines to separate words.

But is the coding standard really going to fix things? There is a hard truth in
software engineering that is often forgotten. Joel Spolsky summarized it very
neatly in Part 1 of `Things You Should Never Do`_:

.. epigraph::

  There’s a subtle reason that programmers always want to throw away the code
  and start over. The reason is that they think the old code is a mess. And
  here is the interesting observation: they are probably wrong. The reason that
  they think the old code is a mess is because of a cardinal, fundamental law of
  programming:
  
  **It’s harder to read code than to write it.**
  
  This is why code reuse is so hard. This is why everybody on your team has a
  different function they like to use for splitting strings into arrays of
  strings. They write their own function because it’s easier and more fun than
  figuring out how the old function works.

  - Joel Spolsky

Let's explore this a bit further ...

But Coding Standards Make Reading Code Easier
---------------------------------------------

To be fair, it *is* actually a little easier to read well-formed code, but
that's something you can fix in a few minutes with any number of code
formatting utilities. You can fix up most naming problems with a decent editor.
But you can't make a more complex module easier to understand, maintain, or
debug just by having a coding standard.

It feels good to write and read a nicely formatted block of code where the
names all make sense, the flow is clear, and the comments explain the thinking
behind the hard parts.

Now multiply that by a few hundred files and pretty soon you are in the 20-50
kloc range - here's where the time you and your team discussed the number of
spaces to indent a block or enforcing only one exit point per function was
wasted. You would have been better off working on a project level design and
developers guide.

But Coding Standards Make Understanding Code Easier
---------------------------------------------------

Sure. For projects with a hundred or so lines of code. Do you really think that
your coding standard is the one thing that is keeping new team members from
understanding how your interrupt domain functions buffer data so the background
task can process it when it's needed? Or how you guarantee that time critical
hardware updates can run during garbage collection cycles?

It doesn't matter if the code is easy to read if the system is hard to
understand. That's why there are `Cliff's Notes`_ for topics like The Great Gatsby
and Differential Equations.

It's very helpful to have a relatively short document to give you and your team
a detailed guide to the technical challenges the system is designed to solve as
well as a Developer's Guide that explains how those challenges are solved.

But wait. Isn't writing a Design Guide and Developer's Guide exactly what we
are *not* supposed to do anymore? Doesn't Agile prefer working code over
documentation? Shouldn't we avoid doing Big Up Front Design (BUFD)?

Maybe, yes, and yes. I'm no fan of BUFD - unless it's for a relatively small
piece of code where you know all the design constraints and requirements and
you have good acceptance criteria and your team has written some variant of
this code more than once or twice.

For any complex project that's going to run for a few quarters or years there
is no way to think ahead to all the problems or to find a process to eliminate
risk. And that's why you and your team should spend your time writing Design
Guides and Developer's Guides as you go. Take time in each sprint to update
these guides with new knowledge for the project.

For long-running and complex projects, your biggest enemy is not the lack of
coding standards. It's staff turnover and adding more developers to the
project. The loss of tribal knowledge and the friction of onboarding new
developers is what's going to be the root cause of many issues that can be
avoided if you spend time writing great guides.

But Coding Standards Make Maintanance and Debugging Easier
----------------------------------------------------------

A coding standard might make the *mechanics* of maintaining code easier, but
they sure don't help you find *where* to make the changes to add features or
fix bugs.

Debugging code is one of the hardest activities there is, and a coding standard
is not going to help with that either. There are of course a few general rules
that can be used to make it easier for the compiler to tell you about a
potential bug. And there are static and dynamic code analyzers that can point
you to dangerous constructs.

In my experience, this is completely backwards. For full disclosure I was a
strong advocate for compile time and code analyzers to find potential bugs. I
changed my mind when I discovered Test-Driven Development (TDD).

Actually I discovered the `TDD For Embedded Systems`_ book by James Grenning back
in 2011, but I didn't really dig in and *do* TDD until I refactored my
`umm_malloc`_ project using TDD in about 2018.

Then I wrote a non-trivial (2000 loc) feature extension for another project
using TDD. It worked pretty much the first time it was integrated it into the
codebase running on our embedded target.  When I reflected on how TDD improved
our development process I realized that *I never had to use the debugger*.

Ever. Not even once.

Long story short, the bit about debugging being easier when you have a coding
standard is simply untrue. Easier maintenance is also a myth - you still have
to know where to change the code, or how to plug a new feature in.

What Can We Do To Improve Outcomes?
-----------------------------------

The first thing we can do is take a look around us and have some hard
conversations about *why* we think a coding standard is so important, and
if so, does it need to apply uniformly to each and every project?

I'm going to argue that a coding standard is not nearly as important as a project level
Developers Guide - unless your department only works on variants of the same
codebase for all projects. I'll also ask you to recall all the hours you have
spent getting to a semi-done coding standard, giving up in the end because
you cannot get an agreement on something like allowing an early return out
of a function.

Next we can do a literature survey looking for actual (not anecdotal)
evidence of the benefit of a coding standard - even an industry standard one
like MISRA-C. Guess what? A `study at TU Delft`_ (a very well respected CS school)
and Les Hatton's paper on `Language Subsetting`_ using MISRA-C have shown that
the standard is not much better than random chance at catching faults. To make
matters worse, Hatton's earlier paper shows that there is a non-trivial chance
that fixing code to be MISRA-C compliant actually *increases* the risk of
introducing new and subtle bugs.

The third thing you and your team can do is start working in pairs or small
groups to break down your functional components into pieces that are
decoupled from the rest of the system, and that follow good software engineering
principles, like `Uncle Bob's SOLID`_ response to a reader's letter.

Finally, find a TDD evangelist in your team and take them off their
assigned tasks for a while. Let them float in a couple of teams and ask them
to coach developers in TDD. Make sure that your developers know the difference
between code *coverage* and code *correctness* - it's usually easy to write
tests after the code is done that prove code coverage. It takes a little
longer (at the beginning) to write code that makes failing tests pass, but
pretty soon the rhythm of writing a test, breaking your program, and then
writing code to make the test pass becomes natural.

Your new developers will be *much* more productive on your complex system
if they have read a good Developers Guide and understand the workflow for
adding features or fixing (hopefully rare) bugs. They won't need a Coding
Standard because you'll have a senior staff member coaching them for the
first few months, they will have a safety net of tests, and they will develop
a mindset that drives quality, attention to detail, and testability that a
coding standard simply cannot help with.

.. _Free-42: https://thomasokken.com/free42/
.. _Things You Should Never Do: https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/
.. _Cliff's Notes: https://www.cliffsnotes.com/
.. _`TDD For Embedded Systems`: https://www.amazon.com/Driven-Development-Embedded-Pragmatic-Programmers/dp/193435662X
.. _`umm_malloc`: https://github.com/rhempel/umm_malloc
.. _`study at TU Delft`: http://resolver.tudelft.nl/uuid:646de5ba-eee8-4ec8-8bbc-2c188e1847ea
.. _`Language Subsetting`: https://www.leshatton.org/Documents/MISRA_comp_1105.pdf
.. _`Uncle Bob's SOLID`: https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html

.. _`Big MISRA study`: https://arxiv.org/pdf/2007.08978.pdf
.. _`Coding Standard JAVA`: https://www.jstage.jst.go.jp/article/transinf/E98.D/7/E98.D_2014EDP7327/_article


