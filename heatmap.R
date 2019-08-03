#R script to plot a heatmap from 3 column data
library(reshape) # used for cast function
library(plyr) # used for ddply function
library(RColorBrewer) # used to customize heatmap colors
library(gplots)

data_heatmap<-read.table("try.txt")
data<-data.frame(Frame=data_heatmap$V1,Residue=data_heatmap$V2,SS=data_heatmap$V3)
data_heatmap_matrix <- cast(data, Frame ~ Residue)  # Matrix creation

#####data plotting#####
#######################
data_heatmap_matrix <- cast(data_heatmap, Year ~ Month)
rownames(data_heatmap_matrix) <- data_heatmap_matrix[,1]
data_heatmap_matrix[,1] <- NULL
data_heatmap_matrix <- as.matrix(t(data_heatmap_matrix))
data_heatmap_matrix <- data_heatmap_matrix[nrow(data_heatmap_matrix):1,]
data_heatmap_matrix[1:5, 1:5]

heatmap.2(data_heatmap_matrix, 
          dendrogram = "none", Colv = FALSE, Rowv = FALSE,
          scale = "none", col = rev(brewer.pal(11, "RdBu")),
          key = TRUE, density.info = "none", key.title = NA, key.xlab = "Temperature",
          trace = "none",
          main = "Temperature in the Netherlands",
          xlab = "Year",
          ylab = "Month")
