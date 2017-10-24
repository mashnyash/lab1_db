

def print_data_base(my_data_base):
    print("%15s" % "AUTHOR", "%15s" % "BOOK TITLE", "%7s" % "PAGES" "\n")
    for record in my_data_base:
        print("%15s" % record['author'])
        for element in record['books']:
            print("%30s" % element['name'], "%7s" % element['pages'])



def find_book(my_data_base):
    author=input("Please enter your first and last name of the author: ")
    if (check_author(my_data_base, author)==True):
        for record in my_data_base:
            if (record['author']==author):
                for element in record['books']:
                    print("%30s" % element['name'], "%7s" % element['pages'])
    else:
        print("There isn`t such author in the database")


def select_by_author(my_data_base, author_name):
        for record in my_data_base:
            if (record['author']==author_name):
                return record

            

def print_one_element(record):
    print("AUTHOR: ")
    print("%20s" % record['author'])
    print("%10s" % "BOOK TITLE: ", "%20s" % "PAGES:")
    for element in record['books']:
         print("%21s" % element['name'], "%15s" % element['pages'])


def var_function (my_data_base):
    for record in my_data_base:
        mark=0
        for element in record['books']:
            if (element['pages']>100):
                mark=1
        if (mark==1):
            print(record['author'])

                
def add_element(my_data_base):
    author=input("Please enter your first and last name of the author: ")
    if (check_author(my_data_base, author)==True):
        print("\nThis author already exists in the database:\n")
        print_one_element(select_by_author(my_data_base, author))
        check=input("Do you want add book by %s to database  Y/N ?" % author)
        check.lower
        if (check=="y"):
            book_title=input("please enter the title of the book: ")
            pages=int(input("Please enter the number of pages of the book: "))
            add_book(my_data_base, author, book_title, pages)
    else:
        check=input("Do you want add author %s to the database Y/N ?" % author)
        check.lower
        my_data_base.append({'author':author, 'books':[]})
        if (check=="y"):
            check=input("Do you want add book by %s to the database Y/N ?" % author)
            check.lower
            if (check=="y"):
                book_title=input("please enter the title of the book: ")
                pages=int(input("Please enter the number of pages of the book: "))
                add_book(my_data_base, author, book_title, pages)


def delete_element(my_data_base):
    author=input("Please enter your first and last name of the author: ")
    if (check_author(my_data_base, author)==True):
        check=input("Do you want delete all books by %s  Y/N?" % author)
        check.lower
        if (check=='y'):
            for record in my_data_base:
                if (record['author']==author):
                    my_data_base.remove(record)
        else:
            check=input("Do you want delete one book by %s  Y/N?" % author)
            check.lower
            if (check=='y'):
                book_title=input("please enter the title of the book: ")
                delete_book(my_data_base, author, book_title)
    else:
        print("There isn`t such author in the database")
        
                            

def delete_book(my_data_base, author_name, book_title):
    for record in my_data_base:
        if (record['author']==author_name):
            for book in record['books']:
                if (book['name']==book_title):
                    record['books'].remove(book)
                    
                
            
def add_book(my_data_base, author_name, book_title, pages):
    for record in my_data_base:
        if (record['author']==author_name):
            record['books'].append({'name':book_title, 'pages':pages}) 
        
           
def check_author(my_data_base, author_name):
    for record in my_data_base:
        if(author_name==record['author']):
            return True
def Fffilter(my_data_base):
    temp=[]
    for record in my_data_base:
        books=record['books']
        for book in books:
            if book['pages']>=100:
                print(record['author'],'\t',book['name'],'\t',book['pages'])
                
                temp.append(record['author'])
    n = []
    for i in temp:
        if i not in n:
            n.append(i)
            print(i)






