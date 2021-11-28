%Función que crea las 100 imágenes with an inclination. 
%Gf= función con las 100 imágenes, es una función, no son imágenes.
%sv= posición de cada uno de los centros de línea.
% A = Amplitude
% c = line with
% n = number of images
% d = inclinación arctg 1/d=angulo positivo
%Creo n imágenes de una línea gaussiana dada por los parámetros anteriores

%d values
%d=1.732 ==> 30º

%d=572.957==> 0.1º
%d=286.477==> 0.2º
%d=190.984==> 0.3º
%d=143.237==> 0.4º
%d=114.588==> 0.5º
%d=95.489 ==> 0.6º
%d=81.844 ==> 0.7º
%d=71.615 ==> 0.8º
%d=63.656 ==> 0.9º
%d=57.289 ==> 1º

function [GfF,sv] = creagfrim_in(A,c,n,d)


    %Build the matrix
    Gf = 0;
    
    %Basler-Cam spatial resolution
    % Nx = 1624; %Column
    % Ny = 1234; %rows
    
    Nx = 100; %Column
    Ny = 100; %rows
    
    %Initial position of the line
    i0 = round(Ny/2);

    %Generate n images
    Gf = zeros(Nx,Ny,n);%inicializo para no sobrecargar memoria
    Gf2 = zeros(Nx,Ny,n);%inicializo para no sobrecargar memoria
    GfF = zeros(Nx,Ny,n);%inicializo para no sobrecargar memoria
    sv = zeros(1,n);
    
    %(i,j) subíndices de cada imagen
    %"k" es cada imagen
    in = 0;%inclinación
    for i = 1:Nx %columns
        if d ~= 0
            in = in-1/d;
        end
        for j = 1:Ny %rows
            for k = 1:n 
                sv = i0 + (k)/n; %subpixel varitation (n=100-> centécima)
                 
                % j = center position.
                % sv = function independent variable
                Gf(j,i,k)= round(A*exp(-(sv+in-j)^2/(2*c^2)));%gaussian line  
                Gf2(j,i,k)= round(A*exp(-(sv+in+1-j)^2/(2*c^2)));%gaussian line  
                GfF(j,i,k)= Gf2(j,i,k) + Gf(j,i,k);
            end
        sv = 0;
        end
    end

    for k = 1:n 
       sv(k) = i0 + 0.5 + (k)/n; %subpixel vatiation with shift
       %sv(k) = i0  + (k)/n;  %subpixel vatiation without shift
       %sv(k) = i0 + (k); %pixel vatiation
    end
    

save('D:\PhD\Simulation Data\frim05_in009.mat', 'sv', 'GfF');   

end%final de la función