import math
def reading_time (mynum_words, myreading_speed):
    if str(mynum_words).isnumeric() == False:
        return "cannot work this out"
    if str(myreading_speed).isnumeric() == False:
        return "cannot work this out"
    mynum_words = int(mynum_words)
    myreading_time = (mynum_words / myreading_speed)
    mynumberofseconds, mynumberofmins = math.modf(myreading_time)
    mynumberofseconds = int(60 * mynumberofseconds)
    mynumberofmins = int(mynumberofmins)
    myreturn = str(mynum_words) + ' words will take ' + str(mynumberofmins) + ' minutes and ' + str(mynumberofseconds) + ' seconds to read.' 
    myreturn = str(mynumberofmins) + 'mins ' + str(mynumberofseconds) + 'seconds'
    return(myreturn)