import sys

def probOfStreak(numCoins, minHeads, headProb, saved=None):
	if saved == None: saved = {}
	ID = (numCoins, minHeads, headProb)
	if ID in saved:
		return saved[ID]
	else:
		if minHeads > numCoins or numCoins <= 0:
			result = 0
		else:
			result = headProb ** minHeads
			for firstTail in range(1, minHeads+1):
				pr = probOfStreak(numCoins-firstTail, minHeads, headProb, saved)
				result += (headProb ** (firstTail-1)) * (1 - headProb) * pr
		saved[ID] = result
		return result

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print('Usage: %s <number of trials> <minimum streak> <win probability>'%sys.argv[0])
		sys.exit()
	sys.setrecursionlimit(2000)
	print (str(round(probOfStreak(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])),6)))