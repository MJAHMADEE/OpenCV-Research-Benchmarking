import numpy as np
from statistics import mean 
import matplotlib
import matplotlib.pyplot as plt
resultList = []
resultList.append([(15, 7702, 16902, 25093, 30879, 34489), (37, 20010, 33691, 39065, 42173, 44266), (5, 7355, 16797, 19453, 21097, 22469), (3, 3437, 9323, 12508, 14713, 16372), (39, 6371, 16677, 26384, 32470, 36836), (0, 4113, 10714, 14094, 16014, 17123), (3, 5292, 12793, 19456, 25235, 29355)])
resultList.append([(3, 8328, 20100, 27169, 31582, 34098), (8, 11117, 27463, 35415, 39820, 42128), (1, 3590, 12012, 15536, 18064, 20328), (0, 1956, 7799, 11222, 14566, 17293), (4, 4661, 14335, 23808, 30405, 34540), (0, 3277, 7747, 10400, 12858, 14279), (7, 5692, 14766, 21864, 27740, 31487)])
resultList.append([(27, 13239, 25323, 32312, 36625, 39992), (62, 23698, 34350, 40090, 42478, 45129), (26, 10731, 16246, 19867, 20686, 21263), (28, 6913, 9976, 13048, 15707, 17504), (10, 7863, 19685, 30278, 37210, 40971), (13, 5444, 9477, 11553, 12356, 12851), (11, 5302, 15690, 23698, 28967, 32873)])
resultList.append([(46, 14572, 23201, 28833, 32469, 36592), (114, 20931, 32817, 36716, 39187, 40818), (17, 10418, 17664, 19948, 21423, 22065), (33, 6460, 10508, 13813, 15844, 17591), (11, 7929, 21109, 30161, 35405, 38976), (14, 6740, 11900, 13275, 13934, 14657), (4, 8671, 18100, 24007, 28125, 31506)])
resultList.append([(2, 7908, 20935, 28370, 33033, 35771), (7, 11078, 26131, 35089, 40205, 43207), (0, 3788, 11375, 15466, 18247, 20258), (0, 1494, 6404, 9785, 12954, 15424), (3, 5347, 16816, 25756, 32079, 35731), (6, 3060, 8294, 11920, 14397, 16009), (5, 5633, 13589, 20085, 24554, 28557)])
resultList.append([(10, 10881, 23176, 31199, 34634, 37158), (17, 17250, 34146, 40544, 43611, 46592), (1, 6785, 16592, 20357, 22166, 23530), (6, 3362, 8689, 11478, 13495, 15534), (2, 5049, 16959, 25813, 32090, 36533), (1, 2457, 7507, 11014, 13155, 14777), (1, 5221, 13012, 19501, 24544, 28646)])
resultList.append([(18, 13416, 25387, 32915, 36479, 39505), (50, 21833, 33592, 39592, 42061, 43555), (19, 9830, 17522, 21086, 22375, 23705), (21, 5997, 9655, 12532, 14983, 16827), (12, 9076, 20015, 27390, 33264, 37449), (8, 6222, 10792, 12625, 13255, 13661), (7, 6413, 15969, 22969, 28076, 32004)])
#resultList.append([(58260, 34129, 23099, 13752, 2500, 12), (58260, 43177, 34814, 23666, 5996, 6), (58260, 21767, 17941, 13874, 3466, 5), (58260, 17552, 13107, 8305, 1056, 0), (58260, 38136, 23244, 10417, 1826, 4), (58260, 17005, 13640, 8818, 1096, 0), (58260, 25150, 15991, 7867, 1452, 0)])
#resultList.append([(58260, 34843, 26410, 15054, 1730, 1), (58260, 41992, 32384, 20207, 2002, 0), (58260, 20642, 16563, 12366, 1625, 1), (58260, 19722, 13861, 8672, 528, 0), (58260, 35893, 23036, 9659, 1046, 3), (58260, 15858, 12473, 8144, 1024, 0), (58260, 29856, 19174, 9272, 1697, 2)])
#resultList.append([(58260, 41781, 31931, 19181, 6055, 2), (58260, 44509, 35380, 25752, 9154, 2), (58260, 20504, 17127, 13971, 6697, 1), (58260, 18400, 13578, 9678, 4884, 0), (58260, 39516, 26861, 13201, 3052, 0), (58260, 13090, 10638, 7754, 3079, 0), (58260, 30982, 20221, 8604, 1675, 0)])
#resultList.append([(58260, 37987, 28036, 16852, 6634, 3), (58260, 41182, 33612, 22965, 9579, 22), (58260, 21290, 18043, 14197, 6005, 0), (58260, 17554, 14021, 9364, 4330, 0), (58260, 40588, 26383, 11619, 2588, 0), (58260, 14663, 12425, 9099, 2868, 0), (58260, 31131, 21799, 9962, 1423, 0)])
#resultList.append([(58260, 37398, 27547, 16279, 1650, 0), (58260, 42649, 34682, 22686, 940, 0), (58260, 20354, 16513, 12321, 666, 0), (58260, 18652, 11815, 7098, 243, 0), (58260, 37611, 25886, 10752, 861, 0), (58260, 16583, 12212, 7358, 682, 0), (58260, 27850, 17632, 8770, 1826, 2)])
#resultList.append([(58260, 36912, 29065, 16975, 1626, 0), (58260, 46762, 37257, 25414, 3863, 1), (58260, 23023, 19530, 14151, 1862, 0), (58260, 16396, 11904, 7299, 1165, 0), (58260, 37597, 23888, 9003, 1112, 0), (58260, 16035, 12877, 6586, 379, 0), (58260, 26363, 17741, 7684, 1356, 0)])
#resultList.append([(58260, 40092, 31442, 19997, 5119, 2), (58260, 43763, 36923, 27095, 9130, 14), (58260, 23316, 19958, 14681, 5327, 0), (58260, 17662, 12650, 8660, 3329, 0), (58260, 39748, 24964, 11929, 2237, 0), (58260, 13619, 11599, 8347, 2117, 0), (58260, 30040, 20585, 10526, 1483, 2)])


k = 0
sums = []
for i in range(len(resultList)): 
    currsum = [0.,0.,0.,0.,0.,0.]
    for j in range(len(resultList[i])): 
        print(resultList[i][j])
        for k in range(len(resultList[i][j])): 
            currsum[k] += resultList[i][j][k]
    print('====================================')
    for j in range(len(currsum)): 
        currsum[j] /= len(resultList[i])
    print(str(currsum))
    sums.append(currsum)
    print ('\n')


x = np.arange(0, 51, 10)

# normalize values from 0 to 1
for i in range(len(sums)):
    divisor = sums[i][-1] 
    for j in range(len(sums[i])): 
        sums[i][j] /= divisor
print("sums = " + str(sums))

trackerList = ['Boosting', 'CSRT', 'KCF', 'MedianFlow', 'MIL', 'MOSSE', 'TLD']


# add labels 
plt.xlabel('Location error threshold')
plt.ylabel('Precision')
plt.title('Average Precision plots of SRE')

# plot each tracker
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i in range(len(trackerList)): 
    plt.plot(x, sums[i], color[i], label=(trackerList[i]) + ' [' + str(round(mean(sums[i]), 3)) + ']')
plt.legend()
plt.savefig('./Plots/SREPlots/SREPrecisionPlotAverage.eps', format='eps')
plt.show()
 