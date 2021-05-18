#!/usr/bin/R

library(biomaRt)
ensembl=useMart("ensembl")
argv <- commandArgs(trailingOnly=T)

#ensembl = useMart("ensembl",dataset="ggallus_gene_ensembl")

ensembl = useMart("ensembl",dataset=argv[1])

filters = listFilters(ensembl)

attributes = listAttributes(ensembl)

trans_id = getBM(attributes=c("ensembl_transcript_id","chromosome_name","start_position","end_position","strand"), filters = c('chromosome_name','start','end'),values=list(argv[2],argv[3],argv[4]), mart=ensembl)

utr5_id = getBM(attributes=c("ensembl_transcript_id","chromosome_name","5_utr_start","5_utr_end","strand"), filters = c('chromosome_name','start','end'),values=list(argv[2],argv[3],argv[4]), mart=ensembl)

utr3_id = getBM(attributes=c("ensembl_transcript_id","chromosome_name","3_utr_start","3_utr_end","strand"), filters = c('chromosome_name','start','end'),values=list(argv[2],argv[3],argv[4]), mart=ensembl)

cds_id = getBM(attributes=c("ensembl_transcript_id","chromosome_name","exon_chrom_start","cdna_coding_start","exon_chrom_end","cdna_coding_end","5_utr_start","5_utr_end","3_utr_start","3_utr_end","strand"), filters = c('chromosome_name','start','end'),values=list(argv[2],argv[3],argv[4]), mart=ensembl)

cds_seq = getSequence(chromosome = argv[2], start = argv[3], end  = argv[4],seqType = "cdna", mart = ensembl, type = "ensembl_transcript_id")

write.table(trans_id,"../source/trans.txt",col.names = FALSE, quote=F)

write.table(utr5_id,"../source/utr5.txt", col.names = FALSE, quote=F)

write.table(utr3_id,"../source/utr3.txt", col.names = FALSE, quote=F)

write.table(cds_id,"../source/exon.txt", col.names = FALSE, quote=F)

write.table(cds_seq,"../source/cds_sequence.txt", col.names = FALSE, quote = F)
