# Q&As on the Project Description
## As you mentioned 6 minutes per script of MapReduce Algorithm and if mine is taking 7-8 minutes on my x86 laptop would it still finish under 6 minutes on the test computer that will be used to evaluate our scripts?
We couldn't comment on this since each student's implementation may vary. The MapReduce algorithm should run very fast if implemented properly because the nature of MapReduce is distributed computing.
## The format mentions order is not important for q1, does this mean the following list of inverted indices are equally valid:
```
Hotels & Travel ['01OmT3PXceLBRsYyWdummy', '023Lc6yStQnKuqymEdummy', '03PyMX1yFb_VYgPw4dummy']
Hotels & Travel ['023Lc6yStQnKuqymEdummy', '01OmT3PXceLBRsYyWdummy', '03PyMX1yFb_VYgPw4dummy']
```
Answer: Yes
## Are we allowed to use multiple reducers for Q2, or can we only use one?
Please strictly follow the implementation instructions. Your scripts should be run using the command presented in the project description.

## How should we be able to gauge whether our scripts will complete in time on the computers used to evaluate the submissions? E.g. on my computer, my current solution for Q3 finishes in ~1:42, but it was done on a (relatively new) PC with an SSD, 32GB of RAM and 8GB of RAM allocated to WSL2, and with an Intel® Core™ i5-11500H Processor. However, I don't know how powerful the computers used for submission will be, so I don't know if my solution will pass or fail during submission evaluation.
The machine used for evaluation has 40 cores and 180GB of memory. If your scripts can give the output within the time limit on a regular x86 laptop, you don't need to worry about the time limit. 
By the way, the time limit is for filtering out solutions that are not based on MapReduce. The MapReduce algorithm should run very fast if implemented properly because the nature of MapReduce is distributed computing.

## How are the categories supposed to be differentiated on? Is it sufficient if I split a certain category based on a comma delimiter? 
```
For example in the dataset there is an entry like this

"categories":"Elder Law, Wills, Trusts, & Probates, General Litigation, Divorce & Family Law, Professional Services, Estate Planning Law, Criminal Defense Law

Is it correct that "& Probates" is an valid category in this case?
```
Answer: Please assume categories are comma-separated. Therefore, "& Probates" is a valid category.

## Does the output for question 2 need to be sorted? For example, sorted by month, or sorted by proprotion.
The order does not matter.

## For Project 2, can we assume that the number of reducers will always be 1 (i.e. -D mapreduce.job.reduces=1, which is the default), and write our programs such that they work with this assumption but might not work if the number of reducers is more than 1?
Please test your solution using the Docker image (eecs4415/hadoop) we provided. We will use the same environment for evaluation.
