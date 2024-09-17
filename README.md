# AccuKnox-Assignment

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


Answer:- By default, Django signals are executed synchronously. This means that when a signal is triggered, the connected signal handlers (receivers) are executed immediately, within the same thread, before the flow of the program continues.

Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer:- Yes, Django signals run in the same thread as the caller. This means that when a signal is emitted (for example, via a model's post_save signal), the signal handler is executed in the same thread that triggered the signal.
To conclusively prove this, we can use Python's threading module to show the thread identity of both the caller and the signal handler.

Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer:- By default, Django signals do run in the same database transaction as the caller. This means that if the caller's transaction fails and is rolled back, the signal handler’s effects will also be rolled back, as both are part of the same transaction.


