<?php


/*

	It is possible to write five as a sum in exactly six different ways:

	4 + 1
	3 + 2
	3 + 1 + 1
	2 + 2 + 1
	2 + 1 + 1 + 1
	1 + 1 + 1 + 1 + 1

	How many different ways can one hundred be written as a sum of at least two positive integers?

*/



$n = 100;
$t1 = array(1);
$t2 = array_fill(1, $n, 0); 
$ways = array_merge($t1, $t2);

for($i=1; $i<$n; $i++)
	for($j=$i; $j<=$n; $j++)
		$ways[$j] += $ways[$j-$i];
		
echo $ways[$n];



?>