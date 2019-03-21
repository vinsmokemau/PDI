clc
imagen=zeros(300,250,3);
for i=1:300
    for j=1:250
      
        
        if i>=180 && i<=240 && j>=100 && j<=200   %%rectandulo azul  
    
            imagen(i,j,3)=255;
        
       elseif 90<=i && i<=150 && j>=(-2*i/3)+110 && j<=(2*i/3)-10 %%triangulo rojo
            imagen(i,j,1)=255;
           
        elseif  60<=i && i<=120 && 150<=j && j<=200+sqrt(30^2-(i-90)^2) %%figura amarilla
            imagen(i,j,1)=255;
            imagen(i,j,2)=255;
         
        else
            imagen(i,j,1)=255; %% fondo blanco
            imagen(i,j,2)=255;
            imagen(i,j,3)=255;
        end
    end
 end
imshow(uint8(imagen))
