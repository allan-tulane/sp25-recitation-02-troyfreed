# CMPS 2200  Recitation 02

**Name (Team Member 1):** Troy Freed 
**Name (Team Member 2):** Mike Baron

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

for function 1: f(n) = 1 for base case where a=1, f(n) = 1 = n^(log_b a) = 1. In this case it is case 2 applies & W(n) = Theta(logn) for any a > 1, say a = 2 and b = 2, f(n) = 1 which is dominated by n^1 as n grows larger. here it is W(n) = Theta(n) 

for function 2: f(n) = logn for a > 1, when observing f(n) = logn and n^(log_b a) we can see that as n grows, f(n) grows logarithmically, which is slower than n^(logb a) that grows pollynomially So, f(n) is dominated by n^(log_b a) for the same example, a = 2 and b = 2, logn < n^1 as n grows. this means W(n) = Theta(n^log_b a) whic for this example is Theta(n) 

for function 3: f(n) = n for here, using example a=2 and b=2 again, f(n) = n which grows at the same rate as n^(log_2 2) since that = n^1. This means that case 2 applies W(n) = Theta(nlogn)

here is an example set of results: n=2, f(n) = 1 => 3, f(n) = logn: =>3.0, f(n) = n =>4 n=4, f(n) = 1 => 7, f(n) = logn: =>8.0, f(n) = n =>12 n=8, f(n) = 1 => 15, f(n) = logn: =>19.0, f(n) = n =>32 n=16, f(n) = 1 => 31, f(n) = logn: =>42.0, f(n) = n =>80 n=32, f(n) = 1 => 63, f(n) = logn: =>89.0, f(n) = n =>192 n=64, f(n) = 1 => 127, f(n) = logn: =>184.0, f(n) = n =>448 n=128, f(n) = 1 => 255, f(n) = logn: =>375.0, f(n) = n =>1024

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

The work from recursive calls is roughly n^log_b a. When using the work_calc function there is f which is an extra step for the function. Asymptotic behavior depends on which function takes more work. If the extra function is n^c the asymptotic behavior will be dependent on n^log_b a if n^c is less work, but will be dependent on n^c if it is more work. In the case where c < \log_b a the recursive function dominates it making W(n) = O(n^log_b a). In the case where c > \log_b a the extra function dominates it making W(n) = O(n^c). In the case where c = \log_b a, the extra work and the recursive function are equal making them grow at the same rate. Because the problem size decreases at a factor of b each time, the recursion tree is log_b(n). Because you add the same amount of work at log(n) levels, W(n) = O(n^c log(n)).

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

The span is the longest case of dependent operations in a function. We assume there is a base case where S(1) = f(1), and that a = 2 and b = 2
Case 1: f(n) = 1, we have S(n/2) + 1. Because the problem gets split on every step it comes out to O(log(n))
Case 2: f(n) = log(n), when going through this recurrence you start to add up values like log(n) + log(n/2) + log(n/4)... when you continue this the result comes out to S(n) = O(log(n)^2)
Case 3: f(n) = n, when going through this problem the top level is n then because S(n/2) + n, it starts to look like S(n) = n/2 + n/4 + n/8... this creates a geometric sequence with a common ratio of 1/2 and the sum of the sequence being 2n. Because we ignore constants it becomes S(n) = O(n)
