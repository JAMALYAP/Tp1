nombres = int(input())
Syracuse = []
while (nombres != 1):
    if(nombres % 2 == 0):
        nombres = int(nombres/2)
    else:
        nombres = 3 * nombres  + 1
    Syracuse.append(nombres)
print("La suite de syracuse dU premier terme "+ str(nombres)+" est la suivante  :"+str(Syracuse) + " Elle s'est faite en: " + str(len(Syracuse))+ " etapes et de hauteur(max) :"+ str(max(Syracuse)))