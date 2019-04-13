code.directory <- "~/Github/TSA-Project-2019/assests/R/CandleChart"
options("getSymbols.warning4.0"=FALSE)
args <- commandArgs(trailingOnly = TRUE)
file.create("TSA_METHOD_2", to = code.directory)
print(dir(code.directory))
print(args[1])
print(args[2])
print(dev.list())
code.files <- dir(code.directory, pattern = "[.r]")
for (file in code.files){
  source(file = file.path(code.dir,file))
}
#install.packages("quantmod")
require("quantmod")
library("quantmod", character.only = TRUE)
start_date <- args[1]
end_date <- args[2]
ticker <- args[3]
fileName <- args[4]
stock_part2 <- function(start_date, end_date, ticker){
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
  y<-na.omit(getSymbols(ticker,src = "yahoo", from = start.date, to = end.date+1, auto.assign = FALSE))
  t <- paste(ticker, ".Close", sep = "", collapse ="")
  z.frame <- data.frame(y[, t])
  z.frame$DATE <- as.Date(rownames(z.frame))
  z.frame <- z.frame[, c(2,1)]
  rownames(z.frame) <- NULL
  #View(z.frame)
  Sys.sleep(2)
  candleChart(as.xts(data.frame(y)),up.col = "green", down.col = "red", theme = "white", name = ticker)
  a <- 0
  b <- 0
  for (i in seq_along(z.frame$DATE)) {
    if(z.frame$DATE[i] == start.date){
      a <- i
    }else if(z.frame$DATE[i] == end.date){
      b <- i
    }
  }
  #print (a)
  #print (b)
  #print( (b-a) >= 19)
  if( (b-a) >= 19){
    plot(addSMA(n = c(20)))
  }
}
#stock_part2(start_date, end_date, ticker)
setwd("./assets/images")
print(getwd())
jpeg(paste(fileName, ".jpg", sep = ""), width = 450, height = 450)
print(stock_part2(start_date, end_date, ticker))
dev.off()
