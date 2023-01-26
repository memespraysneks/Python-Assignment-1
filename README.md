

Welcome to Assignment 1, in which you will explore asymptotic analysis of algorithms, through empirical means.  For science!  (Lab coat, and weird-coloured liquids, are optional.)


# What You Start With

There are three files of code provided.

* `sorting_routines.py` contains four sorting functions, named `sort_alpha` through `sort_delta`.  These can, of course, be imported from other files, including the measuring code that you will have to write.
* `data_generators.py` contains two different functions for generating random data to be sorted.  You are expected to use these generators in your measurements, not to create your own.  I have my reasons.
* `test_sorts.py` contains unit tests to prove that these sorting functions do actually sort things in order.
    * tests with 'fixed' in the name should run the same way every time they are run, because they supply a seed to the randomness
    * tests with 'random' in the name do not supply a seed, and so run differently every time, which makes them hard to reproduce, but they give extra coverage
    * tests with 'numb' in the name test on arrays of integers
    * tests with 'invoice' in the name test on arrays of invoices

# Task Description

For each of the sorting routines provided, you will need to

* **measure** the average time at various input sizes
* create a **visualization** of your measurement results
* make a **hypothesis** about the asymptotic performance of the sorting routine
* form a reasonable **conjecture** based on that hypothesis


## Measuring

In this task, you are trying to answer the question "How long does this sorting routine actually take to run, at various input sizes, on my computer?".

You need to feed various input sizes into the generator, save that generated data, feed that into the sorting routine, and time how long the sorting routine takes.  This should be run many many times, at many different input-sizes (**at least 7 different input-sizes**).  Use the `create_numbers` generator from `data_generators`.

So, you should write (and run) some code that loops across various input sizes and does the measuring, and then output some statistics.  You could include various statistics, but at least give us the mean and median time, and the standard deviation, per-run, for each of the input-sizes that you try.

I'm including an image of what my testing code does for a sorting routine that is not included in this assignment.  Yours doesn't need to be exactly the same, but I hope it gives you some ideas, as would the labs from week 2 and week 3.

Once you have the bugs worked out, you should do a run that takes a long time, like at least an hour, so that you get data at larger sizes than you otherwise would.  Set it up, go for bubble tea or a jog or a movie or whatever.  Don't do other things on the same computer while the final data run is running, it could mess up the results, right?

Screenshot your raw output.

### Hint

Most of the sorting routines, it's fine to just do input sizes like `[16, 32, 64, ...]` and so on, until it's large enough that the thing takes long enough that you run out of patience.  That should get you enough data points.  But on one of the sorting routines, this powers-of-two approach will probably not generate enough data, because it gets really slow after only a few sizes, and your computer will just get stuck (mine did).  So for that one, I did numbers like `[10, 20, 30, 40, ...]`.  That way I got measurements at more than 10 different values of n, which helped for later stages of the assignment.


## Data Visualization

For each sorting routine that you tested (and there should be 4), you should generate a table of results, and a graph.

For the table, I'd suggest throwing it into Excel or something like that.

You'll need to clearly annotate the graph, including marking the axes, and highlighting the data points, and connecting the dots with a line.

