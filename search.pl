open(my $fh, "<", "/var/log/pacman.log")	
	or die "Error: File Name";

@fh=split(/\n/,$fh);

for(my $i=0;$i<@fh;$i++){
	if($fh[$i] =~ /dhcpcd/){
		print $fh[$i]."\n";
	}
}
