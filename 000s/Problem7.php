<?php


/*

	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

	What is the 10 001st prime number?

*/



function sieve()
{
	$limit = 200000;
	$sqrtlimit = sqrt($limit);
	$range = 0;
	$i = "";
	
	while($range<$limit)
	{
		$i .= "11";
		$range += 2;
	}

	$n = 2;
	while($n < $sqrtlimit)
	{
		if ($i[$n])
		{
			$sqn = $n*$n;
			$k = $sqn;
			$i[$k]=0;

			while($k<=$limit)
			{
				$k += $n;
				$i[$k]=0;
			}
		}
		++$n;
	}
	
	$n = 1;
	while($n<$limit)
	{
		if($i[$n])
		{
			$primes[] = $n;
		}
		
		$n+=2;
	}

	if($limit>=2)
	{
		$primes[0] = 2;
	}
	
	return $primes[10000];
}


echo sieve();



?>