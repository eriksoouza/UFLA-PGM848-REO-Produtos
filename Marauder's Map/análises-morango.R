setwd("C://Users//Erik Souza//desktop")
#Matriz de correlação com dados experimentais de morangos em diferentes graus de maturação
dados<-read.table("dados-morango1.txt", h=T)
dados<-transform(dados, Lado=factor(Lado), Trat=factor(Trat))

#ANOVA - Fatorial Duplo - Lado e Trat
{
AOVDados<-aov(SST ~ Lado*Trat, data = dados) #SST
summary(AOVDados)

AOVDados<-aov(Peso ~ Lado*Trat, data = dados) #Peso
summary(AOVDados)

AOVDados<-aov(CE ~ Lado*Trat, data = dados) #CE
summary(AOVDados)

AOVDados<-aov(CM ~ Lado*Trat, data = dados) #CM
summary(AOVDados)

AOVDados<-aov(LE ~ Lado*Trat, data = dados) #LE
summary(AOVDados)

AOVDados<-aov(LM ~ Lado*Trat, data = dados) #LM
summary(AOVDados)

AOVDados<-aov(AE ~ Lado*Trat, data = dados) #AE
summary(AOVDados)

AOVDados<-aov(PE ~ Lado*Trat, data = dados) #PE
summary(AOVDados)

AOVDados<-aov(MaxR ~ Lado*Trat, data = dados) #MaxR
summary(AOVDados)

AOVDados<-aov(MinR ~ Lado*Trat, data = dados) #MinR
summary(AOVDados)

AOVDados<-aov(MedR ~ Lado*Trat, data = dados) #MedR
summary(AOVDados)

AOVDados<-aov(MaxG ~ Lado*Trat, data = dados) #MaxG
summary(AOVDados)

AOVDados<-aov(MinG ~ Lado*Trat, data = dados) #MinG
summary(AOVDados)

AOVDados<-aov(MedG ~ Lado*Trat, data = dados) #MedG
summary(AOVDados)

AOVDados<-aov(MaxB ~ Lado*Trat, data = dados) #MaxB
summary(AOVDados)

AOVDados<-aov(MinB ~ Lado*Trat, data = dados) #MinB
summary(AOVDados)

AOVDados<-aov(MedB ~ Lado*Trat, data = dados) #MedB
summary(AOVDados)
}
#Pacotes Corrplot e Hmisc
library(corrplot)
library(Hmisc)

#Lado A 
{
mc<-cor(dados[1:20,4:20], use = "complete.obs") #Lado A
mcp <- rcorr (as.matrix(dados[1:20,4:20])) #Lado A
matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "blank")
corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")

#Matriz de correlação mista - Lado A
#elipsoide em baixo e números em cima com variáveis na diagonal
corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1, insig="blank")
}
# Lado A - Trat 1
{
mc<-cor(dados[1:5,4:20], use = "complete.obs") #Lado A - Trat 1
mcp <- rcorr (as.matrix(dados[1:5,4:20])) #Lado A
matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")

#Matriz de correlação mista - Lado A - Trat 1
#elipsoide em baixo e números em cima com variáveis na diagonal
corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado A - Trat 2
{
  mc<-cor(dados[6:10,4:20], use = "complete.obs") #Lado A - Trat 2
  mcp <- rcorr (as.matrix(dados[6:10,4:20])) #Lado A - 
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado A - Trat 2
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado A - Trat 3
{
  mc<-cor(dados[11:15,4:20], use = "complete.obs") #Lado A - Trat 3
  mcp <- rcorr (as.matrix(dados[11:15,4:20])) #Lado A - 
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado A - Trat 3
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado A - Trat 4
{
  mc<-cor(dados[16:20,4:20], use = "complete.obs") #Lado A - Trat 4
  mcp <- rcorr (as.matrix(dados[16:20,4:20])) #Lado A - 
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado A - Trat 4
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}

#Lado B
{
mc<-cor(dados[21:40,4:20], use = "complete.obs") #Lado B
mcp <- rcorr (as.matrix(dados[21:40,4:20])) #Lado B
matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")

#Matriz de correlação mista - Labo B
#elipsoide em baixo e números em cima com variáveis na diagonal
corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado B - Trat 1
{
  mc<-cor(dados[21:25,4:20], use = "complete.obs") #Lado B - Trat 1
  mcp <- rcorr (as.matrix(dados[21:25,4:20])) #Lado B
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado B - Trat 1
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado B - Trat 2
{
  mc<-cor(dados[26:30,4:20], use = "complete.obs") #Lado B - Trat 2
  mcp <- rcorr (as.matrix(dados[26:30,4:20])) #Lado B - 
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado B - Trat 2
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado B - Trat 3
{
  mc<-cor(dados[31:35,4:20], use = "complete.obs") #Lado B - Trat 3
  mcp <- rcorr (as.matrix(dados[31:35,4:20])) #Lado B - 
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado B - Trat 3
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}
# Lado B - Trat 4
{
  mc<-cor(dados[36:40,4:20], use = "complete.obs") #Lado B - Trat 4
  mcp <- rcorr (as.matrix(dados[36:40,4:20])) #Lado B - 
  matrizcor<-corrplot(mc,p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black", insig = "label_sig")
  corrplot(mc, p.mat = mcp$P,sig.level = 0.05, type = "upper", method = "number", tl.col = "black")
  
  #Matriz de correlação mista - Lado B - Trat 4
  #elipsoide em baixo e números em cima com variáveis na diagonal
  corrplot.mixed(mc,upper = "number", lower = "ellipse",tl.pos = "lt",tl.col="black",p.mat = mcp$P,sig.level = 0.05,,number.cex = 1.1)
}