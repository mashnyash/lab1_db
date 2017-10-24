import pickle
import Control as H
import Menu 

def Controll():
    check=Menu.My_Menu()
    if (check=='1'):
        H.print_data_base(data_base)
        Controll()
    elif(check=='2'):    
        H.add_element(data_base)
        Controll()
    elif(check=='3'):
        H.delete_element(data_base)
        Controll()
    elif(check=='4'):
        H.find_book(data_base)
        Controll()
    elif(check=='5'):
        H.var_function(data_base)
        Controll()
    elif(check=='6'):
        H.Fffilter(data_base)
        Controll()
    elif(check=='0'):
        check=input("Do you want exit from program Y/N ?")
        check.lower
        if (check=="y"):
            with open('data.pickle', 'wb') as f:
                pickle.dump(data_base, f)

        else:
            Controll()
    else:
        Controll()

with open('data.pickle', 'rb') as f:
    data_base=pickle.load(f)
Controll()
        
        
    
        
    

    

