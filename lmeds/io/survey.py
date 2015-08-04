'''
Created on Nov 17, 2013

@author: timmahrt
'''

import codecs

alpha = lambda num: unichr(num + 96)  # ASCII section for lowercase alpha
numTypeList = [int, alpha]


class SurveyItem(object):
    
    def __init__(self):
        self.idNum = None  # The absolute id number of this item
        self.depth = None
        # The id num of this item relative to the group its in
        self.enumStrId = None
        self.text = None
        self.widgetList = []


def recParseSurveyFile(dataList, currentDepth):
    retList = []
    i = 0
    currentItem = SurveyItem()
    numType = numTypeList[currentDepth]
    currentItemNum = 1
    
    while i < len(dataList):
        
        if dataList[i][:2] == "<s":  # Sublist start
            tmpI, tmpSubList = recParseSurveyFile(dataList[i + 1:],
                                                  currentDepth + 1)
            retList.extend(tmpSubList)
            i += tmpI + 1
            
        elif dataList[i][:3] == "</s":  # Sublist end (exit while loop)
            if currentItem.idNum is not None:
                retList.append(currentItem)
                currentItemNum += 1
                currentItem = SurveyItem()
            i += 1
            break
            
        elif dataList[i] != "":  # Datafull entry
            if currentItem.idNum is None:
                strChar = str(numType(currentItemNum))
                currentItem.enumStrId = strChar
                currentItem.depth = currentDepth
                currentItem.text = dataList[i]
                currentItem.idNum = i
            else:
                splitList = dataList[i].split(" ", 1)
                if len(splitList) > 1:
                    elemType, tail = splitList
                    argList = [arg.strip() for arg in tail.split(",")]
                else:
                    elemType = splitList[0]
                    argList = []
                
                currentItem.widgetList.append((elemType, argList))
            
            if currentItem.text != "None":
                i += 1
            
        else:  # Blank line
            # We are transitioning to a new item
            if currentItem.idNum is not None:
                retList.append(currentItem)
                if not all([row[0] == "None"
                            for row in currentItem.widgetList]):
                    currentItemNum += 1
                currentItem = SurveyItem()
            else:  # Extraneous blank line
                pass
            i += 1
            
    return i, retList


def parseSurveyFile(fn):
    data = codecs.open(fn, "rU", encoding="utf-8").read()
    dataList = data.splitlines()
    dataList += [""]  # Parser requires a trailing blank line
    
    itemList = recParseSurveyFile(dataList, 0)[1]
    
    return itemList


if __name__ == "__main__":
    
    a = parseSurveyFile("/Users/tmahrt/Sites/tests/percept_is/postsurvey.txt")
    
    for x in a:
        print("%s, %s" % (x.enumStrId, x.text))
    print('hi')
