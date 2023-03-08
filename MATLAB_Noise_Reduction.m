tic
clc
clear
close all

[b,a] = butter(3, [800000 1100000]/(10000000/2),'bandpass');

Transistor = "T2x";
iteration = 1:60;
locations = 1:49;
locations = string(locations);

TransistorFolders = "T2\";
TransistorFoldersFiltered = "C:\Users\Taif\Desktop\Thesis_docs\Matlab\T2Filtered\";
backslash = "\";

IterationsFolder = 1:60;
IterationsFolder = string(IterationsFolder);

fileIDs = zeros(1,49);
fileIDs = string(fileIDs);

extension = ".txt";
extensionFiltered = "F.txt";

B = [];
C = [];
D = [];
E = [];

for k = 1:60
    for j = 1:49
        fileIDs(k,j) = append(TransistorFolders,IterationsFolder(1,k),backslash,locations(1,j),Transistor,IterationsFolder(1,k),extension);
        fileIDsFiltered(k,j) = append(TransistorFoldersFiltered,IterationsFolder(1,k),backslash,locations(1,j),Transistor,IterationsFolder(1,k),extension);
    end  
end

formatSpec = '%f';

works for 1-46,48-60
Doesn't work for 2,3,47 (49 double values??)

num1 = 1:46;
num2 = 48:60;

num =[num1 num2];


for k = 1:60
    for j = 1:49
        fileID = fopen(fileIDs(k,j),'r');
        fileIDFiltered = fopen(fileIDsFiltered(k,j),'w');
        fileIDsFiltered(k,j);
        k;
        j;
        A = fscanf(fileID,formatSpec);
        A = A(1:10000);
        dataOut = filter(b,a,A);
        dataOutPlot = dataOut;
        fprintf(fileIDFiltered,'%f ',dataOutPlot);
        D = [D A];
        B = [B dataOut];
        dataOut=[];
        fclose(fileID);
        fclose(fileIDFiltered);
    end
C(:,:,k) = B;
E(:,:,k) = D;
B = [];
D = [];
end

plot(A)

hold on

plot(dataOutPlot)

hold off
toc

% plot1 = E(:,22,5);
% % plot2 = E(:,26,1);
% timescale = linspace(0,0.001,10000)';
% plot(timescale,plot1);
% grid on
% xlabel('Time (s)')
% ylabel('Amplitude (V)')
% title('Signal received by T2 at location K22')



