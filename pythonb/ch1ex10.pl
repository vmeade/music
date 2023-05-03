$n=@ARGV[0];
print "$n\n";
$prime=0;
for(my $x=2;$x*$x <= $n; $x++){
	print "$x\n";
	if($n % $x == 0){
		$prime++;
	} # is divisable, and therefore not prime.
} 

if($prime==0){print "Prime!\n";}
if($prime>1){print "Not Prime!\n";} 

