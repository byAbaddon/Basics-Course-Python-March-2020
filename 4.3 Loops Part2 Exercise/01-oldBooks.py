#oldBooks
import sys 

book = input()
book_count = int(input())
book_list = []

for index in range(0, book_count):
    current_book = input()
    if current_book == book: 
        print(f'You checked {index} books and found it.')
        sys.exit()
     
print(f'The book you search is not here!\nYou checked {book_count} books.')

#Troy, 8 ,Stronger, Life Style, Troy

  
 
  
  
  
