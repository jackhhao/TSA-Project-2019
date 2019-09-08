code.directory <- "~/Documents/TSA-Project-2019/assets/R/forecast.R"
options("getSymbols.warning4.0"=FALSE)
args <- commandArgs(trailingOnly = TRUE)
#file.create("TSA_METHOD_3", to = code.directory)
print(dir(code.directory))
code.files <- dir(code.directory, pattern = "[.r]")
for (file in code.files){
  source(file = file.path(code.dir,file))
}
require("quantmod")
require("gridExtra")
library("quantmod", character.only= TRUE)
library("gridExtra", character.only = TRUE)
print("Please enter dates that are at least 20 days apart")
start_date <- args[1]
end_date <- args[2]
ticker <- args[3]
fileName <- args[4]
forecast <- function(start_date,end_date,ticker){
  start.date = as.Date(start_date)
  end.date = as.Date(end_date)
  if(weekdays(start.date) == "Saturday"){
    start.date = start.date - 1
  }else if(weekdays(start.date) == "Sunday"){
    start.date = start.date + 1
  }
  if(weekdays(end.date) == "Saturday"){
    end.date = end.date - 1
  }else if(weekdays(end.date) == "Sunday"){
    end.date = end.date + 1
  }
  #print(end.date)
  x<-na.omit(getSymbols(ticker,src = "yahoo", from = start.date, to = end.date+1, auto.assign = FALSE))
  s <- paste(ticker, ".Close", sep = "", collapse ="")
  y.frame <- data.frame(x[, s])
  y.frame$DATE <- as.Date(rownames(y.frame))
  y.frame <- y.frame[, c(2,1)]
  rownames(y.frame) <- NULL
  #View(y.frame)
  Sys.sleep(5)
  set.seed(123)
  a <- y.frame[, s]
  new.y.frame <- data.frame(
    DATE = end.date + c(1:30),
    col2 = a[length(a)] + rnorm(30, mean = sd(a[(length(a) - 10)]:length(a)), sd = (sd(a[(length(a) - 10)]:length(a))*0.10))
  )
  colnames(new.y.frame)[2] <- s
  v <- vector(mode = "numeric", length = 0)
  for (i in seq_along(new.y.frame$DATE)){
    if (weekdays(new.y.frame$DATE[i]) == "Saturday" |weekdays(new.y.frame$DATE[i]) == "Sunday" ){
      v <- c(v, i)
    }
  }
  new.y.frame <- new.y.frame[-v, ]
  final.y.frame <- data.frame(
    DATE = new.y.frame$DATE,
    col2 = new.y.frame[, 2]
  )
  colnames(final.y.frame)[2] <- s
  return(final.y.frame)
  #Sys.sleep(5)
  #final.y.frame <- rbind(y.frame, new.y.frame)
  #return(final.y.frame)
  #Sys.sleep(5)
}
#forecast(start_date, end_date, ticker)
setwd("./assets/images")
#mypath <- file.path("","Users","raviraghavan","Downloads" ,paste("myplot_", ticker, ".jpg", sep = ""))
print(getwd())
jpeg(paste(fileName, ".jpg", sep = ""), width = 1000, height = 850)
print(grid.arrange(tableGrob(forecast(start_date, end_date, ticker))))
dev.off()
