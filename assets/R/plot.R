code.directory <- "~/Github/TSA-Project-2019/assests/R/plot"
options("getSymbols.warning4.0"=FALSE)
args <- commandArgs(trailingOnly = TRUE)
file.create("TSA_METHOD_1", to = code.directory)
print(dir(code.directory))
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
stock <- function(start_date, end_date, ticker){
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
  x<-na.omit(getSymbols(ticker,src = "yahoo", from = start.date, to = end.date+1, auto.assign = FALSE))
  #View(x)
  Sys.sleep(5)
  s <- paste(ticker, ".Close", sep = "", collapse ="")
  new.value <- x[, s]
  #View(new.value)
  Sys.sleep(5)
  return(plot(new.value, main = paste("Ticker Symbol: ", ticker), col = "black"))

}
print(getwd())
setwd("./assets/images")
#mypath <- file.path("","Users","raviraghavan","Downloads" ,paste("myplot_", ticker, ".jpg", sep = ""))
print(getwd())
jpeg(paste(fileName, ".jpg", sep = ""), width = 450, height = 450)
print(stock(start_date, end_date, ticker))
dev.off()
