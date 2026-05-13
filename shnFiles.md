## Context:
   - I am generating slides with Latex.  I have a legacy app that generates different output streams from the source files which I
  have dubbed ".shn" files.  The idea for example is to generate a deck of slides and also longer more detailed lecture notes from the same source file, or e.g. to generate an exam and also exam solution from the same .shn file.
  - tags if the form \n<x> denotes an output stream labeled 'x' for the current line.   All tags start on the
  first character of a line.   tags of the form <*x> mean that all subsequent output goes to output stream 'x'.   <*xy> means subsequent
  lines go to output streams x and y.
  - after processing by an old perl script, all tags as well as lines that are not part of the selected stream are commented out and then processed by traditional Latex.

