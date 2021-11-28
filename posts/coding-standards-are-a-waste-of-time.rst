.. title: Coding Standards Are A Waste Of Time 
.. slug: coding-standards-are-a-waste-of-time
.. date: 2021-11-27 12:00:00 UTC-05:00
.. tags: maintenance, code
.. category: Roles
.. link: 
.. description: 
.. type: text
.. status: draft

.. image:: /images/accent/GeneKranzAtConsole.thumbnail.jpg
    :alt: https://history.nasa.gov/SP-4223/p118.jpg
    :align: right

You've been working for hours to figure out why the system you are
debugging only fails very occasionally. When you figure out that
it takes about 25 days of continuous run time for the failure to
occur, and it's happened at 4 different sites now, you get a
spidey sense that it might be related to a timer. You pull out
your phone and fire up Free-42 (because you like RPN calculators)
and do the math for a 1 msec timer interval and figure out that
a 32 bit unsigned int should be good for about 50 days ...

When you find the place where someone did a bit of math with the
clock using signed instead of unsigned values, you say "I wish
that we had a coding standard to catch this". Said nobody. Ever.

What you really needed was a developers guide for this project, a
test-driven development mindset, and a review process that could
work together to have a better chance at catching the problem.

If you take a few minutes and Google "are coding standards useful"
you will get many articles and blog posts promoting the same basic
benfits:

- The code will be easy to read
- The code will be easy to understand
- The code will be easy to maintain
- The code will be easy to debug

This is exactly the kind of fluff that management likes to read
after yet another difficult project delivery. Sometimes consultants
are brought in to review the development process and comment on the
lack of a coding standard (among other things). If only we stuck
to a coding standard our problems would go away.

The thing is, a coding standard is the easiest document to write
and to have meetings about. Everyonce has an opinion about how to
write pretty code, and how varaibles and functions should be named,
and whether to use camel-case or underlines to separate words.

But is the coding standard really going to fix things?

But Coding Standards Make Reading Code Easier
---------------------------------------------

To be fair, it *is* actually a little easier to read well-formed
code, but that's something you can fix in a few minutes with any
number of code formatting utilities. You can fix up most naming
problems with a decent editor. But you can't make anything more
complex than a toy example easier to understand, maintain, or
debug just by having a coding standard.

It feels good to write and read a nicely formatted block of code
where the names all make sense, the flow is clear, and the comments
explain the thinking behind the hard parts.

Now multiply that by a few hundred files and pretty soon you are
in the 20-50 kloc range - here's where the time you and your team
discussed the number of spaces to indent a block or enforcing only
one exit point per function was wasted. You would have been better
off working on a project level design and developers guide.

But Coding Standards Make Understanding Code Easier
---------------------------------------------------

Sure. For projects with a hundred or so lines of code. Do you
really think that your coding standard is the one thing that is
keeping new team members from understanding how your interrupt
domain functions buffer data so the background task can process
it when it's needed? Or how you guarantee that time critical
hardware updates can run durung garbage collection cycles?

It doesn't matter if the code is easy to read if the system is
hard to understand. That's why there are Cliff's Notes for topics
like The Great Gatsby and Differential Equations.

It's very helpful to have a relatively short document to give you
a detailed guide to the technical challenges the system is
designed to solve as wells a developer's guide that explains
how those challenges are solved.

But wait. Isn't writing a Design Guide and Developer's Guide
exactly what we are *not* supposed to do anymore? Doesn't Agile
prefer working code over documentation? Shouldn't we avoid doing
Big Up Front Design (BUFD)?

Maybe, yes, and yes. I'm no fan of BUFD - unless it's for a
relatively small piece of code where you know all the design
constriants and requirements and you have good acceptance criteria
and your team has written some variant of this code more than
once or twice.

For any complex project that's going to run for a few quarters
or years there is no way to think ahead to all the problems or
to find a process to eliminate risk. And that's why you and your
team should spend your time writing Design Guides and Developer's
Guides as you go. Take time in each sprint to update these
guides with new knowledge for the project.

For long-running and complex projects, your biggest enemy is
not the lack of coding standards. It's staff turnover and adding
more developers to the project. The loss of tribal knowledge
and the friction of onboarding new developers is what's going
to be the root cause of many issues that can be avoided if you
spend time writing great guides.

But Coding Standards Make Maintanance and Debugging Easier
----------------------------------------------------------

A coding standard might make the *mechanics* of maintaining
code easier, but they sure don't help you find *where* to make
the changes to add features.

Debugging code is one of the hardest activities there is, and
a coding standard is not going to help with that either. There
are of course a few general rules that can be used to make it
easier for the compiler to tell you about a potential bug. And
there are static and dynamic code analysers that can point you
to dangerous constructs.

In my experience, this is completely backwards. And for full
disclosure I was a strong advocate for compile time and code
analysers to find potential bugs. I changed my mind when I
discovered Test-Driven Development (TDD).

