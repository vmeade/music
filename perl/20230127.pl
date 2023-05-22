use MIDI;
#use strict;
#use warnings;
my @events = (
  ['set_tempo', 0, 2000], 
);
@mn1=(63,67,69,67,65,52,45);
@mn1a=reverse @mn1;
@mn2=(80,74,72,68,64,62,62);
@mn2a=reverse @mn2;
@mn3=(40,42,43,44,48,84,88);
@mn3a=reverse @mn3;
@mn4=(32,28,34,42,44,46,48);
@mn4a=reverse @mn4;
@mn5=(44,42,44,42,44,42,44);
@mn5a=reverse @mn5;
@mn6=(72,70,68,66,90,88,86);
@mn6a=reverse @mn6;

@mn=(@mn1,@mn1a,@mn2,@mn2a,@mn3,@mn3a,@mn4,@mn4a,@mn5,@mn5a,@mn6,@mn6a);

for($i=0;$i<48;$i++){
	for (my$j=1;$j<7;$j++){ 
		if($i%6==0){
	 		 push @events2,
	   		 ['note_on' , 90,  60, $mn6[$j], $mn2[$j%7]],
	    		 ['note_off',  6,  60, $mn6[$j], $mn2[$j%7]],
	  		;
		}
		elsif($i%4==0){
	 		 push @events2,
	   		 ['note_on' , 90,  60, $mn4[$j], $mn3[$j%7]],
	    		 ['note_off',  6,  60, $mn4[$j], $mn3[$j%7]],
	  		;
		}
		else{
	  		push @events2,
	   		['note_on' , 90,  60, $mn1[$j], $mn3[$j%7]],
	    		['note_off',  6,  60, $mn1[$j], $mn3[$j%7]],
	 		 ;
		}
	  #print($mn1[$j])
	} 
	
	if($i%3==0){
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
	}
	elsif($i%2==0){
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
	}
	else{
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
		push @events2,['note_on',90,60,0,0],['note_off',90,60,0,0],;
	}

}
my $track2 = MIDI::Track->new({ 'events' => \@events2 });
my $opus2 = MIDI::Opus->new(
 { 'format' => 0, 'ticks' => 400, 'tracks' => [ $track2 ] } );
$opus2->write_to_file( 'output.mid' );
