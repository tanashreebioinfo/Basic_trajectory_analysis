#R script to plot 2D contour 
#Library akima needs to be installed before using this script in R.

data<-read.table("final_data.dat")
library(akima)
 my.heat.colors <- function(x) { rev(heat.colors(x, alpha=1)) }
X <- matrix(data$V1)
Y <- matrix(data$V2)
Z <- matrix(data$V3)
my.matrix  <- interp(X,Y,Z)
ind.mat.na <- which(is.na(c(my.matrix$z)))
my.matrix$z[ind.mat.na] <- 0
tiff("2D_plot.tiff")
filled.contour(my.matrix, nlevels=10, color=my.heat.colors,xlab="Distance (Deamination), Å",ylab="Distance (Protonation), Å") ## nlevels to adjust the color bar levels

#filled.contour(my.matrix, nlevels=10, color.palette=colorRampPalette(c('cadetblue4','white','red')),xlab="Distance1",ylab="Distance2") 
## you can use any colors here

dev.off()
