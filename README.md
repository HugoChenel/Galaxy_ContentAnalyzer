# Galaxy_ContentAnalyzer
Tool that provides basic information on nucleic acid and protein sequence

==========================================================
==========================================================

DOCUMENTATION for the tool : Content Analyzer

==========================================================
==========================================================


This tool requires Python 3.9.6 version.


===================Installation on a galaxy instance====================

Two files are provided in the archive file. Start by unziping this 
archive.
The first file is the python script contentAnalyzer.py, which will be 
run in the galaxy instance.
The second file is the xml wrapper file, which allows galaxy to implement
the file in the galaxy instance properly.


--------- Test the tool outside Galaxy

You can test the file with files provided in the test_file directory.

To test nucleotide analyzer, run :
python contentAnalyser.py -i test_files/nucleotide_test.fasta -t nucleotide -o results/test_nucleotide.tsv

To test peptide analyzer, run :
python contentAnalyser.py -i test_files/peptide_test.fasta -t peptide -o results/test_peptide.tsv

These tests must provide your output files containing your results.


--------- Put the tool into Galaxy's tools directory

You must create a myTools directory in the tools directory ( if not 
already existing ), which will contain the Content Analyzer tool.

Run the following commands in your galaxy directory:
cd tools
mkdir myTools
cd myTools

Then copy the python file contentAnalyzer.py and the xml wrapper file 
in the myTools directory.


--------- Make Galaxy aware of the new tool

In the config directory, you will find the galaxy.yml file which allows
galaxy to understand that a new tool is available.
In the tool_conf.xml add the 3 following lines 

...
<section name="MyTools" id="mTools">
    <tool file="myTools/contentAnalyser.xml" />
</section>
...

Refresh your galaxy instance, and the tool should be available in the 
MyTools section !
