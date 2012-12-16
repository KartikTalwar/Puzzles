## Median of 2 sorted arrays

There are 2 sorted arrays A and B of size n each. What's the complexity of an efficient algorithm that finds the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n)? 

**Answer** : log(n)

### Explanation

Let ar1 and ar2 be the input arrays. 

- Calculate the medians m1 and m2 of the input arrays ar1[] and ar2[] respectively. 
- If m1 and m2 both are equal then we are done  return m1 (or m2) 
- If m1 is greater than m2, then median is present in one of the below two subarrays. 
  - From first element of ar1 to m1 (ar1[0...|_n/2_|]) 
  - From m2 to last element of ar2  (ar2[|_n/2_|...n-1]) 
- If m2 is greater than m1, then median is present in one of the below two subarrays. 
  - From m1 to last element of ar1  (ar1[|_n/2_|...n-1]) 
  - From first element of ar2 to m2 (ar2[0...|_n/2_|]) 
- Repeat the above process until size of both the subarrays  becomes 2. 
- If size of the two arrays is 2 then use below formula to get the median. 

Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2 

