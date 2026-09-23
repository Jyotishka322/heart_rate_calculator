#Heart-rate classification module.


def classify_heart_rate(heart_rate, low_limit=60, normal_limit=100):
    #Classify the calculated BPM using the same ranges used in the original project.
    if heart_rate < low_limit:
        print( "Below 60 BPM")
    elif heart_rate <= normal_limit:
        print( "60-100 BPM")
    else:
        print( "Above 100 BPM")
