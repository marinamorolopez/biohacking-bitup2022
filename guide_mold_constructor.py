# -*- coding: utf-8 -*-

"""

Created on Tue Oct  25 20:52 2022
@author: Marina Moro López

"""

from tkinter.filedialog import askopenfile
import math

def main():
    
    print('Select genome file')
    genome_file = askopenfile(mode='r')
    genome_seq = genome_file.readlines()[1:]
    genome_seq = ''.join(genome_seq).replace('\n', '')
    
    mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    while mutation_position <= 0:
        print('Invalid input. Introduce positive integer. ')
        mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    while mutation_position > len(genome_seq):
        print('Invalid input. Introduce position within genome length (e.g. ' + str(len(genome_seq)) + ').')
        mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    
    print('Select tweet file')
    tweet_file = askopenfile(mode='r')
    tweet_text = tweet_file.readlines()
    tweet_text = ''.join(tweet_text).replace('\n', '')
    
    tweet_binary = toBinary(tweet_text)
    tweet_DNA = toDNA(tweet_binary)
    
    DNA_guide, mold, mutated_genome_seq = seq_constructor(genome_seq, mutation_position, tweet_DNA)

    tweet_binary_decoded = fromDNA(mutated_genome_seq, mutation_position, tweet_DNA)
    tweet_text_decoded = toString(tweet_binary_decoded)

    coded_tweet_file = open('CODED_TWEET.txt', 'w')
    coded_tweet_file.write(tweet_DNA)
    coded_tweet_file.close()
    
    guide_file = open('GUIDE.txt', 'w')
    guide_file.write(DNA_to_RNA(DNA_guide))
    guide_file.close()

    mold_file = open('MOLD.txt', 'w')
    mold_file.write(mold)
    mold_file.close()
    
    mutated_genome_file = open('MUTATED_SEQUENCE.txt', 'w')
    mutated_genome_file.write(mutated_genome_seq)
    mutated_genome_file.close()
    
    decoded_tweet_file = open('DECODED_TWEET.txt', 'w')
    decoded_tweet_file.write(tweet_text_decoded)
    decoded_tweet_file.close()


def seq_constructor(genome_seq, mutation_position, tweet_DNA):
          
    DNA_guide = genome_seq[mutation_position-25:mutation_position+25]
    mold = genome_seq[mutation_position-25:mutation_position]+ tweet_DNA + genome_seq[mutation_position:mutation_position+25]
    mutated_genome_seq = genome_seq[:mutation_position] + tweet_DNA + genome_seq[mutation_position:]
    
    return DNA_guide, mold, mutated_genome_seq


def toBinary(tweet_text):
    
    tweet_ascii, tweet_binary = [], []
    for letter in tweet_text:
        tweet_ascii.append(ord(letter))
    for char in tweet_ascii:
        tweet_byte = format(char, "#010b")
        tweet_byte = tweet_byte[2:]
        tweet_binary.append(tweet_byte)

    return tweet_binary


def toDNA(tweet_binary):
    
    tweet_DNA = ""
    for byte in tweet_binary:
        for i in range(0, (len(byte)-1), 2):
            if byte[i] + byte[i+1] == "00":
                tweet_DNA += "A"
            elif byte[i] + byte[i+1] == "11":
                tweet_DNA += "T"
            elif byte[i] + byte[i+1] == "01":
                tweet_DNA += "G"
            elif byte[i] + byte[i+1] == "10":
                tweet_DNA += "C"

    return tweet_DNA

    
def fromDNA(mutated_genome_seq, mutation_position, tweet_DNA):
    
    tweet_DNA_decoded = mutated_genome_seq[(mutation_position):(mutation_position + len(tweet_DNA))]
    tweet_binary_decoded = ""
    for base in tweet_DNA_decoded:
        if base == "A":
            tweet_binary_decoded += "00"
        elif base == "T":
            tweet_binary_decoded += "11"
        elif base == "G":
            tweet_binary_decoded += "01"
        elif base == "C":
            tweet_binary_decoded += "10"
    tweet_binary_decoded = [tweet_binary_decoded[i:i+8] for i in range(0, len(tweet_binary_decoded), 8)]

    return(tweet_binary_decoded)                                      
    

def toString(tweet_binary_decoded):
    
  tweet_ascii_decoded = []
  tweet_text_decoded = ""
  for byte in tweet_binary_decoded:
    byte = int(byte)
    rem = 0
    char = 0
    digits = int(math.log10(byte)) + 1
    for j in range(digits):
      rem = ((byte%10)*(2**j))   
      byte = byte//10
      char = char + rem
    tweet_ascii_decoded.append(char)
  for char in tweet_ascii_decoded:
    tweet_text_decoded=tweet_text_decoded + chr(char)
    
  return tweet_text_decoded


def DNA_to_RNA(DNA_guide):
    
    RNA_guide = ""
    for base in DNA_guide:
        if base == "T":
            RNA_guide += "A"
        elif base == "A":
            RNA_guide += "U"
        elif base == "C":
            RNA_guide += "G"
        elif base == "G":
            RNA_guide += "C"
    
    return RNA_guide


main()