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

<<<<<<< HEAD
		sentiment_analysis.main(i)
		cont = input("cont? ")
		if cont == "no":
			break
	except KeyboardInterrupt:
		print("sorry, don't")
		break
=======
nlp_summary.generate_summary("pageContent.txt", len(sentiment_analysis.main(i))/3.0)
#Summary should be stored in Collection to create Database-like Structure
stockDictionary = {}

>>>>>>> 864e495b18e76d29eb0200fa1e42c75873197215
