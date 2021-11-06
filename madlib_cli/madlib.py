import re
print('===============================================================================')
print('=  in this game the compyter will ask you to enter word(adjectives,noun... )  =')
print('=  then youll see text that may be strange and funny                          =')
print('===============================================================================')

def read_template(path):
    ''' this function read the file '''
    with open(path) as f :
        content = f.read()
    return content

    
def parse_template(path):
    '''this function return all values inside the curly praces'''
    data=re.findall(r'{(.*?)}',path)
    list= tuple(data)
    replaceddata=re.sub(r'{(.*?)}',"{}",path)
    return replaceddata,list
print(parse_template('assets/sample.txt'))

def merge(file , words):  

    """

    """
    testing1=file.format(*words)
    return testing1
    # lst = parse_template(file)  # file is the parsed text which has text and empty{} to put things inside curly braces in te step below
    
    # return (re.sub(r' {[^}]*?}',' {}',file)).format(*words) # we use string.format() to give the string text which have text and empty curly braces values one by one from the values in format 
    #                                         # we put * before the name of array so it will take elements one by one in the array which is (words), then put each value into empty braces
def writeText (file):
    with open('assets/new_sample.txt','w') as f:
        f.write(file)



if __name__ == "__main__":

    fileName=read_template("assets/sample.txt")
    edited=re.findall(r'{(.*?)}',fileName)
    desiredData=[]
    for i in edited:
       inputData=input(f'Please enter a {i} ')
       desiredData.append(inputData)
    entrydata=tuple(desiredData)
    newdata=re.sub(r'{(.*?)}',"{}",fileName)
    writeText(merge(newdata,entrydata))