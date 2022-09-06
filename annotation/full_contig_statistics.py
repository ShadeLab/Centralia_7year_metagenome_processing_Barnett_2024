#!/usr/bin/python

import sys
import os
import pandas
import re
from Bio import SeqIO

# Arguments
print('Number of arguments: ', len(sys.argv), 'arguments.')
print('Input contig directory: ', sys.argv[1])
print('Directory for stats: ', sys.argv[2])
print('Sample: ', sys.argv[3])
print('\n---\n')

contig_dir = sys.argv[1]
stats_dir =  sys.argv[2]
sampleID = sys.argv[3]

input_fasta = os.path.join(contig_dir, sampleID + '.filt_scaffolds.fasta')
output_stats = os.path.join(stats_dir, sampleID + '.contig_stats.txt')

id_list = []
length_list = []
GC_count_list = []
gap_count_list = []
N_count_list = []

contig_seq = SeqIO.parse(input_fasta, 'fasta')
for record in contig_seq:
	id_list.append(record.id)
	seq_length = len(str(record.seq))
	length_list.append(seq_length)
	GC_count = str(record.seq).count('G') + str(record.seq).count('C') + str(record.seq).count('g') + str(record.seq).count('c')
	GC_count_list.append(GC_count)
	gap_count_list.append(str(record.seq).count('-'))
	N_count_list.append(str(record.seq).count('N') + str(record.seq).count('n'))

stats_df = pandas.DataFrame({'contigName':id_list, 'length':length_list,
                             'GC_count':GC_count_list, 'n_gaps':gap_count_list,
                             'n_Ns':N_count_list})
stats_df.to_csv(output_stats, sep='\t', header=True, index=False)
