import sys                  # importing modules
import unicodedata

if len(sys.argv) != 3:      # checking for correct number of arguments and exiting if there are not sufficient
    print("Incorrect number of input parameters")
    sys.exit(1)

file1 = sys.argv[1]         # assigning inputs given via arguments to variables
file2 = sys.argv[2]

print('\nThe system utilities I used to verify the  number of lines and number of characters are:\n'    # system utilities to check count
      ' 1)number of lines      : wc -l filename\n'
      ' 2)number of characters : wc -m filename\n')

def fileProcessing(file):   # function for processing the file
    print("Book: " + file.split("/")[-1])
    with open(file, 'r', encoding="utf-8") as f:         # opening the file with proper encoding format
        line_count=0
        char_count=0
        vowel_count=0
        consonant_count=0
        letter_count=0
        vowel_per=0
        for line in f:      # looping through each line in the file and counting number of lines and characters
            line = line.lower()
            line_count += 1
            char_count += len(line)
            vowels=['a', 'e', 'i', 'o', 'u']     # english vowels
            uni_vowels=['\u00e9', '\u00e2', '\u00ea', '\u00ee',     # french vowels unicodes
                        '\u00f4', '\u00fb', '\u00e0', '\u00e8',
                        '\u00f9', '\u00eb', '\u00ef', '\u00fc']
            L=['L', 'Lu', 'Ll', 'Lt', 'Lm', 'Lo', 'LC']    # letters unicode categories
            for letter in line:                            # looping through each letter in the line
                if unicodedata.category(letter) in L:      # checking for unicode character and calculating number of letters, vowels, consonants
                    letter_count += 1
                    if letter in vowels:
                        vowel_count += 1
                    elif letter in uni_vowels:
                        vowel_count += 1
                    else:
                        consonant_count += 1

            vowel_per = round(float(vowel_count)/letter_count*100, 2)     # calculating vowel percentage

    print("Number of lines      =  " + str(line_count).rjust(7))          # printing counts of variables in format
    print("Number of characters =  " + str(char_count).rjust(7))
    print("Number of vowels     =  " + str(vowel_count).rjust(7))
    print("Number of consonants =  " + str(consonant_count).rjust(7))
    print("Number of letters    =  " + str(letter_count).rjust(7))
    print("% vowels             =  " + str(vowel_per).rjust(6) + "%\n")
    return file.split("/")[-1],consonant_count,vowel_count                # returning filename, number of consonants, number of vowels

file1,consonants_file1,vowels_file1 = fileProcessing(file1)               # calling the file processing functions
file2,consonants_file2,vowels_file2 = fileProcessing(file2)

print("Actual:")                                                          # printing the actual calculated vowel and consonant values in each file
print("Book\t\tConsonants\tVowels")
print(file1 + "\t" + str(consonants_file1) + "\t\t" + str(vowels_file1))
print(file2 + "\t" + str(consonants_file2) + "\t\t" + str(vowels_file2) + "\n")

exp_consonants_file1 =  round(  (consonants_file1 + consonants_file2)     # calculating expected vowels and consonant values in each file
                              / (consonants_file1 + consonants_file2 + vowels_file1 + vowels_file2)
                              * (consonants_file1 + vowels_file1),2)
exp_vowels_file1 =  round(  (vowels_file1 + vowels_file2)
                          / (consonants_file1 + consonants_file2 + vowels_file1 + vowels_file2)
                          * (consonants_file1 + vowels_file1),2)
exp_consonants_file2 =  round(  (consonants_file1 + consonants_file2)
                              / (consonants_file1 + consonants_file2 + vowels_file1 + vowels_file2)
                              * (consonants_file2 + vowels_file2),2)
exp_vowels_file2 =  round(  (vowels_file1 + vowels_file2)
                          / (consonants_file1 + consonants_file2 + vowels_file1 + vowels_file2)
                          * (consonants_file2 + vowels_file2),2)

print("Expected:")                                                        # printing the expected calculations
print("Book\t\tConsonants\tVowels")
print(file1 + "\t" + str(exp_consonants_file1) + "\t" + str(exp_vowels_file1))
print(file2 + "\t" + str(exp_consonants_file2) + "\t" + str(exp_vowels_file2) + "\n")

chi_square = round(  (consonants_file1 - exp_consonants_file1)**2 / exp_consonants_file1          # calculating the chi-square value with actual and expected values
		   + (consonants_file2 - exp_consonants_file2)**2 / exp_consonants_file2
		   + (vowels_file1 - exp_vowels_file1)**2 / exp_vowels_file1
		   + (vowels_file2 - exp_vowels_file2)**2 / exp_vowels_file2 ,2)

print("chi-square = " + str(chi_square) + "\n")                           # printing the chi-square value

print('The null hypothesis is that the text in the two books is\n'        # hypothesis
      'drawn from the same population.\n')

print('Chi-square is 7160.61 with df = 1. That is above the cutoff\n'     # checking the chi-square value with p value to decide on the fact of hypothesis
      'for p < .5, which is 3.84. Therefore the null hypothesis\n'
      'is rejected, and there is a significant difference in the\n'
      'percentage of vowels in the two texts.\n')
