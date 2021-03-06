import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    global nFinal


    test_mean = CsvReader("Tests/csv/Mean.csv").data
    test_med = CsvReader("Tests/csv/Median.csv").data
    test_mode = CsvReader("Tests/csv/Mode.csv").data
    test_var = CsvReader("Tests/csv/Variance.csv").data
    test_stddev = CsvReader("Tests/csv/StdDeviation.csv").data

    test_quar = CsvReader("Tests/csv/Quartiles.csv").data
    col_quar = [row["QF"] for row in test_quar]
    col_quar1 = [row["Value1"] for row in test_quar]
    col_quar2 = [row["QF1"] for row in test_quar]

    test_skew = CsvReader("Tests/csv/SkewnessTest1.csv").data
    col1_skewness = [row["Value1"] for row in test_skew]
    col10_skewness = [row["skewness"] for row in test_skew]

    test_sam_corr = CsvReader("Tests/csv/Correlation.csv").data
    col_sam_corr1 = [row["value1"] for row in test_sam_corr]
    col_sam_corr2 = [row["value2"] for row in test_sam_corr]
    col_sam_corr3 = [row["correlation"] for row in test_sam_corr]

    test_pop_corr = CsvReader("Tests/csv/PopulationCorrelation.csv").data
    col1_population = [row["value1"] for row in test_pop_corr]
    col2_population = [row["value2"] for row in test_pop_corr]
    col3_population = [row["population"] for row in test_pop_corr]

    test_mean_dev = CsvReader("Tests/csv/MeanDeviation.csv").data
    test_unitTest = CsvReader("Tests/csv/UnitTestForStatistic.csv").data

    test_z_score = CsvReader("/Tests/csv/ZScore.csv").data
    col_zscore = [row["zscore"] for row in test_z_score]
    col_zscore1 = [row["zscore2"] for row in test_z_score]




    def setUp(self):
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_mean_statistics(self):
        pprint("________Mean________")
        for row in self.test_mean:
            theList = []
            for keys in row.keys():
                if keys != "CalculatedMean":
                    if row[keys] != "-":
                        theList.append(float(row[keys]))

            self.assertEqual(self.Statistics.mean(theList), float(row["CalculatedMean"]))
            self.assertEqual(self.Statistics.result, float(row["CalculatedMean"]))
            print(self.Statistics.result, " equals ", row["CalculatedMean"])

    def test_mean_deviation_statistics(self):
        pprint("________Mean Deviation________")
        for row in self.test_mean_dev:
            theList = []
            for keys in row.keys():
                if keys != "CalculatedMean" and keys != "CalculatedMeanDeviation":
                    theList.append(float(row[keys]))

            self.assertAlmostEqual(self.Statistics.meandeviation(theList), float(row["CalculatedMeanDeviation"]), 5)
            self.assertAlmostEqual(self.Statistics.result, float(row["CalculatedMeanDeviation"]), 5)
            print(self.Statistics.result, " almost equals within 5 decimal places ", row["CalculatedMeanDeviation"])

    def test_median_statistics(self):
        pprint("________Median________")
        for row in self.test_med:
            theList = []
            for keys in row.keys():
                if keys != "CalculatedMedian":
                    if row[keys] != "-":
                        theList.append(float(row[keys]))

            self.assertEqual(self.Statistics.median(theList), float(row["CalculatedMedian"]))
            self.assertEqual(self.Statistics.result, float(row["CalculatedMedian"]))
            print(self.Statistics.result, " equals ", float(row["CalculatedMedian"]))

    def test_mode_statistics(self):
        pprint("________Mode________")
        for row in self.test_mode:
            self.assertEqual(self.Statistics.mode(self.column1), float(row["mode"]))
            self.assertEqual(self.Statistics.result, float(row["mode"]))

    def test_mode_statistics(self):
        pprint("________Median Deviation________")
        for row in self.test_mode:
            theList = []

            for keys in row.keys():
                if keys != "CalculatedMode":
                    if row[keys] != "-":
                        theList.append(int(row[keys]))

            if row["CalculatedMode"] != "No mode found":
                self.assertEqual(self.Statistics.mode(theList), int(row["CalculatedMode"]))
                self.assertEqual(self.Statistics.result, float(row["CalculatedMode"]))
                print(self.Statistics.result, " equals ", int(row["CalculatedMode"]))
            else:
                self.assertEqual(self.Statistics.mode(theList), (row["CalculatedMode"]))
                self.assertEqual(self.Statistics.result, (row["CalculatedMode"]))
                print(self.Statistics.result, " equals ", (row["CalculatedMode"]))

    def test_variance_statistics(self):
        pprint("________Variance________")
        for row in self.test_var:
            theList = [int(row["Value1"]), int(row["Value2"]), int(row["Value3"]), int(row["Value4"]),
                       int(row["Value5"])]
            self.assertEqual(self.Statistics.variance(theList), float(row["Variance"]))
            self.assertEqual(self.Statistics.result, float(row["Variance"]))
            print(self.Statistics.result, " equals ", (float(row["Variance"])))

    def test_standard_deviation_statistics(self):
        pprint("________StandardDeviation________")
        for row in self.test_var:
            theList = [int(row["Value1"]), int(row["Value2"]), int(row["Value3"]), int(row["Value4"]),
                       int(row["Value5"])]
            self.assertAlmostEqual(self.Statistics.stddev(theList), float(row["stddev"]))
            self.assertAlmostEqual(self.Statistics.result, float(row["stddev"]))
            print(self.Statistics.result, " equals ", (float(row["stddev"])))


    def test_skewness_statistics(self):
        pprint("________Skewness________")
        for row in self.test_skew:
            z_list = []
            for x in self.col10_skewness:
                z_list.append(x)
            nFinal = float(z_list[0])
            self.assertAlmostEqual(float(self.Statistics.skewness(self.col1_skewness)), nFinal)
            self.assertAlmostEqual(self.Statistics.result, nFinal)
            #print(self.Statistics.result, " equals ", nFinal)

    def test_quartiles_statistics(self):
        pprint("________Quartiles________")
        for row in self.test_quar:
           z_list = []
           for x in self.col_quar2:
                z_list.append(x)
           nFinal = int(z_list[0]), int(z_list[1]),int(z_list[2])
           self.Statistics.quartiles(self.col_quar1)
           self.assertEqual(self.Statistics.result,nFinal)
        #print(self.Statistics.result, " equals ", nFinal)

    def test_z_score_statistics(self):
        pprint("________ZScore________")
        for row in self.test_z_score:
            z_list = []
            for x in self.col_zscore1:
                z_list.append(x)
            nFinal = float(z_list[0])
            self.assertEqual(self.Statistics.zscore(self.col_zscore), nFinal)
        #print(self.Statistics.result, " equals ", nFinal)

    def test_sample_correlation_statistics(self):
        pprint("________Sample Correlation________")
        for row in self.test_sam_corr:
            z_list = []
            for x in self.col_sam_corr3:
                z_list.append(x)
            nFinal = float(z_list[0])
            self.assertEqual(self.Statistics.samplecorrelation( self.col_sam_corr1,  self.col_sam_corr2),self.Statistics.result )
            self.assertEqual(self.Statistics.result, nFinal)
            #print(self.Statistics.result, " equals ", nFinal)

    def test_Population_correlation_statistics(self):
        pprint("________Population Correlation________")
        for x in self.col3_population:
            if x =='':
                break
            y=float(x)
            self.assertEqual(self.Statistics.populationcorrelation( self.col1_population,  self.col2_population),y )
            self.assertEqual(self.Statistics.result, y)
            #pprint(self.Statistics.result, " equals ", y)

if __name__ == "__main__":
    unittest.main()

