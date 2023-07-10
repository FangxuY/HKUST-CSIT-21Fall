#---
# Title: CS229 project--Goal 1
# Editor: Xiaojuan 
# Date created: 4/15/2021
# Date edited: 6/02/2021
#---

#------------------------Aim 1 predict onset time---------------
df0 <- read.csv("./data/vaers.csv")
# impute 
fun_NA <- function(x){x <- ifelse(is.na(x),0,x)}
# df0 <- as.data.frame(sapply(df0[,62:79],FUN=fun_NA))
df0[,62:79] <- apply(df0[,62:79],2,FUN=fun_NA)
# remove unknown sex/manufactor or age <12 
dfs <- df0[df0$SEX!="U"&df0$VAX_MANU!="UNKNOWN MANUFACTURER"&df0$AGE_YRS>11,]
# dfs <- as.data.frame(sapply(dfs,FUN=fun_NA))
outcome <- "dur"
covariates <- c( "AGE_YRS","SEX", "VAX_MANU", "othermeds", "allergies", "disable",colnames(dfs)[62:79])


# remove missing 
mmat  <-  lm(as.formula(paste(outcome, paste(c(covariates), collapse=" + "), sep=" ~ ")),data=dfs,na.action = na.omit)
if (!is.null(mmat$na.action)) dfs <- dfs[-mmat$na.action,]

fmla <- as.formula(paste0("~0+", paste0( covariates, collapse="+")))
X <- model.matrix(fmla, dfs)
colnames(X)[5] <- "VAX_MANUPFIZER"
Y <- as.numeric(dfs[,outcome])

set.seed(229)

sample <- sample(dim(dfs)[1],dim(dfs)[1]*0.8)
train.X <- X[sample,]
train.Y <- Y[sample]

test.X <- X[-sample,]
test.Y <- Y[-sample]
##-------------OLS------------------
lm.fit <- glm(train.Y~.,data=as.data.frame(train.X))
summary(lm.fit)
lm.pred <- predict(lm.fit,newdata =as.data.frame(test.X))
print(test.mse=sqrt(mean((lm.pred - test.Y)^2)),train.mse=sqrt(mean((lm.fit$residuals)^2)))
sort(lm.fit$coefficients)

##-------------regularized regression------------------
## Lasso
lasso.cv <- cv.glmnet(x=train.X, y=train.Y, alpha=1)
# plot(lasso.cv)
train.mse <- sqrt(lasso.cv$cvm[which(lasso.cv$lambda==lasso.cv$lambda.min)])
# nonzero <- predict(lasso.cv, s ='lambda.min', type = 'nonzero')
# colnames(train.X)[unlist(nonzero)]
lasso.pred <- predict(lasso.cv, s=lasso.cv$lambda.min, newx=as.matrix(test.X))
print(c(train.mse=train.mse, test.mse=sqrt(mean((lasso.pred - test.Y)^2))))
# importance 
coef <- coef(lasso.cv,s = "lambda.min")
rownames(coef)[order(coef)]

## ridge
ridge.cv <- cv.glmnet(x=train.X, y=train.Y, alpha=0)
train.mse <- sqrt(ridge.cv$cvm[which(ridge.cv$lambda==ridge.cv$lambda.1se)])
ridge.pred <- predict (ridge.cv, s=ridge.cv$lambda.min, newx=as.matrix(test.X))
print(c(train.mse=train.mse,test.mse=sqrt(mean((ridge.pred - test.Y)^2))))
# importance 
coef <- coef(ridge.cv,s = "lambda.min")
rownames(coef)[order(coef)]

##-------------random forest ------------------
require(randomForest)
rf.model <- randomForest(train.Y~., data=train.X, importance=TRUE, ntree=500, mtry=8)
rf.pred <- predict(rf.model,newdata=test.X)
test.mse <- mean(sqrt((test.Y-rf.pred)^2))
rf.pred <- predict(rf.model,newdata=train.X)
train.mse <- mean(sqrt((train.Y-rf.pred)^2))
print(c(train.mse=train.mse,test.mse=test.mse))
# importance 
importance(rf.model)[order(-importance(rf.model)[, 1]), ]

##-------------neural network ------------------
require(neuralnet)
nn1=neuralnet(train.Y~., data=train.X, hidden=c(2,1),
              linear.output = FALSE)

Predict=compute(nn1,train.X)
train.mse <-mean(sqrt((train.Y-Predict$net.result)^2))
Predict=compute(nn1,test.X)
test.mse <-mean(sqrt((test.Y-Predict$net.result)^2))
print(c(train.mse=train.mse,test.mse=test.mse))

# plot nn
plot(nn1)

# importance 
weights <- as.data.frame(cbind(colnames(train.X),nn1$weights[[1]][[1]][2:27,1],nn1$weights[[1]][[1]][2:27,2]),)
weights$V4 <- abs(as.numeric(weights$V2))+abs(as.numeric(weights$V3))

library(lattice)
dotplot(factor(weights$V1) ~ weights$V2+weights$V3,xlim=c(-50,50))
dotplot(factor(weights$V1) ~ weights$V4,xlim=c(0,100))