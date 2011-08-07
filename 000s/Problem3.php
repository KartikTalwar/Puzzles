<?php


/*

	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?

*/


set_time_limit(30000);

$n = 600851475143;


if($n % 2 == 0)
{
	$n /=  2;
	$last = 2;
	while ( $n % 2 == 0 )
	{
		$n /= 2;
	}
}
else
{
	$last = 1;
}

$factor = 3;

while( $n >1)
{
	if($n % $factor == 0)
	{
		$n /= $factor;
		$last = $factor;
		while($n % $factor == 0)
		{
			$n /= $factor;
		}
	}
	$factor = $factor + 2;
}

echo $last;



/**

OR

function factorize($n)
{
	$factors = array();
	$d = 2
	
	while($n > 1)
	{
		while($n%$d==0)
		{
			$factors[] = $d;
			$n /= $d;
		}
	}
	
	return $factors;
}


echo max(factorize($n));

*/





?>