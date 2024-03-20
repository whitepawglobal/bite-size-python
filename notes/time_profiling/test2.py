from line_profiler import LineProfiler

profiler = LineProfiler()

def profile(func):
    def inner(*args, **kwargs):
        profiler.add_function(func)
        profiler.enable_by_count()
        return func(*args, **kwargs)
    return inner

@profile
def run(file : str):
    # I/O operations
    with open(file, 'r') as f:
        data = f.read()
	
    

if __name__ == '__main__':
    run("file.txt")
    profiler.print_stats()
