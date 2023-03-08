clc
clear
close all
%changes when test to train
%TransistorFolders & TransistorFoldersDestination  Test to Train
%Iterations from 46:60 to 1:45 
%IterationsFolder from 46:60 to 1:45
%for loop k 1:15 to 1:45 (recursive)
%Selection of the transducer
Transistor = "T2x";
%Selection of the points on the grid. Here, 14 points are selected.
locations = 15:28;
locations = string(locations);
%Directory from which the files are to be copied
TransistorFolders = "C:\Users\Taif\Desktop\Thesis_docs\Matlab\T2_check\";
%Directory to which files are to be copied
TransistorFoldersDestination = "C:\Users\Taif\Desktop\Thesis_docs\Matlab\T2_organized_check\Train\";
backslash = "\";
%The number of iterations to be copied. 75% of the training data is selected.
IterationsFolder = 1:45;
IterationsFolder = string(IterationsFolder);
%The number of locations.
fileIDs = zeros(1,14);
fileIDs = string(fileIDs);
destinationFolders = zeros(1,14);
destinationFolders = string(destinationFolders);
extension = ".txt";
%Getting a list of directory pathways from where the files are to be copied.
for k = 1:45
    for j = 1:14
        fileIDs(k,j) = append(TransistorFolders,IterationsFolder(1,k),backslash,locations(1,j),Transistor,IterationsFolder(1,k),extension);
    end  
end
%Selection of the locations on the grid. These are folder names of the destination.
destinationFolderNumbers = 15:28;
destinationFolderNumbers = string(destinationFolderNumbers);
%The loop returns a list of destination folder pathways
for k = 1:14
    destinationFolders(1,k) = append(TransistorFoldersDestination,"k",destinationFolderNumbers(1,k));
end
%The outer loop controls the location names. The inner loop covers the iterations within those locations. 
for k = 1:14
    for j = 1:45
        copyfile (fileIDs(j,k), destinationFolders(1,k));
    end
end