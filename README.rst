README
======

It seems that the key to doing well on the GRE's Quantitative section to be able to do mental math quickly.
This is a program that I made to practice mental math.

This program asks math questions in several forms that are useful for the GRE.
These questions use random numbers (within some specified range) and show you the solution, as well as hints. 

To make it more fun, the type of question is random, too.
You can specify the relative frequency of different question types in the code.

Question types include:

* Arithmetic
* Squaring numbers
* Factorials
* Basic combinatorics (n choose k)


An example of a training session looks like:

::

    GRE MATH PRACTICE
    =================

    Question 1:
    
        What is 4*19?
        
        >>> 76
        
        Correct!

    Question 2:
    
        What are the factorials smallest to largest of 115? Input as a list ([x,y,...]).
        
        >>> [5, 23]
        
        Correct!

    Question 3:
    
        What is 26^2?
        
        >>> 676
        
        Correct!

    Question 4:
    
        What is 27*5?
        
        >>> 27*5
        
        Are you trying to cheat?

        What is 27*5?
        
        >>> 136
        
        Incorrect! Answer is 135
                
        ***Hint: Divide by 2, then multiply by 10


	SUMMARY
	=======
		Correct:       	3 / 4
		Total time:   	40 seconds
		Average time: 	10 seconds
		Slowest question was question 4 (18 seconds)

Adding New Questions
--------------------
If you wish to add new questions, follow the following steps:

1. Create a function that returns a dictionary fo the same form as the
   other questions
2. Make a lambda function for that function to fill in the specific
   parameters (if there are no parameters just pass the function handle
3. Add your function with a relative frequency to the
   :code:`questionsAndFrequencies` variable in main

Setup
-----

1. Clone the repository.
2. Install dependencies in the requirements (just NumPy)
3. Run the quizzer with ``python main.py``
    * You can use ``--num_questions`` or ``-n`` to set the number of questions


