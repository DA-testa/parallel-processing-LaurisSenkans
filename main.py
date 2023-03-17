# python3

def parallel_processing(n, m, data):
    output = []
    next_free = [0] * n 
    thread_jobs = [i for i in range(n)] 
    
    for i in range(m):
        
        min_time = min(next_free)
        thread_index = next_free.index(min_time)
        
        output.append((thread_index, next_free[thread_index]))
        
        next_free[thread_index] += data[i]
        thread_jobs.remove(thread_index)
        
        if i < m-1:
            thread_jobs.append(thread_index)
            
        if not thread_jobs:
            break
    
    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = parallel_processing(n, m, data)
    
    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()