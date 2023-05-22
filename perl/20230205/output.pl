use MIDI;
#use strict;
#use warnings;
my @events = (  ['set_tempo', 0, 2000]  );

@note=(60);



for($i=60;$i<120;$i+=5){
	push @note, int((($i+($i-1))/2)*.66);
}

for($i=30;$i<90;$i+=5){
	push @note, int((($i+($i-1))*2)*.33);
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
