# Interview exercise

Everything is already installed. Two commands:

    uvicorn main:app --reload   # run the app, then open /docs on port 8000
    pytest                      # run the tests

The session is two short questions on one small FastAPI app, about 50 minutes in total.

## Ground rules

- You're welcome to use documentation and search as you work. Looking things up is expected and isn't marked down.
- Please think aloud, and ask clarifying questions whenever something is unclear.
- Your reasoning matters more than getting the code perfect.

## Question 1

You're working on a small orders service. The starting code is in `main.py`: a FastAPI app and an in-memory list of orders.

**Task:** implement an endpoint that returns the total value of paid orders for a given customer.

Talk us through your choices as you go.

## Question 2

Your interviewer will point you to `QUESTION_2.md` when you're ready.
