opcao = input("Digite c para criptografar ou d para descriptografar\n")

j = 0
i = 0

alfabeto = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
cripto = ["@1*72", "H#i*&","$#8F*","9H&M4","&*#J@","6W7$H","%K%&G","O5$G3","7S3H2","XPU!*","*GH$#","#O*&Y",")O(IU","(3$2*","O86/*","-3-%G","$$E6&","-R8-4","1E1R!","&R87H","V7$$@","B02$2",")45W!","&*BA7","*)()#","*IW*W","G*/*7"]

if opcao == "c":
    x = input("Digite uma frase:\n")

    escolha = x.upper()
    
    frase = list(escolha)
    

   
    for i in range(len(frase)):
        
        j=0
        
        while(j <= 26):
            if(frase[i] == alfabeto[j]):
                frase[i] = cripto[j]
            j+=1    
            
    for j in range(len(frase)):
        print(frase[j], end="")
                
    

elif(opcao == "d"):
    
    escolha = input("Digite o codigo:\n")
    
    
    frase = [""]
    frase1 = [""]
    frase1 = list(escolha)
    
    
    k=0
    
    for l in range(len(frase1)):
        contador = 0
        print("l valor de l: ",l)
        while contador < 5:
            print("contador: ",contador)
            frase[l] = frase[l] + frase1[k]
            contador += 1
            k += 1
    
    
    for i in range(len(frase)):
        j=0
            
        while(j <= 26):
            if(frase[i] == cripto[j]):
                frase[i] = alfabeto[j]
                j+=1    

    for j in range(len(frase)):
        print(frase[j], end="")
    




