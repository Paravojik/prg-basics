test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]
cor=0
for i in range(len(test_results)):
    if test_results[i]==True:
        cor+=1

fal=len(test_results)-cor
perc=cor/len(test_results)*100





print('TEST STATISTICS')
print('===============')
print('Number of questions:', len(test_results))
print('Number of correct answers:', cor)
print('Number of incorrect answers:', fal)
print('Percentage of correct answers:', round(perc,2))

