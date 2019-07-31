SHOW_ERROR_DATA = False
def go_to(dataObject, path):
    if path == "":
        return dataObject
    path_array = path.split("/")
    for path_element in path_array:
        try:
            dataObject = dataObject.get(path_element)
        except AttributeError:
            dataObject = dataObject[int(path_element)]
    return dataObject

def process(dataObject, processDefinition):
    if processDefinition == []:
        return True;
    [dataPath, whatToDo, functionToCall, nextProcess] = processDefinition
    data = go_to(dataObject, dataPath)
    if whatToDo == "loop":
        # print("loop")
        for item in data:
            if functionToCall is not None:
                processedData = functionToCall(item)
            else:
                processedData = item
            process(processedData, nextProcess)
    elif whatToDo == "process":
        # print("process")
        if functionToCall is not None:
            processedData = functionToCall(data)
        else:
            processedData = dataObject
        process(processedData, nextProcess)
    else:
        pass
