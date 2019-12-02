opcao = input("Digite c para criptografar ou d para descriptografar\n")

j = 0
i = 0

alfabeto = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
cripto = ["$", "+","1","2","#","3","4","0","5","*","9","(","6",")","@","7","8","&","!","-","{","^","}","~","[","]","?"]

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
                
    

elif opcao == "d":
    x = input("Digite o codigo:\n")

    frase = list(x)
    

   
    for i in range(len(frase)):
        
        j=0
        
        while(j <= 26):
            if(frase[i] == cripto[j]):
                frase[i] = alfabeto[j]
            j+=1    
            
    for j in range(len(frase)):
        print(frase[j], end="")
    








