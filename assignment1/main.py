'''
1. Implement an algorithm which takes as input the parity-check matrix H returns you the generator matrix G. 
Assume systematic coding;
2. Implement loopy belief propagation decoding algorithm for LDPC code; use the ecient approach described
above to compute the messages from factors to variables; implement parallel and sequential schedules and 
dampened updates. We will assess the eciency of your implementation during grading (for example it is not 
recommended to use nested loops during one iteration of the decoder). Make a picture which illustrates the 
decoding process (see ﬁg. 1 for an example);
3. Experiment with di↵erent message passing schedules and dampening coecients; in particular plot the fraction
of stabilized beliefs vs. the iteration number (average the results over several runs); estimate the inﬂuence 
of the message passing schedule and the dampening coecient on the running time;
1Note that on the seminar we obtained exactly the same formulas by applying Fourier transform to the convolution
(2) of vectors of length two.
4. Consider two quality measures of a code: the probability of error in at least one bit of a block (p(ˆ e 6= e))
an dthe mean probability of error in one bit ( 1 nPn i=1 p(ˆ ei 6= ei)). Implement an estimator of these
two probabilitiesby Monte Carlo simulations (generate a dataset of error vectors e (ei = 1 with probability q), 
compute all syndromes s = He, and reconstruct the error vector ˆ e using your decoder);
5. Estimate the block and bit error probabilities for di↵erent values of the code-word length n, code rate r, 
probability of inverting a bit in the channel q, and mean number of ones in a column of the parity check matrix j. 
In particular, analyse the following situations: • The Shannon’s theorem deﬁnes the channel capacity as the maximal 
rate of the code which still allows for reliable transmition. Check how the code quality measures change when you 
change the code rate r from the minimal value to the channel capacity (we recommend to ﬁx the code-word length n in 
this experiment). • The Shannon’s theorem suggests that the code quality improves with the increase of the code-word 
length n. Check this statement on practice. • One of the Shannon’s theorem colloraries claims that a random parity-check 
matrix H yields a high-quaility code. In particular, the code quality should improve with the increase of the mean number 
of ones in a column of the parity-check matrix j. Check this claim for LDPC codes (consider several values of j, starting from 3).
6. Report all the conducted experiments in one PDF ﬁle
'''