import nlp_summary
import sentiment_analysis
import io
while True:
	try:
		i = input("url: ")

		"""
		with open("pageContent.txt", "w") as f:
			f.write(sentiment_analysis.main(i))

		nlp_summary.generate_summary("pageContent.txt", len(sentiment_analysis.main(i))//3)
		"""

		sentiment_analysis.main(i)
		cont = input("cont? ")
		if cont == "no":
			break
	except KeyboardInterrupt:
		print("sorry, don't")
		break
