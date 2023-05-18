from time import sleep
from multiprocessing.pool import Pool
import random
 
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
        #results = pool.imap(task, range(20), chunksize=10)
        #results = pool.imap_unordered(task, range(40), chunksize=10)
        
        # shutdown the process pool
        pool.close()
        # wait for all issued task to complete
        pool.join()
        
        
    for result in results:
        print(result)
        
    print(type(results))
    print(type(result))