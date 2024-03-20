from line_profiler import LineProfiler

def run(file : str):
    # I/O operations
    with open(file, 'r') as f:
        data = f.read()
	
    

if __name__ == '__main__':
    lp = LineProfiler()

    lp_wrapper = lp(run)

    #pass argument to the function
    lp_wrapper('file.txt')
    lp.print_stats()
