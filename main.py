import GoogleFitness
import AppleHealthXmlParser
import sys

weightRecords = []
stepRecords = []
distanceRecords = []
heartRateRecords = []
sleepRecords = []

records = AppleHealthXmlParser.parse(sys.argv[1]);

print("XML file parsed.")

for record in records:
	if record.recordType == "HKQuantityTypeIdentifierBodyMass":
		weightRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierStepCount":
		stepRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierDistanceWalkingRunning":
		distanceRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierHeartRate":
		heartRateRecords.append(record)
	if record.recordType == "HKCategoryTypeIdentifierSleepAnalysis":
		sleepRecords.append(record)

print("Creating Data Sources...")

# weightDataSource = GoogleFitness.createWeightDataSource()
# print("Weight Data Source: " + str(weightDataSource))
stepDataSource = GoogleFitness.createStepDataSource()
print("Step Data Source: " + str(stepDataSource))
# distanceDataSource = GoogleFitness.createDistanceDataSource()
# print("Distance Data Source: " + str(distanceDataSource))
# heartRateDataSource = GoogleFitness.createHeartRateDataSource()
# print("Heart Rate Data Source: " + str(heartRateDataSource))
# sleepDataSource = GoogleFitness.createSleepDataSource()
# print("Sleep Data Source: " + str(sleepDataSource))

print("Finished creating Data Sources.")

# if weightDataSource and len(weightRecords) > 0 :
# 	print("Sending Weight Records...")
# 	GoogleFitness.sendPoints(weightDataSource, weightRecords)

if stepDataSource and len(stepRecords) > 0 :
	print("Sending Step Records...")
	GoogleFitness.sendPoints(stepDataSource, stepRecords)

# if distanceDataSource and len(distanceRecords) > 0 :
# 	print("Sending Distance Records...")
# 	GoogleFitness.sendPoints(distanceDataSource, distanceRecords)

# if heartRateDataSource and len(heartRateRecords) > 0 :
# 	print("Sending Heart Rate Records...")
# 	GoogleFitness.sendPoints(heartRateDataSource, heartRateRecords)

# if sleepDataSource and len(sleepRecords) > 0 :
# 	print("Sending Sleep Records...")
# 	GoogleFitness.sendPoints(sleepDataSource, sleepRecords)