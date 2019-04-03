close all
clear all
clc
A=imread('Koala.jpg');
A3=uint8(Color2Grey(A));
t=input('\n Introduzca Tamaño de Máscara (numero impar):');
[f,c]=size(A3);
borde=floor(t/2);
A1=imnoise(A3,'gaussian',0.0001);
A1=double(A1);
A2=ones(f,c);
for i=(1+borde):(f-borde)
    for j=(1+borde):(c-borde)
        pprom=0;
        for i1=((i-borde):(i+borde))
            for j1=((j-borde):(j+borde))
                pprom=pprom+A1(i1,j1);
            end
        end
        A2(i,j)=(pprom/(t^2));
    end
end
f1=figure;
imshow(A3);
f2=figure;
imshow(A1/255);
f3=figure;
imshow(A2/255);
