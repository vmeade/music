use MIDI;
#use strict;
#use warnings;
my @events = (  ['set_tempo', 0, 2000]  );

@note=( 70, 60, 68, 62, 66, 64, 72,
        80, 70, 78, 72, 76, 74, 72,
        90, 80, 88, 82, 86, 84, 82,
        60, 50, 58, 52, 56, 54, 52);

for($i=0;$i<120;$i++){
	push @note, ($note[$i]+5/2+$note[$i-1]+5/2)%20;
}

@vel=( 30, 90, 60, 30, 30, 90, 60,
       30, 90, 60, 30, 30, 90, 60,
       30, 90, 60, 30, 30, 90, 60,
       45, 40, 45, 40, 60, 90, 45,
       30, 90, 60, 30, 30, 90, 60,
       30, 90, 60, 30, 30, 90, 60,
       30, 90, 60, 30, 30, 90, 60,
       45, 40, 45, 40, 60, 90, 45);

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
