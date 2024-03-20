### Memory profile to count memory per command line and number of occurences

```
pip install memory_profiler
```


#TLDR

- Add 
  ```
  from memory_profiler import profile
  ```
- Add decorator `@profile` to function to profile
  ```
  @profile
  def func()
  ```
- And run normally


<img src="metadata/memory.png" width="500">


<img src="metadata/memory_with_slots.png" width="500">