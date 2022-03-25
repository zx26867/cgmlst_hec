<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    <li>
      <a href="#Algorithms">Algorithms</a>
    </li>
    <li><a href="#Assumptions and Limitation">Assumptions and Limitation</a></li>
    <li><a href="#Remaining Errors">Remaining Errors</a></li>
    <li><a href="#Software Required">Software Required</a></li>
    <li><a href="#Input">Input</a></li>
    <li><a href="#Output">Output</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Citation">Citation</a></li>
    <li><a href="#Contact">Contact</a></li>
  </ol>
</details>

## Introduction

ONT 9.4.1 flowcell is prone to generate indel (insertion/deletion) errors in homopolymer regions (single base repeating regions). This tool is used to correct these errors appearing in the core genes of bacteria. The corrected sequence has improved allelic call results for cgMLST analysis. In our testing dataset, the number of allelic call errors was reduced by 70.5%. 

This tool is built based on the concept of NanoMLST. However, NanoMLST can only be applied to the traditional 7-gene MLST. This tool enables such concept to be applied to cgMLST. We borrowed and modified a key function of NanoMLST’s script and supplied with our own algorithms/codes to make it work for cgMLST. 

Enterobase is a widely used database that offers cgMLST schemes for most bacteria. All available schemes can be downloaded from here. However, we found some of the alleles in these schemes are actually false alleles. Occasionally, Enterobase treats a sequencing error as a new allele and added into the scheme. Therefore, we have to use chewbbaca to remove these false alleles. If the Enterobase raw scheme is used as input, our correction approach would not work well. Detailed explanation for this please see the publication paper here. 

<!-- <p align="right">(<a href="#top">back to top</a>)</p> -->
## Algorithms

Detailed algorithms and logical flowchart for this correction approach are described in the publication paper.

## Assumptions and Limitation

For our correction approach, we assume Enterobase cgMLST schemes contain complete alleles of the bacteria species. For the DNA sequence of an isolate, if there is no allele in the scheme matching it, we assume it is always a sequencing error. However, it is possible that such no-match results from a new allele, but we assume the possibility is extremely low. 

Although we use chewbbaca adapted scheme to perform homopolymer error correction, we cannot use the adapted scheme for Enterobase cgMLST allelic call, since current Enterobase allelic calling does not support customized scheme. Chewbbaca allelic caller generates a bit different allelic call result from Enterobase. Therefore, we use chewbbaca adapted scheme to perform homopolymer error correction but use Enterobase to perform cgMLST allelic call. The discrepancy between the two schemes leads to a “mis-correction” problem (details are described in the publication paper). However, our correction approach still improves the allelic call accuracy by around 70% overall. 

## Remaining Errors

The remaining errors are mostly “mis-correction” and some uncorrected homopolymer errors, mismatches and insertions. Details are presented in the publication paper.

## Software Required

* Installation of chewbbaca and its dependencies
* Installation of BLAST Command Line

<!-- USAGE EXAMPLES -->
## Input
* A sample directory
     - Each sample must be single-contig DNA sequence
     - In FASTA files
* Directory to the chewbbaca adapted Enterobase Scheme

<!-- ROADMAP -->
## Output
* Corrected sample FASTA files placed in the same directory


## Usage
Step 1, download cgMLST raw scheme from Enterobase. 

Step 2, use chewbbaca to clean up invalid alleles present in the Enterobase raw scheme

* First, download the Prodigal training file (.trn) for your bacteria species <a href="https://github.com/B-UMMI/chewBBACA/tree/master/CHEWBBACA/prodigal_training_files"><strong>here</strong></a>.

* Then, run:
  ```sh
  chewBBACA.py PrepExternalSchema -i path/to/enterobase_raw_scheme/ -o adapted_scheme --cpu x --ptf /path/to/ProdigalTrainingFile
  ```

Step 3, open the script file, fill in the absolute paths to your sample directory and the adapted scheme directory

Step 4, enter the adapted scheme directory and run the script. 
* Then run:
  ```sh
  cd path/to/adapted_scheme
  python path/to/script.py
  ```

## Citation
Liou CH, Wu HC, Liao YC, Yang Lauderdale TL, Huang IW, Chen FJ. 2020. nanoMLST: accurate multilocus sequence typing using Oxford Nanopore Technologies MinION with a dual-barcode approach to multiplex large numbers of samples. Microb Genom 6.

<!-- CONTACT -->
## Contact
Zhihan Xian, email: zhihan.xian@uga.edu