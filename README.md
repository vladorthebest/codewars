# CodeWars

## Kata-4

    1.  Most frequently used words in a text.

        Function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
    

    2.  Sudoku Solution Validator.

        Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
        The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
    

    3.  Roman Numerals Helper.

        Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
        Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.   
    

    4.  Snail.

        Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

  
## Kata-5

    1.  Number of trailing zeros of N!

        Write a program that will calculate the number of trailing zeros in a factorial of a given number.

    2.  Extract the domain name from a URL.

        Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

        * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
    
    3.  Regex Password Validation.

        You need to write regex that will validate a password to make sure it meets the following criteria:

        - At least six characters long
        - Contains a lowercase letter
        - Contains an uppercase letter
        - Contains a number
        Valid passwords will only be alphanumeric characters.
    
    4.  Moving Zeros To The End.

        Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
    
    5.  Valid Parentheses.

        Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
    
    6.  Where my anagrams at?

        What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. 
    

## Kata-6

    1.  Persistent Bugger.

        Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
    
    2.  Counting Duplicates.

        Count the number of Duplicates
        Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
    
    3.  Take a Ten Minutes Walk.

        You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.