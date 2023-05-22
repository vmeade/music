use MIDI;
#use strict;
#use warnings;
my @events = (  ['set_tempo', 0, 800]  );

@note = ( 80, 80, 80, 80,
		  80, 80, 80, 80,
		  80, 80, 80, 80,
		  80, 80, 80, 80,
		  80, 80, 90, 80,
		  70, 80, 70, 70,
		  80, 70, 70, 90,
		  70, 70, 90, 70,
		  40, 40, 40, 50,
		  50, 80, 80, 40,
		  49, 50, 80, 49,
		  49, 50, 80, 49,
		  50, 80, 80, 40,
		  43, 47, 43, 43);

@vel=( 30, 90, 60, 30,
       30, 90, 60, 30,
       30, 90, 60, 30,
       45, 40, 45, 40,
       30, 90, 60, 30,
	   30, 90, 60, 30,
       30, 90, 60, 30,
       30, 90, 60, 30,
	   40, 80, 40, 70,
	   70, 70, 40, 70,
	   80, 70, 80, 80,
	   50, 40, 50, 43,
	   60, 30, 60, 43,
	   43, 43, 43, 74);

for (my$j=0;$j<@note;$j++){ 
	print($note[$j]);
	print("\n");
	push @events2,
	['note_on' , 90,  60, $note[$j], $vel[$j%7]],
	['note_off',  6,  60, $note[$j], $vel[$j%7]];
}

my $track2 = MIDI::Track->new({ 'events' => \@events2 });
my $opus2 = MIDI::Opus->new(
 { 'format' => 0, 'ticks' => 400, 'tracks' => [ $track2 ] } );
$opus2->write_to_file( 'output.mid' );
