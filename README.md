# Tech Dev Google
Foundations of Programming Reach beyond the basics of coding with these curated resources for programmers who have completed 1-2 computing courses.
https://techdevguide.withgoogle.com/paths/foundational/

## Environment

All the programs are done in Python3 without any external libraries. 


## maxSpan.py
Consider the leftmost and righmost appearances of some value in an array. 
We'll say that the "span" is the number of elements between the two inclusive. 
A single value has a span of 1. Returns the largest span found in the given array. 
(Efficiency is not a priority) 

maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

## strSplosion.py
Given a non-empty string like "Code" return a string like "CCoCodCod".

## subSeq.py
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
