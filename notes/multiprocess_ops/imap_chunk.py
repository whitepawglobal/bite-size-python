from time import sleep
from multiprocessing.pool import Pool
import random
 
"""
Setting number of worker to # of logical cpu: 

By default this equals the number of logical CPUs in your system.
    
For example, if we had 4 physical CPU cores with hyperthreading, this would mean we would have 8 logical CPU cores and this would be the default number of workers in the process pool.

We can set the “processes” argument to specify the number of child processes to create and use as workers in the process pool.
Pool(4)

References: https://superfastpython.com/multiprocessing-pool-num-workers/
"""
# task executed in a worker process
def task(task_identifier) -> int:
    
    # report a message
    print(f'Task {task_identifier}', flush=True)
    # block for a moment
    sleep(random.random())
    # return the generated value
    return task_identifier

# protect the entry point
if __name__ == '__main__':
    
    print("Notice how that the task might be generated in the different order but the result will be in the task order been given because we call imap, use imap_unordered otherwise")
    # create and configure the process pool
    with Pool(4) as pool:
        # issue tasks to the process pool
        #range(20) is okay and list(range(20)) is okay too
        results = pool.imap(task, range(20), chunksize=10)
        #results = pool.imap_unordered(task, range(40), chunksize=10)
        
        # shutdown the process pool
        pool.close()
        # wait for all issued task to complete
        pool.join()
        
        
    for result in results:
        print(result)
        
    print(type(results))
    print(type(result))
