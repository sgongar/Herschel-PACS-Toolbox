import csv
import sys

obsids = [1342186305, 1342186798, 1342186797, 1342187020, 1342188034,\
          1342188941, 1342189072, 1342188526, 1342189411, 1342187779,\
          1342199407, 1342199420, 1342199415, 1342199238, 1342199748,\
          1342199746, 1342200158, 1342200155, 1342189410, 1342206850,\
          1342214636, 1342214673, 1342220743, 1342220982, 1342220599,\
          1342221384, 1342221386, 1342220751, 1342221382, 1342221362,\
          1342221364, 1342222076, 1342222100, 1342222084, 1342222194,\
          1342222251, 1342222248, 1342223119, 1342222250, 1342223129,\
          1342222765, 1342223104, 1342223124, 1342223106, 1342223102,\
          1342223732, 1342223748, 1342223718, 1342223743, 1342223720,\
          1342223779, 1342224399, 1342224397, 1342224395, 1342223805,\
          1342228534, 1342231427, 1342232601, 1342237582, 1342232561,\
          1342239376, 1342245246, 1342247009, 1342246394, 1342247784,\
          1342247817, 1342249386, 1342249385, 1342249393, 1342249387,\
          1342249392, 1342249390, 1342249391, 1342249384, 1342250904,\
          1342246641, 1342265446, 1342265445, 1342265672, 1342265684,\
          1342265682, 1342265673, 1342265683, 1342265689, 1342265686,\
          1342265674, 1342265676, 1342265681, 1342265675, 1342265685,\
          1342265690, 1342265670, 1342265692, 1342265677, 1342265671,\
          1342265687, 1342265680, 1342265688, 1342265691, 1342265698,\
          1342265697, 1342264210, 1342264211, 1342265700, 1342264217,\
          1342264204, 1342264203, 1342265699, 1342264200, 1342264218,\
          1342264213, 1342264209, 1342264208, 1342264212, 1342264202,\
          1342264206, 1342264214, 1342264201, 1342264216, 1342264205,\
          1342264207, 1342264215, 1342264220, 1342264219, 1342264237,\
          1342264238, 1342265929, 1342265923, 1342265921, 1342265937,\
          1342265952, 1342265928, 1342265934, 1342265924, 1342265938,\
          1342265930, 1342265931, 1342265936, 1342265922, 1342265940,\
          1342265925, 1342265933, 1342265939, 1342265935, 1342265932,\
          1342265927, 1342267182, 1342267177, 1342267178, 1342267185,\
          1342267186, 1342267184, 1342267183, 1342267179, 1342267626,\
          1342267875, 1342267858, 1342267844, 1342267879, 1342267842,\
          1342267881, 1342267843, 1342267859, 1342267874, 1342267870,\
          1342267880, 1342267861, 1342267878, 1342267877, 1342267860,\
          1342270680, 1342270681, 1342209709, 1342209717, 1342229752,\
          1342208907, 1342267869, 1342189612, 1342198300, 1342202589,\
          1342203446, 1342208901, 1342208926, 1342209711, 1342209707,\
          1342210384, 1342210399, 1342210824, 1342210827, 1342210834,\
          1342211537, 1342211693, 1342211842, 1342212220, 1342212600,\
          1342212790, 1342213146, 1342213911, 1342213925, 1342214220,\
          1342225586, 1342225580, 1342225849, 1342225993, 1342234063,\
          1342235692, 1342236271, 1342236272, 1342250999, 1342251177,\
          1342251176, 1342252090, 1342252092, 1342253738, 1342254219,\
          1342254218, 1342254216, 1342254217, 1342254257, 1342254255,\
          1342254256, 1342254275, 1342254274, 1342254280, 1342254298,\
          1342254297, 1342254299, 1342254300, 1342254610, 1342254611,\
          1342254608, 1342254609, 1342254607, 1342254606, 1342254767,\
          1342254620, 1342254616, 1342254617, 1342254618, 1342254619,\
          1342254612, 1342254768, 1342254770, 1342254769, 1342254932,\
          1342254931, 1342254937, 1342256254, 1342256255, 1342256256,\
          1342256248, 1342256766, 1342256763, 1342256477, 1342256784,\
          1342256783, 1342256928, 1342257275, 1342257686, 1342257793,\
          1342259608, 1342262028, 1342262540, 1342262544, 1342262936,\
          1342262945, 1342262958, 1342262967, 1342262981, 1342262976,\
          1342263462, 1342263465, 1342263463, 1342263496, 1342266972,\
          1342266971, 1342266969, 1342266970, 1342266968, 1342266964,\
          1342266922, 1342266976, 1342266975, 1342266974, 1342266973,\
          1342266977, 1342266978, 1342266979, 1342266982, 1342266981]




f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f)
    for i in range(len(obsids)):
        writer.writerow(('leak_region', obsids[i]))
    for j in range(len(obsids_2)):
        writer.writerow(('full_sed', obsids_sed[i]))

finally:
    f.close()

print open(sys.argv[1], 'rt').read()