from Bio import SearchIO
from Bio import SeqIO
from Bio.Seq import Seq
import os
import sys

# Enter the absolute path for the directory of ONT single-contig assembly files
# Do NOT include a slash at the end
# Example: '/data/samples'
samples = "/data/samples"

# Enter the absolute path for the directory of chewbbaca processed scheme
# Example: '/data/scheme'
scheme = "/data/scheme"


def processgap (query,subject):
    gappos=0
    k=3
    if '-' in query:
        for i in range(len(query)):
            if '-AA' in query[i:i+3] or 'AA-' in query[i:i+3]:
                gappos=i
                if subject[gappos:gappos+3]=='AAA':
                    print ("   gap in query:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k])
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k] + query[gappos + 3 + k:]

            if '-TT' in query[i:i+3] or 'TT-' in query[i:i+3]:
                gappos=i
                if subject[gappos:gappos+3]=='TTT':
                    print ("   gap in query:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k])
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k] + query[gappos + 3 + k:]
            if '-CC' in query[i:i+3] or 'CC-' in query[i:i+3]:
                gappos=i
                if subject[gappos:gappos+3]=='CCC':
                    print ("   gap in query:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k])
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k] + query[gappos + 3 + k:]
            if '-GG' in query[i:i+3] or 'GG-' in query[i:i+3]:
                gappos=i
                if subject[gappos:gappos+3]=='GGG':
                    print ("   gap in query:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k])
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k] + query[gappos + 3 + k:]
    if '-' in subject:
        for i in range(len(subject)):
            if '-AA' in subject[i:i+3] or 'AA-' in subject[i:i+3]:
                gappos=i
                if query[gappos:gappos+3]=='AAA':
                    print ("   gap in subject:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k].replace('-',''))
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k].replace('-', '') + query[gappos + 3 + k:]
                    subject=subject.replace(subject[gappos-k:gappos+3+k],subject[gappos-k:gappos+3+k].replace('-',''))
            if '-TT' in subject[i:i+3] or 'TT-' in subject[i:i+3]:
                gappos=i
                if query[gappos:gappos+3]=='TTT':
                    print ("   gap in subject:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k].replace('-',''))
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k].replace('-', '') + query[
                                                                                                       gappos + 3 + k:]
                    subject=subject.replace(subject[gappos-k:gappos+3+k],subject[gappos-k:gappos+3+k].replace('-',''))
            if '-CC' in subject[i:i+3] or 'CC-' in subject[i:i+3]:
                gappos=i
                if query[gappos:gappos+3]=='CCC':
                    print ("   gap in subject:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k].replace('-',''))
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k].replace('-', '') + query[gappos + 3 + k:]
                    subject=subject.replace(subject[gappos-k:gappos+3+k],subject[gappos-k:gappos+3+k].replace('-',''))
            if '-GG' in subject[i:i+3] or 'GG-' in subject[i:i+3]:
                gappos=i
                if query[gappos:gappos+3]=='GGG':
                    print ("   gap in subject:"+query[gappos-k:gappos+3+k]+"==>"+subject[gappos-k:gappos+3+k].replace('-',''))
                    query = query[:gappos - k] + subject[gappos - k:gappos + 3 + k].replace('-', '') + query[gappos + 3 + k:]
                    subject=subject.replace(subject[gappos-k:gappos+3+k],subject[gappos-k:gappos+3+k].replace('-',''))

    return (query)


for isolate in os.listdir(samples):
    if isolate.endswith("ONT"):
        input_seq = samples + '/' + str(isolate)
        #input_seq = os.path.abspath(isolate)
        print(input_seq)

        # input_seq = input("Enter input path: ")
        # input_seq = "/data/zhihan/Mars_ONT_guppy5/Runs/Mars_Run01/2009K-1742_ONT"

        seq_in = SeqIO.read(input_seq, "fasta")
        real_seq = seq_in.seq

        for file in os.listdir(scheme):
            if file.endswith(".fasta"):
                try:
                    output_name = file[:-6] + ".xml"

                    cmd = "makeblastdb -in " + file + " -dbtype nucl"
                    os.system(cmd)

                    cmd = "blastn -db " + file + " -query " + input_seq + " -out " + output_name + " -outfmt 5 -max_target_seqs 10000"
                    os.system(cmd)

                    blast_qresult = SearchIO.read(output_name, "blast-xml")

                    blast_hit = blast_qresult[:15]
                    has_em = False
                    for blast_hsp in blast_qresult:
                        if blast_hsp[0].ident_num == blast_hsp[0].aln_span:
                            has_em = True

                    if has_em:
                        continue

                    temp = []
                    for blast_hsp in blast_hit:
                        if blast_hsp[0].aln_span - blast_hsp[0].ident_num - blast_hsp[0].gap_num <= 1:
                            temp.append(blast_hsp)
                    blast_hit = temp
                    print("The number of top hit is " + str(len(temp)))

                    top_hit = blast_qresult[0][0]
                    print("gap# for top hit is " + str(top_hit.gap_num))

                    query_seq = str(top_hit.query.seq)
                    query_start = top_hit.query_start
                    query_end = top_hit.query_end
                    query_set = []

                    for blast_hsp in blast_hit:
                        hit_range = blast_hsp[0].hit_range
                        query_range = blast_hsp[0].query_range
                        alignmen_len = blast_hsp[0].aln_span

                        start_point = blast_hsp[0].hit_start

                        query_seq = str(blast_hsp[0].query.seq)
                        query_len = len(query_seq.replace("-", ""))
                        hit_seq = str(blast_hsp[0].hit.seq)
                        original = query_seq

                        processed_query = processgap(query_seq, hit_seq)

                        if original != processed_query:
                           query_set.append(processed_query)

                    consensus = query_seq.replace('-', '')
                    max_count = 0
                    for item in query_set:
                        if query_set.count(item) > max_count:
                            max_count = query_set.count(item)

                    for item in query_set:
                        if query_set.count(item) == max_count and max_count > 0:
                            consensus = item
                            break
                    print("length of candidate set is " + str(len(query_set)))
                    print("max count is " + str(max_count))
                    print(len(query_set))

                    real_seq = str(real_seq).replace(query_seq.replace('-', ''), consensus.replace('-', ''))

                    seq_in.seq = Seq(real_seq)

                except IndexError:
                    continue

        output_name = input_seq + "_hec"
        SeqIO.write([seq_in], output_name, "fasta")





