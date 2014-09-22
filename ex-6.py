def pairwiseScore(seqA, seqB):
	flag = False
	score = 0
	seqC = []
	for i in range(len(seqA)):
		if seqA[i] == seqB[i]:
			if flag == False:
				flag = True
				score += 1

			else:
				score += 3
			seqC.append("|")
		else:
			flag = False
			score = score-1
			seqC.append(" ")
	seqD = "".join(seqC)
	return "%s\n%s\n%s\nScore: %s" % (seqA, seqD, seqB, score)

print pairwiseScore('ATTCGT','ATCTAT')
print pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")