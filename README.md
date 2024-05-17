## Github Repository for
# Seven years of whole community shotgun metagenomes from soils affected by the coal mine fires in Centralia, Pennsylvania
## by Samuel Barnett and Ashley Shade
<i>This work is published.</i>

### Data
The raw data for this study are available in the NCBI SRA under bioproject [PRJNA974462](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA974462).

### To cite this work or code
Barnett SE, Shade A. 0. Seven years of microbial community metagenomes from temperate soils affected by an ongoing coal seam fire. Microbiol Resour Announc 0:e00198-24. DOI: [10.1128/mra.00198-24](https://doi.org/10.1128/mra.00198-24)

### Abstract
We examined the dynamics of soil microbiomes under heat press disturbance from an underground coal mine fire in Centralia, Pennsylvania. Here we present metagenomic sequencing and assembly data from soil microbiomes across seven consecutive years at repeatedly sampled fire affected sites along with unaffected reference sites.

### Contents
Code is split up into two directories: [sequence_proc](https://github.com/ShadeLab/Centralia_7year_metagenome_processing_Barnett_2024/tree/main/sequence_proc) and [Annotation](https://github.com/ShadeLab/Centralia_7year_metagenome_processing_Barnett_2024/tree/main/annotation).

#### sequence_proc
Code used for sequence processing including read QC and assembly can be found under sequence_proc. Scripts were run using SLURM on the MSU HPCC using slurm batch files with suffix .sb and are numbered by their order in the processing workflow. Outputs such as logs, warnings, or errors if any, are designated by the suffix .out and named in accordence with the slurm batch file. Assembly in particular was run in chunks largely by sample site and outputs are within subdirectories. Also included are code and output logs for generating read statistics, nonpareil, microbecensus, N50, and read based kraken taxonomic annotation.

#### annotation
Code used for annotating contigs with prokka and contig taxonomic annotation with kraken. As before Scripts were run using SLURM on the MSU HPCC using slurm batch files.

### Funding
This work was supported by the U.S. National Science Foundation CAREER award #1749544 to AS. This work was supported in part by Michigan State University through computational resources provided by the [Institute for Cyber-Enabled Research](https://icer.msu.edu/).

### More info
[ShadeLab](http://ashley17061.wixsite.com/shadelab/home)
