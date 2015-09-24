<?php
  /**
  * Swaps the given indices in a string
  */
  function swap($string,$x,$y)
  {
     $t=$string[$x];
     $string[$x]=$string[$y];
     $string[$y]=$t;
    return $string;
  }
  /**
  * Returns the Permutations of a String
  */
  function permute($in,$startPos,$endPos)
  {
     if((strlen($in)==1) || ($startPos==$endPos))
     {
       print($in."\n");
       return $in;
     }
     else
     {
       for($a = $startPos; $a < $endPos; $a++)
       {
         $in=swap($in,$startPos,$a);
         permute($in,$startPos+1,$endPos);
       }
     }
  }
  $input = "abcd";
  permute($input,0,strlen($input));

?>
