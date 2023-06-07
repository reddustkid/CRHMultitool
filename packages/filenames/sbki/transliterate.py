# import pytest
class stransname:
    
    def __init__(self, name_to_translate: str):
        self.name = name_to_translate
    
    def backward_text(x):
        return x[::-1]
    
    # def isRu(self):
    #     return 1
    #     with pytest.raises(ValueError, "name must be in ru"):
    #         print("ti ebalan?")
 
    # isRu(name_to_translate)
    def translate(self):
        ru_convTable = ["А","Б","Ц","Д","Е","Ф","Г","Х","И","Ж","К","Л","М","Н","О","П","Р","С","Т","У","В","И","Х","Й","З","Ы","Ь","Ъ","Ш","Щ","Ч","Ю","Я",
        "а","б","ц","д","е","ф","г","х","и","ж","к","л","м","н","о","п","р","с","т","у","в","и","х","й","з","ы","ь","ъ","ш","щ","ч","ю","я"," ","-"]
        en_convTable = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","I","X","Y","Z","II","","","HS","HS","HC","U","AY",
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","i","x","y","z","ii","","","hs","hs","hc","u","ay"," ","-"]
        tr_name_rev = ''
        for index_name in range(len(self.name)):
        
            tr_name = en_convTable[ru_convTable.index(self.name[index_name])]
            tr_name_rev = tr_name + tr_name_rev
            
        name_result = stransname.backward_text(tr_name_rev)    
        return name_result
    
if __name__ == '__main__':
    name_to_translate = stransname(input("Enter a name"))
    print(name_to_translate.translate())
