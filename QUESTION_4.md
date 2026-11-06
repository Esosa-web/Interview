# Question 4

This one is a discussion, not code. Sketch on the whiteboard or in a file if that helps.

The orders service has taken off:

- There are 20 million customers and about 5 million new orders a day.
- The paid total from Question 1 now shows as "lifetime spend" on every customer's account page. Finance also uses it for monthly reports.
- Customer details come from a separate customer service, owned by another team. Every account page needs them, and that service has occasional outages.

**Task:** talk us through how you'd design the orders service for this. In particular:

1. How and where you'd store orders.
2. How you'd calculate the paid total so the account page stays fast.
3. What the account page does when the customer service is down.

We're more interested in the trade-offs you weigh than in one right answer. Ask us anything you'd need to know.
