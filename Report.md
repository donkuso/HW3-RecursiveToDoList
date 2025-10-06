# Report
## Olivia Donkus

**Reflection**
This coding assignment was challenging at first because I was still wrapping my head around how recursive lists work. Understanding how nodes reference each other and how recursive calls traverse the list took some trial and error. Once I started to visualize how each function call represented a smaller version of the same problem, things clicked. Writing functions like conditional_str() and filter() helped me see how recursion can replace loops in linked list operations. Overall, the assignment definitely served its purpose — it forced me to think recursively and understand how data structures can be manipulated through self-referential logic.

**Filter Algorithm Explanation**
The filter() algorithm takes in a condition/lambda that returns true/false. The boolean value is used to filter the data. If this boolean value is true, a new Node containing the same data is created and recursively calls filter() on the next node, linking the result. If false, it skips the current node and directly returns the result of recursively filtering the next node. The base case occrus when there are no more nodes. The process builds the linked list containing only the nodes that satisfy the condition.

**Self-grade**
I would give myself a 90%. I believe I demonstrated a strong understanding of recursion and was able to get the methods working correctly. 