If you want to do this with some fancy software, that's great.  If you don't know how to use any software to make nice charts (I admit, I don't), you can do it by hand on paper and take a photo.  Make sure it's legible.

You should have one graph per sorting routine tested.

Possible consideration: should the axes be linear?  Logarithmic?  How do you present this data so that it's comprehensible?


## Hypothesis

> Warning, in this section I need to talk about both functions-as-in-Python as well as functions-as-in-math.  I'll use "routine" to mean "functions-as-in-Python", and "mathematical function" for, well, math functions.  I hope that helps keep the confusion to a bearable level.

For each sorting routine, based on the data, try to tell me...  what is the asymptotic running time of this sorting routine?

That is, give me a mathematical function that approximately predicts how long the sorting routine will take for various sizes.

I'm looking for a little more detail than big-Oh notation...  I'd like to know the linear scaling as well.  For example, instead of answering "It looks like `O(n^2)` running time", you could answer something like "It looks like it takes around `14 * n^2` seconds running time".  You're trying to find a mathematical function that is pretty close at several size levels, especially the largest sizes that you tested.


For each sorting routine, add the curve for the mathematical function you came up with to your graph.  Again, you can do that with software, or you can just bodge it by hand.  Even if you did the data visualization step with software, you could do this step by importing into MS Paint or whatever and drawing your estimate with crayon-or-equivalent.  Just something to show how well your estimated mathematical function fits.

### Hint

Most of the sorting routines, the mathematical function is along the lines of `time = n^p * s`, where you have to play with the values of `p` and `s` to get the right result.

Personally, I threw all my data into Excel (or actually Google Sheets because I'm too dumb to figure out how to use the BCIT license for Excel), with values of `n` in column G and values of `time` in column H, and wrote a formula like `=pow(G3,$I$1)/H3/$J$1` so that I could put my `p` hypothesis into `I1`, and put my `s` hypothesis into `J1`, and then mess around until I got values that worked out.

BUT, WARNING, this will not work out for all four of the sorting routines.  Why not?


## Conjecture

Now.  For each sorting routine, tell me the following:

Suppose you were going to just run this sort on a single array for 48h on your computer.  Forty eight hours non-stop!  How large an array could you sort in that time (probably)?

48 hours is `2 * 24 * 60 * 60 = 172800` seconds, by the way.

I want to see an actual estimate (like "For sort_alpha, in 48 hours, my computer could probably do array of size around 11,324,620,965,800").

I also want to see just a tiny bit of algebra to justify this claim.  How did you turn your results from the Hypothesis section into your answer here?

I don't really care about exactly the number.  I care that it is the right order of magnitude (right number of digits), and that your reasoning is basically sane.


# Deliverables

I want this whole thing wrapped up in a PDF.

Your name and student number should be somewhere visible on the first page, because sometimes when I download from D2L the filenames get all screwed up, so I want to be able to untangle that if necessary.

First your measurement code (don't bother including all the code I gave, just give me the new code you wrote).

Then your screenshot of raw output.

Then your table of results for all the sorting routines.  Give that its own page, please.

Then your graphs, one per page.  As mentioned above, graphs should include the facts of your actual measurements, as well as your estimated large-scale trend curve.

Then your hypotheses and conjectures, for all 5 sorting routines.  These can go together (i.e. do both for sort_alpha, then both for sort_bravo, etc).

## Submission

There'll be an Assignment dropbox on D2L.



# Grades

You will receive one of four grades for this assignment:

* Unsatisfactory, 0%
* Pass, 55%
* Satisfactory, 75%
* Exemplary, 100%

You will receive the highest grade listed below for which I feel that you completely qualify (or, if you qualify for none of them, then Unsatisfactory, of course).


## Pass

Your submission must be a PDF.

Your measuring code looks plausible, and contains no clear errors that would result in totally utterly wrong data (for example if your timing code is generating 0 for most times, that would be pretty bad, or if you're timing the generators instead of the sorting routines, that'd be pretty bad, or you're not running the generators at all, etc etc).

You have screenshots of raw terminal output.

You have clear, legible, cleaned-up tables for all four of the sorting routines, with at least 7 different sizes measured for each.  The tables should show the mean time for each, the median, and the standard deviation.  Make sure the tables are readable; if you can fit them all on one page that'd be nice, but readability is more important.

You have clear graphs for each of the sorting routines, with labelled axes.  Each graph should have two functions graphed: one is the data you measured (this will probably be a jaggy line), and the other should be the graph of your corresponding hypothesis from the Hypothesis section (that graph should probably be a smooth curve).  I want to be able to quickly eyeball-compare them.  One graph per page, so that they can be nice and big and clear.

At least two of your four hypotheses are roughly correct.  All four hypotheses are present, and all four are at least sane (i.e., you tried).


## Satisfactory

All of the requirements of the previous level, plus....

You have good Conjectures in the Conjecture section, with at least a few sentences of justification for each.

At least three of your four hypotheses are roughly correct.  All four hypotheses are present, and all four are at least sane (i.e., you tried).

## Exemplary

All of the requirements of the previous level, plus....

Your measurement code is better than what I showed in class.  That is, it takes care of more possible things that could go wrong.  Please add a page to your PDF explaining what possible-problems you are attempting to solve, and how you are solving them.

Your Hypothesis section, for all four sorting routines, contains two independent arguments: one based purely on the data, and one based purely on the code.  If you cannot get these arguments to agree, use the based-on-data argument 

All four of your hypotheses are correct.

