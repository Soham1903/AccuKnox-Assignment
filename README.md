# AccuKnox-Assignment

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
Answer:- By default, Django signals are executed synchronously. This means that when a signal is triggered, the connected signal handlers (receivers) are executed immediately, within the same thread, before the flow of the program continues
