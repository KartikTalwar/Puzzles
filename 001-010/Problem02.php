<?php


/*

	Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

*/

set_time_limit(300);

$phi = (1+sqrt(5))/2;
$tao = (1-sqrt(5))/2;

$fourmillion = false;
$x = 1;
$sum = NULL;

function fib( $n ) 
{
	if( $n < 2 ) 
	{
		return $n;
	} 
	else 
	{
		return fib( $n - 1 ) + fib( $n - 2 );
	} 
}


while($fourmillion == false)
{
	$nthterm = fib($x);
	
	if($nthterm < 4000000)
	{
		if($nthterm % 2 == 0)
		{
			$sum += $nthterm;
		}
		
		$x++;
	}
	else
	{
		$fourmillion = true;
	}
	
}


echo $sum;

?>