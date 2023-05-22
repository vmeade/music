use MIDI;
#use strict;
#use warnings;
my @events = (
  ['set_tempo', 0, 20000], 
);

@mn1=();



for (my$j=0;$j<@mn1;$j++){ 
	  push @events,
	    ['note_on' , 90,  60, $mn1[$j], 127],
	    ['note_off',  6,  60, $mn1[$j], 127],
	  ;
} 
my $track= MIDI::Track->new({ 'events' => \@events });
my $opus = MIDI::Opus->new(
 { 'format' => 0, 'ticks' => 120, 'tracks' => [ $track ] }); 
$opus->write_to_file( 'easy.mid' );
