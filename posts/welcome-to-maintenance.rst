.. title: Welcome to Maintenance
.. slug: welcome-to-maintenance
.. date: 2021-01-05 12:00:00 UTC-05:00
.. tags: maintenance, resources, opportunity
.. category: Roles
.. link: 
.. description: 
.. type: text

Great news - the company you work for is doing relatively well considering the
global pandemic of 2020-2021 and you still have a job. Your team has made a
final release of your flagship product and the engineers are being assigned to
new projects. Just before the monthly all-hands, your manager schedules a 1:1
where he tells you that you are now going to be on the maintenance crew for the
project that your team has released.

Maintenance, sustaining, support - no matter what the word is, this is not
where you thought you would end up. Fixing bugs and adding features that were
dropped to meet the schedule is no fun and a dead-end.

Or is it?

In my experience the maintenance team performs a vital business function, and
it's a great time to really lean in and develop some of the skills that will
make you a much better embedded systems programmer. This is also an opportunity
to help your leadership team get a better idea of what is needed to support a
high-performing firmware maintenance team.

If the company you work for doesn't have a great culture around maintenance
after product launch in place, don't worry. You will have to do some extra
work to drive organizational change, but patience and solid data to back up
your ideas can kick-start the change journey.

First Steps
-----------

In your new role on the maintenance team it's important to take stock of 
the expectations on your team and the resources you have available.

When we talk about resources in a traditional project management
context, the first thing that comes to a PM's mind is budget, developers,
and and equipment. 

Before we go too far down this path, I'd like to ask you to deliberately
leave developers out of the resources category. The reason is simple - if
you need a bigger hard drive, you buy it. If you need more desks you can
move them from another department. Those are resources - people are not
resources. Please encourage your company to avoid calling developers
resources because it implies a 1:1 trade capability. We already know
that no two developers have the same capability or capacity, so let's
stop using the word resource for staff.

I'll suggest here that resources may also include:

- Product requirements (including features that are not yet implemented)
- Technical and user documentation
- Test plans and automated test systems
- Source code, CI/CD pipelines
- Any specially modified PCBAs or programming fixtures

Any artifacts that the team needs to build and support your product is a
resource, so identify and conserve them.

Technical Debt
--------------

Wait, you don't have some of these items, or they are at best incomplete and
outdated? Welcome to the reality of technical debt. Some projects have the
misfortune to run long enough that they get bogged down in technical debt and
end up cancelled. Other projects have a short enough run that the developers do
only what is absolutely needed to get the job done, and corners will be cut -
most likely in documentation.

Now is the time to meet with the development team (that you may have even
been a part of) and gather any artifacts that they still have. If
you're lucky there's a decent bug/feature list in a tool like JIRA and some
form of Wiki or Confluence site for the documentation.

Expect to spend at least a week or two getting these resources into useable
shape together with the rest of your team - and avoid falling into the trap
of doing any more actual coding until you are satisfied that you and the team
are prepared to look after the code properly.

In the next installment we'll talk about building a culture of quality
and accountability.
