<?php
/**
* This has a runtime of (O)n^2
*/
function subArray2($a)
{
	$arrayLength=count($a);
	$s = [0];//prefix sum array

	//calculate prefix sums
	for($i=1; $i<$arrayLength; $i++)
		$s[$i]=$s[$i-1]+$a[$i];

	$max= 0;//current max
	for($j=1; $j<$arrayLength; $j++)
		for($k=$j; $k<$arrayLength; $k++)
		{
			$sum = $s[$k]-$s[$j-1];
			if($sum>$max)
				$max = $sum;
		}
	var_dump($s);	
	return $max;
}
/**
* This has a runtime of (O)n
*/
function subArray3($a)
{
	$arrayLength=count($a);
	$m = [0];//suffix sums
	for($t=1; $t<$arrayLength;$t++)
	{
		$m[$t]=max(0,$m[$t-1]+$a[$t]);
	}
	$max = 0;
	for($t=1; $t<$arrayLength;$t++)
	{
		$max = max($max,$m[$t]);
	}
	var_dump($m);
	return $max;
}
//0 index of array does not matter.
$array = [0,-2, -3, 4, -1, -2, 1, 5, -3];
// $array=[0,2,-4,3];
echo(subArray3($array));
?>