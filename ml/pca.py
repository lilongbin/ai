#! /usr/bin/env python
# coding=utf-8
####################################################
# Author      : longbin
# Created date: 2018-05-06 23:12:17
####################################################

from numpy import *

def loadDataSet(fileName, delim="\t"):
    fd = open(fileName)
    strArr = [line.strip().split(delim) for line in fd]
    datArr = [map(float, line) for line in strArr]
    return mat(datArr)

def replaceNanWithMean(fileName, delim="\t"):
    datMat = loadDataSet(fileName, delim)
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:,i].A))[0], i])
        datMat[nonzero(isnan(datMat[:,i].A))[0], i] = meanVal
    return datMat

def pca(dataMat, topNfeat=9999999):
    # remove meanVals
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals

    # get covMat eigVals, eigVects
    covMat = cov(meanRemoved, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat))

    # use argsort to get topNfeat eigVects
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVects[:,eigValInd]

    # get lower dim data Mat
    lowDDataMat = meanRemoved * redEigVects
    # get reconstructed Mat
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


