import requests
import json
from random import randint
import config



def getDataSources():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return True
    else:
        print(r.status_code)
        print(r.content)
        return False


def createStepDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleStepDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "steps",
                    "format": "integer"
                }
            ],
            "name": "com.google.step_count.delta"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print(r.status_code)
        print(r.content)
        return False


def createWeightDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleWeightDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "weight",
                    "format": "floatPoint"
                }
            ],
            "name": "com.google.weight"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print(r.status_code)
        print(r.content)
        return False


def createDistanceDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleDistanceDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "distance",
                    "format": "floatPoint"
                }
            ],
            "name": "com.google.distance.delta"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print(r.status_code)
        print(r.content)
        return False
    
def createHeartRateDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleHeartRateDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "bpm",
                    "format": "floatPoint"
                }
            ],
            "name": "com.google.heart_rate.bpm"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print(r.status_code)
        print(r.content)
        return False
    
def createSleepDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleSleepDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "sleep_segment_type",
                    "format": "integer"
                }
            ],
            "name": "com.google.sleep.segment"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print(r.status_code)
        print(r.content)
        return False

def sendPoints(dataSourceId,records):
    dataPoints = []


    if records[0].recordType == "HKQuantityTypeIdentifierBodyMass":

        for record in records:
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.weight",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": endTimeNanos,
                "value": [
                    {
                        "fpVal": record.value
                    }
                ]
            }
            dataPoints.append(point);

    if records[0].recordType == "HKQuantityTypeIdentifierStepCount":

        for record in records:
            point = {
                "dataTypeName": "com.google.step_count.delta",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": record.endTime*1000000,
                "value": [
                    {
                        "intVal": getValidatedStepCount(record.value, record.startTime, record.endTime)
                    }
                ]
            }
            dataPoints.append(point);

    if records[0].recordType == "HKQuantityTypeIdentifierDistanceWalkingRunning":

        for record in records:
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.distance.delta",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": record.endTime*1000000,
                "value": [
                    {
                        "fpVal": record.value*1000
                    }
                ]
            }
            dataPoints.append(point);
    
    if records[0].recordType == "HKQuantityTypeIdentifierHeartRate" or records[0].recordType == "HKQuantityTypeIdentifierHeartRateVariabilitySDNN":

        for record in records:
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.heart_rate.bpm",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": record.endTime*1000000,
                "value": [
                    {
                        "fpVal": record.value
                    }
                ]
            }
            dataPoints.append(point);
    
    if records[0].recordType == "HKCategoryTypeIdentifierSleepAnalysis":

        for record in records:
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.sleep.segment",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": record.endTime*1000000,
                "value": [
                    {
                        "intVal": int(record.value)
                    }
                ]
            }
            dataPoints.append(point);

    print("Sending " + str(len(dataPoints)))

    chunkSize = 10000
    i = 0
    for points in chunks(dataPoints, chunkSize):
        i = i + 1
        (minStartTime,maxEndTime) = getTimes(points)
        addData(dataSourceId,points,minStartTime,maxEndTime,getPercentComplete(dataPoints,i,chunkSize),False)


def getValidatedStepCount(value, startTimeStamp, endTimeStamp):
    'Google Fit requires the step count to be between 0 and 10 steps per second, so we validate here and send the max if it is over'
    nanoStart = startTimeStamp*1000000
    nanoEnd = endTimeStamp*1000000
    seconds = (nanoEnd - nanoStart)/1000000000
    if value/seconds > 10:
        return 10*seconds
    else:
        return value


def getPercentComplete(dataPoints, i, chunkSize):
    totalChunks = len(dataPoints) // chunkSize
    percentComplete = (i + 1) / totalChunks * 100
    return str(int(percentComplete)) + "%"

def getTimes(dataPoints):
    minStartTime = dataPoints[0]['startTimeNanos']
    maxEndTime = dataPoints[len(dataPoints) - 1]['endTimeNanos']
    for point in dataPoints:
        if point['startTimeNanos'] < minStartTime:
            minStartTime = point['startTimeNanos']
        if point['endTimeNanos'] > maxEndTime:
            maxEndTime = point['endTimeNanos']
    return (minStartTime, maxEndTime)

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def addData(dataSourceId,dataPoints,minStartTime ,maxEndTime, percentComplete,retry):

    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/" + dataSourceId + "/datasets/" +str(minStartTime) + "-"+ str(maxEndTime)

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataSourceId": dataSourceId,
        "minStartTimeNs": minStartTime,
        "maxEndTimeNs": maxEndTime,
        "point": dataPoints
    }

    r = requests.patch(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        print(percentComplete + " :: " + str(len(dataPoints))  + " dataPoints : " + dataSourceId)

        return True
    else:
        print(r.status_code)
        print(r.content)
        if retry:
            print(dataPoints)
            exit()
        for point in dataPoints:
            # Try to add each point individually if the batch fails
            # dump the point to the console so we can see what failed
            addData(dataSourceId,[point],point['startTimeNanos'],point['endTimeNanos'],"RETRY",True)
        return False





