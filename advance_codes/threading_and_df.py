import pandas as pd
import threading

# Example DataFrame
data = {'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# Example function to process a row
def unitIteration(a):
    # print(f"Processing: {a['col1']}")
    pass

# Multithreading
threadList = []
maxThreadCount = 3

for index, row in df.iterrows():
    print("print","{",index, row ,"}")
    exit(0)
    thread = threading.Thread(target=unitIteration, kwargs={'a': row})
    thread.start()
    threadList.append(thread)

    while len(threadList) == maxThreadCount:
        for thr in threadList:
            if not thr in threading.enumerate():
                threadList.remove(thr)

# Wait for all threads to complete
for thread in threadList:
    thread.join()
