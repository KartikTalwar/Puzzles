<?php


/*
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below two million.
*/



function sieve()
{
	$limit = 2000000;
	$sqrtlimit = sqrt($limit);
	$range = 0;
	$i = "";
	$sum = 0;
	
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
			$sum += $n;
		}
		
		$n+=2;
	}

	if($limit>=2)
	{
		$primes[0] = 2;
		$sum += 1;
	}
	
	//return array($primes, $sum);
	return $sum;
}


echo sieve();





?>