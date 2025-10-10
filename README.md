# 1dv018-U2

## assignment 1:
Fördelar med linked list över arraylist:
Bättre tidskomplexitet för insättning och borttagning av element, O(1) kontra O(n)
Dynamisk storlek, minnet används mer effektivt beroende på antalet element
Nackdelar med linked list över arraylis:
sämre tidskomplexitet för att hitta element, eftersom den måste ta sig "fram" genom listan
Mer minnesanvändning på grund av lagring av pekare

## assignment 5

resultaten där jag mäter antalet kollisioner beroende på antal objekt och kapaciteten hos hashtabeln kan ses nedanför:
Number of collisions: 12 of 20 objects (capacity=8)
Number of collisions: 42 of 50 objects (capacity=8)
Number of collisions: 92 of 100 objects (capacity=8)
Number of collisions: 192 of 200 objects (capacity=8)
Number of collisions: 492 of 500 objects (capacity=8)
Number of collisions: 992 of 1000 objects (capacity=8)
Capacity=8: 192 collisions of 200 objects
Capacity=16: 184 collisions of 200 objects
Capacity=32: 169 collisions of 200 objects
Capacity=64: 138 collisions of 200 objects
Capacity=128: 99 collisions of 200 objects
Capacity=256: 56 collisions of 200 objects

så man kan se att min hashfunktion fungerar väl med mindre tabeller, såsom 20 objekt, men när objekten ökar så ökar även kollisionerna, detta är såklart förväntat, har man bara 8 hinkar så kommer man inte kunna få plats med 200 objekt.
Eftersom jag däremot la till en funktion där jag kan ge ett kapacitetvärde (skapa mer hinkar), så kan jag beroende på datamängden
öka antalet hinkar, och på så sätt minska antalet kollisioner, även om jag över 200 objekt har 138 kollisioner med 64 buckets, så behöver detta inte vara något negativt, eftersom det är få kollisioner per bucket, vilket leder till en bra tidskomplexitet (närmare O(1) vid find), till skillnad från 200 objekt med 8 buckets, där varje bucket troligtvis innehåller ungefär 25 objekt, alltså måste
koden leta efter rätt objekt i de enstaka bucketsen.
