
def encode_morse(text):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'ą','ć','ę','ł','ń','ó','ś','ż','ź','1','2','3','4','5','6','7','8','9','0']
    
    b = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..','__',
        '_.','___','.__.','__._','._.','...','_','.._','..._','.__','_.._','_.__','__..',
        '._._','_._..','.._..','._.._','__.__','___.','..._...','__.._.','__.._',
        '.____','..___','...__','...._','.....','_....','__...','___..','____.','_____']
    
    text = text.lower()
    text2 = ''
    
    for t in text:
        if(t in a):
            text2 = text2+b[a.index(t)]+' '
        else:
            text2 = text2+t
            
    return text2.strip()
    
    
    
def decode_morse(text):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'ą','ć','ę','ł','ń','ó','ś','ż','ź','1','2','3','4','5','6','7','8','9','0']
    b = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..','__',
        '_.','___','.__.','__._','._.','...','_','.._','..._','.__','_.._','_.__','__..',
        '._._','_._..','.._..','._.._','__.__','___.','..._...','__.._.','__.._',
        '.____','..___','...__','...._','.....','_....','__...','___..','____.','_____']
    
    text = text.lower()
    text2 = ''
    
    for t in text.split(' '):
        if(t in b):
            text2 = text2+a[b.index(t)]
        elif(t==''):
            text2 = text2+' '
        else:
            text2 = text2+t
            
    return text2
