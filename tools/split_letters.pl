#!/usr/bin/perl -w

## Grab each command line option in turn and use it as our filename
foreach my $filename (@ARGV) {

    ## Each time we read a line, we'll append it to this variable.
    ## When we reach the start of a letter, we'll print the whole thing
    ## and reset this to an empty string.
    my $buffer = "";
    
    ## Count how many sections we've seen so far
    my $section = 1;

    ## Open the file and read it, one line at a time
    open IN, $filename;
    while (<IN>) {
	## Get rid of newline characters and tabs
	s/\s+/ /g;
	
	# Does this line look like the start of a new letter?
	if (/^LETTER/) {
	    
	    ## Print the previous section,
	    print "${filename}_$section\t$filename\t$buffer\n";
	    
	    ## reset the buffer,
	    $buffer = "";
	    
	    ## and increment the section counter.
	    $section++;
	    
	    ## Now we can start the next section.
	}
	
	## Add the current line to the buffer.
	$buffer .= $_;
    }
    close IN;
    
    ## Print the last section.
    print "${filename}_$section\t$filename\t$buffer\n";
}
