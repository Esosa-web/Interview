# Question 2

Customer data lives in a separate service:

    GET {CUSTOMER_SERVICE_URL}/customers/{id}
      200  customer details (JSON)
      404  customer does not exist

Use `CUSTOMER_SERVICE_URL = "https://customers.internal"`.

**Task:** update your endpoint from Question 1 so it checks the customer exists, using `httpx`, before calculating the total.

The customer service team has given you these constraints:

1. Give up if a connection can't be made within 2 seconds, but allow up to 10 seconds for a response once connected.
2. Connections sometimes drop during their deployments, so retry failed connections up to 3 times.
3. If the service can't be reached, return a sensible error to our caller.

You're expected to use the httpx documentation at https://www.python-httpx.org as you go.

You don't need a real customer service running; we're interested in the code and your reasoning.
