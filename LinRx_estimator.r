# https://notesofdabbler.wordpress.com/2013/06/30/learning-r-parameter-fitting-for-models-involving-differential-equations/

# set working directory
setwd("C:/Users/Owner/AppData/Local\Temp/Rtmpyag5rW/downloaded_packages")
 
# load libraries
library(ggplot2) #library for plotting
library(reshape2) # library for reshaping data (tall-narrow <-> short-wide)
library(deSolve) # library for solving differential equations
library(minpack.lm) # library for least squares fit using levenberg-marquart algorithm

#load concentration data
 df=read.table("C:/Users/Owner/Desktop/desktop code/VanDerPol/VanDerPol/LinRx_data.dat")
 names(df)=c("time","ca","cb","cc")
 
# plot data
 tmp=melt(df,id.vars=c("time"),variable.name="species",value.name="conc")
 ggplot(data=tmp,aes(x=time,y=conc,color=species))+geom_point(size=3)
 
# rate function
rxnrate=function(t,c,parms){
 
 # rate constant passed through a list called parms
 k1=parms$k1
 k2=parms$k2
 
 # c is the concentration of species
 
 # derivatives dc/dt are computed below
 r=rep(0,length(c))
 r[1]=-k1*c["A"] #dcA/dt
 r[2]=k1*c["A"]-k2*c["B"] #dcB/dt
 r[3]=k2*c["B"] #dcC/dt
 
 # the computed derivatives are returned as a list
 # order of derivatives needs to be the same as the order of species in c
 return(list(r))
 
}

# predicted concentration for a given parameter set, uses only the times of data set df
cinit=c(A=1,B=0,C=0)
t=df$time
parms=list(k1=2,k2=1)
out=ode(y=cinit,times=t,func=rxnrate,parms=parms)
head(out)

# loss function judging how well the given parameters fit the data

ssq=function(parms){
 
 # inital concentration
 cinit=c(A=1,B=0,C=0)
 # time points for which conc is reported
 # include the points where data is available
 t=c(seq(0,5,0.1),df$time)
 t=sort(unique(t))
 # parameters from the parameter estimation routine
 k1=parms[1]
 k2=parms[2]
 # solve ODE for a given set of parameters
 out=ode(y=cinit,times=t,func=rxnrate,parms=list(k1=k1,k2=k2))
 
 # Filter data that contains time points where data is available
 outdf=data.frame(out)
 outdf=outdf[outdf$time %in% df$time,]
 # Evaluate predicted vs experimental residual
 preddf=melt(outdf,id.var="time",variable.name="species",value.name="conc")
 expdf=melt(df,id.var="time",variable.name="species",value.name="conc")
 ssqres=preddf$conc-expdf$conc
 
 # return predicted vs experimental residual
 return(ssqres)
 
}

# parameter fitting using levenberg marquart algorithm
# initial guess for parameters
parms=c(k1=0.5,k2=0.5)
# fitting
fitval=nls.lm(par=parms,fn=ssq)

# Summary of fit
summary(fitval)

# variance Covariance Matrix
S=vcov(fitval)

# Estimated parameter
parest=as.list(coef(fitval))
parest

# plot of predicted vs experimental data
 
# simulated predicted profile at estimated parameter values
cinit=c(A=1,B=0,C=0)
t=seq(0,5,0.2)
parms=as.list(parest)
out=ode(y=cinit,times=t,func=rxnrate,parms=parms)
outdf=data.frame(out)
names(outdf)=c("time","ca_pred","cb_pred","cc_pred")
 
# Overlay predicted profile with experimental data
tmppred=melt(outdf,id.var=c("time"),variable.name="species",value.name="conc")
tmpexp=melt(df,id.var=c("time"),variable.name="species",value.name="conc")
p=ggplot(data=tmppred,aes(x=time,y=conc,color=species,linetype=species))+geom_line()
p=p+geom_line(data=tmpexp,aes(x=time,y=conc,color=species,linetype=species))
p=p+geom_point(data=tmpexp,aes(x=time,y=conc,color=species))
p=p+scale_linetype_manual(values=c(0,1,0,1,0,1))
p=p+scale_color_manual(values=rep(c("red","blue","green"),each=2))+theme_bw()
print(p)
  
# get points for a circle with radius r
conf = .95
countParameters = 2
dataPointCount=60
r=sqrt(qf(conf,countParameters,dataPointCount-countParameters)*2)
theta=seq(0,2*pi,length.out=100)
z=cbind(r*cos(theta),r*sin(theta))

# transform points of circle into points of ellipse using
# svd of inverse covariance matrix
Sinv=solve(S)
Sinv_svd=svd(Sinv) # inverse of covariance matrix
xt=t(Sinv_svd$v)%*%diag(1/sqrt(Sinv_svd$d))%*%t(z) # transform from circle to ellispse
x=t(xt)

# translate the ellipse so that center is the estimated parameter value
x=x+matrix(rep(as.numeric(parest),100),nrow=100,byrow=T)

plot(x[,1],x[,2],type="l",xlab="k1",ylab="k2",lwd=2)
points(parest$k1,parest$k2,pch=20,col="blue",cex=2)