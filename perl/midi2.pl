use MIDI;
#use strict;
#use warnings;
my @events = (
  ['set_tempo', 0, 20000], 
);
@mn1=(80,80,79,76,74,73,70);
@mn1a=reverse @mn1;
@mn2=(70,70,69,66,64,63,60);
@mn2a=reverse @mn2;
@mn3=(60,60,59,56,54,53,50);
@mn3a=reverse @mn3;
@mn4=(50,50,49,46,44,43,40);
@mn4a=reverse @mn4;
@mn5=(40,40,39,36,34,33,30);
@mn5a=reverse @mn5;
@mn6=(30,30,29,26,24,23,20);
@mn6a=reverse @mn6;

@mn=(@mn1,@mn1a,@mn2,@mn2a,@mn3,@mn3a,@mn4,@mn4a,@mn5,@mn5a,@mn6,@mn6a);

for (my$j=1;$j<@mn1;$j++){ 
	  push @events,
	    ['note_on' , 90,  60, $mn1[$j], 127],
	    ['note_off',  6,  60, $mn1[$j], 127],
	  ;
	  push @events2,
	    ['note_on' , 90,  60, $mn5[$j], 127],
	    ['note_off',  6,  60, $mn5[$j], 127],
	  ;
} 
my $track= MIDI::Track->new({ 'events' => \@events });
my $track2 = MIDI::Track->new({ 'events' => \@events2 });
my $opus = MIDI::Opus->new(
 { 'format' => 0, 'ticks' => 120, 'tracks' => [ $track ] }); 
my $opus2 = MIDI::Opus->new(
 { 'format' => 0, 'ticks' => 120, 'tracks' => [ $track2 ] } );
$opus->write_to_file( 'easy.mid' );
$opus2->write_to_file( 'easy2.mid' );
