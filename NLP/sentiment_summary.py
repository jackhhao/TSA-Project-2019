import nlp_summary
import sentiment_analysis
import io

i = input("url: ")

with open("pageContent.txt", "w") as f:
	f.write(sentiment_analysis.main(i))

#nlp_summary.generate_summary("pageContent.txt", len(sentiment_analysis.main(i))/3.0)
