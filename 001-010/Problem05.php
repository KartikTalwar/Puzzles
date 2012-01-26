<?php


/*

	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

*/

set_time_limit(300);


for ($i = 1; $i < 10000000000; $i++)  
{  
	$found = true;  
	
	for ($j = 1; $j < 21 ; $j++)  
	{  
		if( $i % $j != 0)   
		{    
			$found = false;  
			break;  
		}  
	}  

	if($found == true)  
	{  
		echo $i;
		break;  
	}    
}  



?>