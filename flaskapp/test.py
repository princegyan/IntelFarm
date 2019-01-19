#this is a sub module written to read portions of the collector file
#please refer to the collector file
'''
    Prince Alfred Gyan
    Effa Amponsah
'''
with open('reading.embs') as file:
    for i in file:
        parts = i.split()
        if len(parts) > 1:
            print parts[0][:5], parts[1][:5]  #prints the fourth column of the file