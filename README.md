# biohacking-bitup2022
This repository includes the slides of the public presentation 'Biohackeando ADN para almacenar bit(up)s' of the BitUp2022 and both the code and files used for the practical case (slide 26 onwards).

## Installation
You simply have to download the .py and fasta file (or get your own fasta file from a database as [NCBI](https://www.ncbi.nlm.nih.gov/)).

## Usage
First you'll have to select the file of your genome of interest, then introduce the mutation position (as a positive integer) and select the txt file containing the tweet you want to add to your genome. The code will codify the tweet to binary and to DNA, so it is then inserted in the specified position of the genome. The code also decodifies that tweet stored in the DNA to binary and then to text format. When finished, you'll have five .txt files saved in the same folder of the .py file with the coded tweet, RNA guide, DNA mold, mutated sequence and decoded tweet.
If you want to recreate the example of the slides just use the provided fasta file with the mutation of the practical case (position 1.175).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
