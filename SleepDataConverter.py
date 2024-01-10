from Record import Record

def convertEnum(value):
    'Converts a AppleHealth Sleep Enum into a GoogleFit Sleep Enum Int Value'
    if value == "HKCategoryValueSleepAnalysisAsleepUnspecified":
        return 2
    elif value == "HKCategoryValueSleepAnalysisInBed":
        return 3
    elif value == "HKCategoryValueSleepAnalysisAsleepCore":
        return 4
    elif value == "HKCategoryValueSleepAnalysisAsleepDeep":
        return 5
    elif value == "HKCategoryValueSleepAnalysisAsleepREM":
        return 6
    elif value == "HKCategoryValueSleepAnalysisAwake":
        return 1

def createRecord(recordType, startTime, endTime, value):
    'Creates a Sleep Record'
    return Record(recordType, startTime, endTime, convertEnum(value))