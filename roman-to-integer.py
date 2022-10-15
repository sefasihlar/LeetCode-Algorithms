class Solution:
    def romanToInt(self, s: str) -> int:
        
        #soruda yapılması gereken en optimum düzeyde tekrarlanmadan girilen sayinin bulunması
        #542 sayininin örnegi alınsın DXLII 
        #500 -10 +50 +1 +1
        #açıklaması: büyükten küçüğe doğru sıralanır ve önündeki sayı kendisinden küçükse eksi olur ve çıkarılır
        
        numbers = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            
        }

        lens = len(s)

        i = lens-1
 
        output =0
         
        while i >= 0:
            #sayiları gez ve keninden önceki sayi kendisinden küçükse çıkar
            if i < lens-1  and numbers[s[i]] < numbers[s[i+1]]:
                output-=numbers[s[i]]
            #önündeki sayi kendisinden büyük ise topla
            else:
                output+= numbers[s[i]]
            i-=1
            
        return output
            
            
            