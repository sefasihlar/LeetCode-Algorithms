            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # liste içerindeki kelimelerin hepsinde aynı harf dizisinin olup olmadıgını kontrol  eden algoritma;eşit harf dizisi yoksa sonucu boş string olarak döndür.
       
    
        if len(strs) ==0:
            return("")
        
        if len(strs) == 1:
            return(strs[0])
        

        pref = strs[0]#dizinin ilk elemanı olan "flower"
        print(pref)
        plen = len(pref)# ilk elemanın sayisi
      

        for i in strs[1:]:# dizinin ikinci elamanından başla
           
            while pref != i[0:plen]:
                # flower ile eşit değilse diğer elemanlar
                # flower'ın sondan bir harfini at
                pref = pref[0:plen-1]
                # ve azaltarak devam et 
                plen-=1
                
                # eğer harf sayisi kalmadıysa ve eşit bulunamadıysa geriye boş str döndür
                
                if plen ==0:
                    return("")
        #strs elemanlarının ilk iki harfı eşit olunca program durdu ve eşite olan harfler = fl
        return(pref)
            
        
        