%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% codes for synthesize a cloudy image 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clc,clear;
Threshold = 0;  % A scope that are greater than the minimum are additionally divided into the background area
N = 512;        %  size of images
Beta = 255;     % maximum gray-level value, 255 here
A = 0.95;       % atmospheic light

I_cloudy_scene = imread('a cloudy sea image');
I_cloud_free_land = imread('a cloud-free land image');

metrix_1 = ones(N);

for c = 1:3  % every channal of a color image
 
    I_cs = double(I_cloudy_scene(:,:,c));
    I_cfl = double(I_cloud_free_land(:,:,c));
    
    Gamma = Beta;
    for i=1:N
        for j=1:N
            if I_cs(i,j) < Gamma
                Gamma = I_cs(i,j);
            end
        end
    end
    Gamma = Gamma + Threshold;
    
    I_dc = I_cs - Gamma * metrix_1;

    sum_cs = 0;
    sum_dc = 0;
    for i = 1:N
        for j = 1:N
            sum_dc = sum_dc + I_dc(i,j);
            if I_cs(i,j) > Gamma
                sum_cs = sum_cs + I_cs(i,j);
            end
        end
    end
    Lambda = sum_cs / sum_dc; 

    I_ci = I_dc * Lambda;
    I_ci_reverse = Beta * metrix_1 - I_ci; 
    I_ol = I_ci_reverse / 255 .* I_cfl;
    I_aci = A * metrix_1 .* I_ci;
    I_scs = I_ol + I_aci; 
   
    I_scs_max = max(max(I_scs));
    [row_max col_max] = find(I_scs_max == I_scs);

    A_adjusted = (Beta - I_ol(row_max(1), col_max(1))) / I_ci(row_max(1), col_max(1));
    if A_adjusted < A
        A = A_adjusted;
    end
    
    I_aci = A * metrix_1 .* I_ci;
    I_scs = I_ol + I_aci;
    
    I_synthesized(:,:,c) = uint8(I_scs);

end
imwrite(I_synthesized ,'the synthesized cloudy image');
    

