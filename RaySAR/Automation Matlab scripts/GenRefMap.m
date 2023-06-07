clear all
close all
clc
%% Import POV-Ray data
folder = 'C:\Users\ekramer3\Documents\GitHub\RaySAR\RaySAR\Testfile\Multibox\'; % Data folder
num_files = size(dir([folder, '\*.txt']),1); % Number of .txt files in folder
for i = 1 : num_files
filename = "Contributions.txt"
full_filename = fullfile(folder,filename);
end
R = load(folder);
%% Define global variables
global Az Ra Intens Tr_L Sp ang r_geom range_dir All_reflections Index_All az_min az_max ra_min ra_max bounce_rem Output_path;

Az = R(Ind_keep,1); % azimuth coordinate
Ra = R(Ind_keep,2); % slant range coordinate
El = R(Ind_keep,3);
Intens = R(Ind_keep,4); % intensities
Tr_L = R(Ind_keep,5); % trace level
Sp = R(Ind_keep,6); % flag for specular reflection

ang
r_geom
range_dir
All_reflections
Index_All
az_min
az_max
ra_min
ra_max
bounce_rem
Output_path;
%% Define local structure
go.a_pix = 1;
go.r_pix = 1;

go.a_min = -20;
go.a_max = 20;

go.r_min = 0;
go.r_max = 40;

go.db_min = 0;
go.db_max = 255;

go.clip = 0;

go.filt = 0;

go.bounce_level = 5;

go.specular_flag = 0;

go.sinc_sim = 0;

go.a_res = 1;
go.r_res = 1;

go.coh = 0;

go.dBnodB = 1;

go.store = 1;
%% Call function
Gen_Refl_Map(go);