Actually I discovered the TDD For Embedded Systems book by
James Grenning back in 2011, but I didn't really dig in and
*do* TDD until I refactored by umm_malloc project using TDD
in about 2018.

Then I wrote a non-trivial (2000 loc) feature extension for
another project using TDD. It worked pretty much the first time we
integrated it into the codebase running on our embedded target.
When we reflected on how TDD improved our development process
I realized that *I never had to use the debugger*. Ever. Not
even once.

Long story short, the bit about debugging being easier when
you have a coding standard is simply untrue. Easier maintenance
is also a myth - you still have to know where to change the
code, or how to plug a new feature in.

What Can We Do To Improve Outcomes?
-----------------------------------




Debugging is
much easier when you follow your design and developer's guides
and you use TDD to avoid 
That was an incredible breakthrough for me, and it has changed
how I think about writing complex system


https://www.amazon.com/Driven-Development-Embedded-Pragmatic-Programmers/dp/193435662X
https://www.cliffsnotes.com/
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjW09jMw7n0AhXyxIsKHTtGCcEQFnoECB4QAQ&url=https%3A%2F%2Frepository.tudelft.nl%2Fislandora%2Fobject%2Fuuid%3A646de5ba-eee8-4ec8-8bbc-2c188e1847ea%2Fdatastream%2FOBJ%2Fdownload&usg=AOvVaw36uiug_akx2HfAXBP92tdi
https://arxiv.org/pdf/2007.08978.pdf
https://www.jstage.jst.go.jp/article/transinf/E98.D/7/E98.D_2014EDP7327/_article

Hands up for anyone who *knows* their company mission statement.

In many organizations, the mission statement is laid out by top level
leadership, sometimes with input from departments or individuals. It tends
to be a general and somewhat fluffy set of words that could apply to
just about any organization. And that makes most mission statements
forgettable.

But that doesn't mean your maintenance team should not have a mission
statement! Your job together with your team is to come up with a
statement that reflects how you want to be seen and heard within
the organization moving forward.

One step towards improving your team's visibility is to have a 30-60 minute
workshop to identify your key responsibilities and accountabilities. Don't
work on your misison statement yet - just keep that list up on a
whiteboard and make sure that it accurately reflects the team's
purpose. As you do your work, feel free to update the whiteboard by
adding, consolidating, or removing items. Within 2-4 weeks the lists will
be boiled down to a few items that will represent your team's "reason
for being" - that's the core of your mission.

Maintenance engineering can be extremely demanding because
your work impacts not only future production but also every unit that
has ever been produced and sold. You could be working on tasks
as varied as reducing manufacturing cost, adding a new feature, or
making a fix that can be applied in the field. In rare cases your team
will have to make a call to stop production or even recall a product.

How do those high level tasks fit into your company's mission statement?
They probably don't - and that's why you and the team need to have one
that feels authentic and relevant for you, while still supporting the
overall company mission.

Mission statements that are authentic are very hard to come by, so why
not take inspiration from an existing statement and modify it (if needed)
to be relevant for your team?

Two of my personal favorites are:

    - "Tough and competent"
    - "Failure is not an option"

    -- Gene Kranz (Apollo Flight Director)

Almost every engineer has at one time or another watched Apollo 13 and
has reflected on their personal work. If you haven't watched it recently,
please make some time to do so, or look up any documentary on the
Apollo program. Maybe bring it up in your next team meeting and ask
for input on an engineering heavy documentary that you can all watch.

Then spend 30 minutes or so on a team reflection to gather input on
what is the most relevant thing the team can do in the next 2-4 weeks
that makes them feel proud of what they are doing.

... but we DID fail - now what?
-------------------------------

I just said that *Failure is not an option* is one of my guiding star
statements. At LEGO we have a similar one - *Only the best is good enough*.

As much as I admire these statements, they come with a downside. They
may set up the organization to believe that failures will not happen, or
support a culture of not releasing a product until it's perfect and
complete.

Of course these are relevant statements for space flight, where cost and
quality are in step with each other. In consumer and commercial goods,
you *will* have failures in design, production, software, and process - and
they will almost always be coupled with schedule and cost pressure or
incorrect assumptions.

Your job as part of the maintenance team is to be prepared to address
these failures, and to do so professionally. That means making sure that:

  #. You value facts over guessing
  #. You fix the root cause and not the symptom
  #. You communicate clearly in a timely fashion

This is where *Tough and Competent* comes in. You and the team need to
be competent in gathering facts and getting to root cause. Then you
need to be tough in challenging assumptions and reporting your findings
and recommendations.

What you and your team discover, how you solve the problem, and the
way you communicate it up the chain will have a huge impact on your team's
visibility and credibility. Never waste the opportunity.

Managing engineering failures that get escalated to senior leadership
is a real challenge, and I'll review personal stories of failure and
success in future posts.
