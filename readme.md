## Bite-Size Python



<p align="left">
<img alt="project status: active" src="https://img.shields.io/badge/Project%20Status-%F0%9F%94%A5Active-brightgreen">

</p>

## Package Installation

**Install package with pip**  Num
`pip install <package-name>`. Example:`pip install numpy`


- For more pip commands, check out [pip guidelines document](pip-guidelines.md)

**Install package with conda**

`conda install <package>`. Example: `conda install numpy`

- For more conda commands, check out [conda guidelines document](conda-guidelines.md)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- [Basic](#basic)
- [Intermediate](#intermediate)
- [Advanced](#advanced)
- [Software Development](#software-development)
- [Machine Learning](#machine-learning)
- [Medium Posts](#medium-posts)


## Basic

### Comment
  
- Single Line Comment: `//sample text`
- Multi Lines Comment:
  ```
   """
   Hello World!
   Nice to meet all of you cookie monsters!
   """
  ```

### Boolean Operator

- bool from int (0, 1): `bool(0) / bool(1)`
- [X and Y](notes/boolean_operator/boolean_options.ipynb)
- [X or Y](notes/boolean_operator/boolean_options.ipynb)
- [if not X](notes/boolean_operator/boolean_options.ipynb)
- [custom object boolean](notes/boolean_operator/boolean_for_object.ipynb)

### [Maths](notes/math)

- [Define Nan, Infinite](notes/math/define_nan_infinite.ipynb)
- Sum up an array: `sum(arr)`
- Max, returns maximum between two value: `max(a, b)`
- Min, returns minimum between two value: `min(a, b)`
- Atan2: `import math; math.atan2(90, 15)`
- Asin: `import math; math.asin(0.5)`
- Sin: `import math; math.sin(1)`
- Cos:`import math; math.cos(1)`
- Factorial: `import math: math.factorial(1)`
- Round up a number to a certain decimal point: `round(value, 1)`
- [Calculate percentile](notes/math/percentile.ipynb)
- Power of a number: `pow(base_number, exponent_number`
- Square root of a number: `sqrt(number)`
- Ceiling
  ```
  import math
  value : int = math.ceil(invalue)
  ```
- Floor
  ```
  import math
  value : int = math.floor(invalue)
  ```
- Logarithm / Log
  - Log to the base of 2:
    - Numpy: `import numpy as np; np.log2(10)` 
    - Math: `import math; math.log2(10)`
    - [Plotting of log to the to the base of 2](notes/math/logn_plotting.ipynb)
  - Log to the base of 10:
    - Math: `import math; math.log10(10)`
- [Exclusive Or (XOR)](notes/math/xor.ipynb)
  - [Swap two numbers with XOR](notes/math/xor_swapping.ipynb)

### Math-others
- [Unique combination pair](notes/math/unique_combination_pair.ipynb)

### Sorting
- [Quick Sort](notes/sorting/quicksort.ipynb)
- [Sort and get the index](notes/sorting/sort_and_get_index.ipynb)

### Data Types

#### Integer
- Get maximum: `import sys; sys.maxsize`
- Get minimum: `import sys: -sys.maxsize - 1`
    
#### Floating Value (float, double)

- Format floating value to n decimal: `"%.2f" % floating_var` / `print("{:.2f}".format(a))` 

#### Bytes

**Notes:**

```
Difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified (immutable), 
and bytearray() returns an object that can be modified (mutable).
```

- [Numpy <> Bytes, Bytes <> Numpy](notes/numpy/np2bytes.ipynb)
- [Bytes -> String](notes/string/bytes2string.ipynb): `bytesobj.decode("utf-8")`
- String -> Bytes: `strobj.encode("utf-8")`
- [Bytes -> Multimedia file (video/audio))](notes/bytesops/readme.md)
- [Check bytes encoding](notes/bytearrayops/checkbytesarrayencoding.ipynb)
- To Bytes: `bytes(<value>)`
- Get size of bytes object: `import sys;sys.getsizeof(bytesobject)`
- [Split bytes to chunks](notes/bytesops/bytestochunk.ipynb)
  - The effect is less overhead in transmitting tasks to worker processes and collecting results.
  
#### ByteArray
  
**Notes:**

```
Difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified (immutable), 
and bytearray() returns an object that can be modified (mutable).
```

- [Integer to Bytearray](notes/bytearrayops/bytearraybasic.ipynb)
- [Native Array to Bytearray](notes/bytearrayops/bytearraybasic.ipynb)
- [Numpy Array to Bytearray](notes/bytearrayops/bytearraybasic.ipynb)
- [Image as Bytearray](notes/cv/image_as bytearray.ipynb)
- [Check bytes array encoding](notes/bytearrayops/checkbytesarrayencoding.ipynb)
- To ByteArray: `bytearray(<value>)`
  
#### Numpy
  
- [Numpy basic](notes/numpy/npbasic.ipynb)
   - numpy array with int random value: `np.random.randint(5, size=(2, 4))`
- Check if numpy array has true value: `np.any(<np-array>)`
- Get numpy shape: `nparray.shape`
- Numpy array to list: `nparray.tolist()`
- List to numpy array: `np.array(listarray)`
- Change datatype: `nparray = nparray.astype(<dtype>)` Example: `nparray = nparray.astype("uint8")`
- Numpy NaN (Not A Number): Constant to act as a placeholder for any missing numerical values in the array: `np.NaN / np.nan / np.NAN`
- Numpy multiply by a value: `nparray = nparray * 255`
- [Numpy array to image](notes/pytorch/torchtensor2image.ipynb)
- Numpy array to Torch tensor: `torch.from_numpy(nparray)`
- [Numpy <> Binary File(.npy)](notes/numpy/np2binary.ipynb)
- Print numpy array without scientific notation (e-2)
- Set numpy print options to suppress scientific notation
    ```
    np.set_printoptions(suppress=True, precision=10)
    print(predictions)
    ```
- [Use of `numpy.where`](notes/cv/blur_region.ipynb)
- Get minimum value of numpy array: `np.amin(array)` 
- Get maximum value of numpy array: `np.amax(array)`
- [Calculate euclidean distance with numpy](https://www.geeksforgeeks.org/calculate-the-euclidean-distance-using-numpy/)
- Opencv Numpy array to bytes
  ```
  targetimage : np.array
  success, encoded_targetimage = cv2.imencode(".png", targetimage)
  encoded_targetimage.tobytes()
  ```

  
#### String

- Generate string with parameter
  - [Using template literal](notes/string/paramwithstring.ipynb): `print(f'Completed part {id}')`
  - [Generate string with templates](notes/string/stringtemplate.ipynb)
  - String formatting method: `print('Completed part %d' % part_id)`
  - create string in the raw format: `varname="world"; print(f"Hello {varname!r}")
- Check if string is empty, len = 0: `strvar = ""; if not strvar:`
- Check if string contains digit: `any(chr.isdigit() for chr in str1) #return True if there's digit`
- Check file extension: [notes/string/check_file_extension.ipynb](notes/string/check_file_extension.ipynb)
- Capitalize a string: `strvar.capitalize()`
- Uppercase a string: `strvar.upper()`
- Lowercase a string: `strvar.lower()`
- Capitalize the beginning of each word: `strvar.title()`
- Get substring from a string: `strvar[<begin-index>:<end-index>]` / `strvar[<begin-index>:]` / `strvar[:<end-index>]`
- [Strip multiple white spaces into only one](notes/string/strip_multiple_white_space.ipynb)
- Remove white spaces in the beginning and end: `strvar.strip()`
- Swap existing upper and lower case: `strvar.swapcase()`
- Capitalize every first letter of a word: `strvar.title()`
- Splitting string:
  - Split a string based on separator: `strvar.split(separator)` Example: `strvar.split("x")`
  - Split on white space: `strvar.split()`
  - If split with every character, do this instead: `[*"ABCDE"]` Result: `["A", "B", "C", "D", "E"]`
- Check if string starts with a substring: `strvar.startswith(<substring>)`
- Check if string ends with a substring: `strvar.endswith(<substring>)`
- Check if string have substring/specific character. Returns -1 if not found: `strvar.find(input : str)`, `strvar.find(input: str, start_index : int)`
- String get substring with index: `str[startindex:endindex]`
- Replace string/character with intended string/character: `strout = strin.replace(" ", "_")`
- [Replace multiple characters with intended character](notes/string/replace_multiple_character.ipynb)
- [Replace multiple string with intended string](notes/string/replace_multiple_string.ipynb)
- [Generate string](https://pynative.com/python-generate-random-string/)
- [String to List/Dict:](notes/string/string2list.ipynb) `eval(strinput)`
- List to string: ` <separators>.join(list) example: ', '.join(listbuffer)`

#### Unique Identifer (UUID)

- [Generate unique identifer UUID](notes/uuid/uuidops.ipynb)
- [Validate if a string is UUID](notes/uuid/uuidops.ipynb)
- [Compare if both UUID are the same](notes/uuid/uuidops.ipynb)
- UUID to string: `str(uuidparam)`
- string to UUID: `uuid.UUID(uuid_in_str)`

#### Datetime
- [date, datetime create](notes/formatting/datetime_comparison.ipynb)
- datetime: [datetime.ipynb](notes/formatting/datetime.ipynb)
  - get current local date and time: `datetime.now()`
  - get utc date and time: `datetime.utcnow()`
  - [time to str and reverse](notes/formatting/time_to_str.ipynb)
- [find differences of two datetime: use divmod](https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python)
- [date, datetime comparison](notes/formatting/datetime_comparison.ipynb))
- datetime.timedelta
  <details>
    
  ```
  from datetime import timedelta
  timediff : timedelta =  datetime.now() - before
  print(timediff.microseconds)
  print(timediff.seconds)
  print(timediff.days)
  ```
  
  </details>
- [Convert datetime between different time zone](notes/formatting/convert_timezone.ipynb)
### Data Structure

#### [List](notes/list)
  
- List of str to int: `list(map(int, arr))`
- List with range of values: `list(range(...))`
- Split str to list of str: `arr.split(" ")`
- Find if a value in a list: `if value in mylist:` / `if value not in mylist:`
- Copy by value: `array.copy()` (to not impact changes in array after changing)
- Sort an array in place: `arr.sort()` / Return a sorted array: `sorted(arr)`
  - Sort an array in reverse: `arr.sort(reverse = True)` / Return a sorted array: `sorted(arr, reverse = True)`
- Get index of a value: `arr.index(value)` (When not found will raise ValueError)
- Add one more value to existing list: `arr.append(value)`
- Insert at index: `arr.insert(index, value)`
- Extend list with values in another list: `arr.extend(arr2)`
- Remove an item (the first item found) from the list: `arr.remove(item)`
- Remove item by index: `del arr[index]` or `del arr[index-start: index-end]`
- Check for empty list: `arr = []; if not arr: #empty list`
- Clear a list: `arr.clear()`
- Get list subset: `list[start:stop:step]` example `array[0::2]` `a[0:6:2]`
- Check all items in a list(subset) if exist in another list, returns boolean: `set(b).issubset(v)`
- Check unordered list to have the same items, returns boolean: `set(a) == set(b)`
- Change values of list with **List Comprehension**: `[func(a) for a in sample_list]`
- Iteration of list with index: `for index, value in enumerate(inlist):`
  - Enumerate with a beginning index: `for index, value in enumerate(inlist, 2):` (Index comes as second parameter)
- Iteration over two lists: `[<operation> for item1, item2 in zip(list1, list2)]`
- [Count occurence of items in list](notes/list/countoccurence.ipynb): `array.count(val)` 
- Get maximum value in a list of numbers (even strings): `max(samplelist)`
- [Get argument of minimum / maximum value](notes/list/argument_min_max.ipynb)
- Reverse a list: `list(reversed([1, 2, 3, 4])` / `listinput.reverse()`
- list to string: `",".join(bufferlist)`
- Remove a value in list by index: `returnedvalue = listarray.pop(index)` (Note: Invoke IndexError if index not valid)
  - Remove last value: `listarray.pop()`
    - [Stack Implementation with list](notes/list/stack.ipynb)
    - [Queue Implementation with list](notes/list/queue.ipynb)
- [List Counter](notes/list/array_counter.ipynb)   
  
**Build list**

- Build list of same values: `['100'] * 20 # 20 items of the value '100'`
- Build multiple list into one: `lista + listb + listc`
- Build list by breaking down every character of a string: `[*'abcdef']`
  
#### [Dictionary](notes/dictionary)
  
- [Define dict with str keys](notes/dictionary/definedict.ipynb)
- Define dict from two lists: `dict(zip(list1, list2))`
- Add new key value pair: `dict.update({"key2":"value2"})`
- [Remove key<> value pair by referring to specific key](notes/dictionary/remove_key.ipynb)
- Get keys as list: `list(lut.keys())`
- Get values as list: `list(lut.values())`
- Create dict from list: `{i: 0 for i in arr}`
- Remove existing key: `del keyvalue['key']`
- Remove key<>value: `value = keyvalue.pop(key, alternative-value-if-key-not-present)`
- [Handling missing items in dict](notes/dictionary/nativedict_handlemissingkey.ipynb)
- [Iteration to dict to get keys and values](notes/dictionary/dict_iteration.ipynb)
- [Save/load dictionary to/from a file](notes/dictionary/saveloaddict.ipynb)
- Revert or inverse a dictionary mapping: `inv_map = {v: k for k, v in my_map.items()}`
- [Copy by value](notes/dictionary/dict_copybyvalue.ipynb): `sampledict.copy()`
- [Decompose/unpack dictionary when passing as argument](notes/dictionary/decompose_dict_when_passing_by_param.ipynb)
  - Use case: class declaration
- [Reverse key value pair to build inverse key value pair with zip](notes/dictionary/reverse_dict_for_inverse_keyvaluepair.ipynb)
- [Dictionary to decide class to call with class as value](notes/dictionary/dict_to_decide_class_to_call.ipynb)
- [Change order of key value based on the key/value items](notes/dictionary/dict_reorder.ipynb)

#### [collections.defaultdict]

- [defaultdict introduction](notes/default_dict/default_dict_intro.ipynb)

#### Set
- Set initialization: `setsample = {1,2,3,4,5}`/ `setsample = set()`
- Add item: `setsample.add(<value>)` example `setsample.add((1,2))` (has to be tuple, not list)
- Add multiple items: `setsample.update(<another-set>)`
- [Set with multiple-value input as set](notes/set/set_with_multiple_value_input.ipynb)
- Remove value by index: `setsample.pop(<index>)`
- Remove value by value: `setsample.remove(<index>)`
- Check if value exist in set: `if value in setsample:`

#### Tuple
- Build a tuple: `var : tuple[bool, str | None] = tuple([True, "abc"])`
- List to tuple: `tuple([1,2])`
    
#### Named Tuple
- [NamedTuple](notes/collections_imp/namedtupleimp.ipynb)

#### Applicable to Python Iterables (List, Set,...)

- To identify if any items in the iterables has True/1 values: `any(sample_list) #returns single value True/False`
- [Zip multiple iterables](notes/zipops/zipops.ipynb)

#### JSON
- [Write dict to json file](notes/json/write2json_readfromjson.ipynb)
- [Read dict from json file](notes/json/write2json_readfromjson.ipynb)
- [Str to json](notes/json/str2json.ipynb)

### Security

- [Encrypt and decrypt string](notes/security/encrypt_decrypt.ipynb)
- 
### [Pandas](https://pandas.pydata.org/docs/reference/)

<details>
 
#### Panda Infos

- [Dataframe basic](notes/pandas/info_basic.ipynb)
  - Get # rows and columns
  - Get summary/infos about dataframe
- [Get data types](notes/pandas/column_types.ipynb)
- [Dataframe/Series Min, Max, Median, General Description](notes/pandas/series_min_max.ipynb)
- [Get rows name (index) and columns name (column)](notes/pandas/info_rows_columns.ipynb)
- [Get a glimpse of dataframe](notes/pandas/info_glimpse.ipynb)
- [Get subset of a dataframe by rows/by columns](notes/pandas/df_subset.ipynb)
- [Get rows by finding matching values from a specific column](notes/pandas/df_find_rows.ipynb)
- Check if a column name exist in dataframe - `if 'code' in df.columns:`
- [Iteration of each rows in a dataframe](notes/pandas/iterrows.ipynb)
- Unique counts of a column: `df["prediction"].value_counts()`

#### Panda Operations

- Check if dataframe is empty: `df.empty #return boolean`
- [Get dataframe from list](notes/pandas/list2df.ipynb)
- Build dataframe with columns name
  ```
  column_list = ["a", "b"]
  df = pd.DataFrame(columns = column_list)
  ```
- [Build a new dataframe from a subset of columns from another dataframe](notes/pandas/series_subset.ipynb)
- [Get subset of dataframe, sample columns with specific criteria](notes/pandas/sample_df.ipynb)
  - Sample by percentage
  - Sample by # of rows specified
  - Sample by matching to a value
- [Apply](notes/pandas/apply_helloworld.ipynb)
- Column to list: [`df.columns.tolist()`](notes/pandas/columns2list.ipynb)
- Sample rows: `df = df.sample(frac=1).reset_index(drop=True) `
- [Referring to dataframe column by key or by string](notes/pandas/refer_column_name.ipynb)
- [Concatenate dataframe](notes/pandas/concat_df.ipynb)
  - Concatenate by adding rows
- [Append string to all rows of a column](notes/pandas/append_value_to_row.ipynb)
- Reset index without creating new (index) column: `df.reset_index(drop=True)`
- Assign df by copy instead of reference - [`df.copy()`](notes/pandas/copybyvalue.ipynb)
- Shuffle rows of df: `df = df.sample(frac=1).reset_index(drop=True)`
- [Pandas with multiple index](notes/pandas/pd_multiple_index.ipynb)
- Bytes to dataframe
  ```
    from io import BytesIO
    import pandas as pd

    data = BytesIO(bytesdata)
    df = pd.read_csv(data)
  ```
- Sort values according to particular column
  ```df = df.sort_values(by=['frame'])```
  
- [Rearrange dataframe column sequence](notes/pandas/arrange_cols_sequence.ipynb)  

#### Panda Type

- [Change column type](notes/pandas/change_column_type.ipynb)
  - change type: `df['your_column'] = df['your_column'].astype(int)`
- [Rename column name if exist](notes/pandas/rename_column.ipynb)
- [Compare column type](notes/pandas/comparecoltype.ipynb)

#### Panda Series

- [Series to value](notes/pandas/series_to_values.ipynb)
- Series/Dataframe to numpy array: `input.to_numpy()`
- Series iteration: `for index, item in seriesf.items():`
- Series to dict: `seriesf.to_dict()`

#### Panda Assign values

- [Create new column and assign value according to another column](notes/pandas/assign_column.ipynb)
- [Assign values by lambda and df.assign](notes/pandas/dfassign.ipynb)
- [Dataframe append rows](notes/pandas/df_append_rows.ipynb)

#### Panda Remove/drop values

- [Drop duplicates for df / subset, keep one copy and remove all](notes/pandas/drop_duplicate.ipynb)
- [Remove/drop rows where specific column matched value](notes/pandas/remove_with_matching_value.ipynb)
- [Remove specific columns with column name](notes/pandas/remove_column.ipynb)
- [Drop rows by index](notes/pandas/drop_row_by_index.ipynb)
- Drop rows/columns with np.NaN: `df3 = df3.dropna(axis = 1) #row`
- Drop columns based on specific column with NaN: `df = df.dropna(subset=['your_column_name'])`
#### Panda SQL-like functions

- pivot table: `:TODO`
  - Drawback: Not able to do filtering selection
- [Merge two dataframes based on certain column values](notes/pandas/pdmerge.ipynb)

#### Panda Filtering

- [Filter with function isin()](notes/pandas/isin.ipynb)
- [Filter df with item not in list](notes/pandas/filtervaluenotinlist.ipynb)
- [Filter with function query()](notes/pandas/query.ipynb)
- Find with loc
  - `df.loc[df['address'].eq('johndoe@gmail.com')] #filter with one value`
  - `df.loc[df.a.eq(123) & df.b.eq("helloworld")] #filter with one value in multiple columns`
  - `df.loc[df.a.isin(valuelist)] #filter with a few values in a list`
  - Filter by substring: `df.loc[df['folder'].eq(folderkey) & df['id'].str.contains(videokey)]`
- [Assign value to specific column(s) by matching value](notes/pandas/df_assign_col_values.ipynb)
- Get a subset of dataframe by rows - `df.iloc[<from_rows>:<to_rows>, :]`
- [Count items and filter by counter values](notes/pandas/filter&valuecount.ipynb)
- [Retrieve columns name which match specific str](notes/pandas/filterbysubsetname.ipynb)

#### Panda Excel In/Out

- Read in excel with specific sheet name: `pd.read_excel(<url>, sheet_name = "Sheet1", engine = "openpyxl")`
  - Note: Install engine by `pip install openpyxl`
- [Read number of sheets in excel](notes/pandas/count_excel_sheets.ipynb)
- Save excel: `df.to_excel('file_name', index = False) `
- [Write to multiple sheets](notes/pandas/write_to_multiple_sheets_excel.ipynb)

#### Panda CSV In/Out

- Read csv with other delimiter `pd.read_csv(<path-to-file>, delimiter = '\x01')`
- Read csv with bad lines `pd.read_csv(<path-to-file>, on_bad_lines='skip')`
  - Note: `pd.read_csv(<path>, error_bad_lines = False)` deprecated
- Read csv with encoding `pd.read_csv('file name', encoding = 'utf-8')`
- Save to csv `df.to_csv('file name', index = False)`
  - Note: Put `index = False` is important to prevent an extra column of index being saved.
- Save to csv with encoding `df.to_csv('file name', encoding = 'utf-8')`
- [Write list/dict to csv file](https://www.geeksforgeeks.org/writing-data-from-a-python-list-to-csv-row-wise/) (Note: to not affected by the comma in the collection)
  
#### Panda [Parquet In/Out](notes/pandas/readwriteparquet.ipynb)

- Read in parquet: `pd.read_parquet(...)`
- Write to parquet: `pd.to_parquet(...)`

#### Panda Pickle In/Out

**Note: Pickle have security risk and slow in serialization (even to csv and json). Dont use**

- Read in pickle to dataframe: `df = pd.read_pickle(<file_name>) # ends with .pkl`
- Save to pickle: `df.to_pickle(<file_name>)`

#### Panda Dataframe Others

- [Random dataframe and database table generator](https://github.com/tirthajyoti/pydbgen)

</details>

### Random
- Fixed Random Seed Number (Generate same pattern) : `random.seed(integer_value)` Randomize everytime: `random.seed()`
- Generate random floating value within 0- 1: `from random import random; random.random()`
- Generate random integer within (min, max). Both bound included: `from random import randint; randint(0, 100) #within 0 and 100`
- Generate random floating value: `from random import random; random()`
- Randomly choosing an item out from a list: `import random; random.choice([123, 456, 378])`
  - [Weighted Sampling](notes/sampling/weighted_sampling.ipynb)
- Generate list with random number: `import random; random.sample(range(10, 30), 5)`
  - Example shown where 5 random numbers are generated in between 10 to 30
- Shuffle an array: `random.shuffle(array)`

## Intermediate
  
### Error Handling

- [Native Catching Exception](notes/error_handling/catcherror.ipynb)
  - Catch multiple error: `except (CompileError, ProgrammingError) as e:`
- [Traceback](notes/error_handling/traceback)
- [Suppress and log error](notes/error_handling/suppress_error)

#### [Types of Built-In Exceptions](https://docs.python.org/3/library/exceptions.html)

- [ValueError: argument of the correct data type but an inappropriate value](notes/error_handling/error_types/valueerror.ipynb)
- [TypeError: the data type of an object is incorrect](notes/error_handling/error_types/typeerror.ipynb)
- [IndexError: Raised when a sequence subscript is out of range](notes/error_handling/error_types/indexerror.ipynb)
- [KeyError: When key cannot be found](notes/error_handling/error_types/keyerror.ipynb)
- [ZeroDivisionError: when a number is divided by zero](notes/error_handling/error_handling/error_types/zerodivisionerror.ipynb)
- [OSError: error from an os-specific function](notes/error_handling/error_types/oserror.ipynb)
- [FileNotFoundError: when a file or directory is requested but doesn’t exist](notes/error_handling/error_types/filenotfounderror.ipynb)
- IsADirectoryError: when removing a file but it turns out is a directory with `os.remove(file)`
- [NotImplementedError: commonly raised when an abstract method is not implemented in a derived class](notes/error_handling/error_types/notimplementederror.ipynb)
- [NameError: reference to some name (variable, function, class) that hasn’t been defined](notes/error_handling/error_types/nameerror.ipynb)
- [AttributeError: reference to certain attribute in a class which does not exist](notes/error_handling/error_types/attributeerror.ipynb)
- [ImportError: Trouble loading a module](notes/error_handling/metadata/importerror.jpg)
  - Submodule
    - ModuleNotFoundError: the module trying to import can’t be found or try to import something from a module that doesn’t exist in the module
- AssertionError: Raise when run `assert`
  
### [File System](notes/filesystem)

- The character used by the operating system to separate pathname components: `os.sep`
- [Iterate through a path to get files/folders of all the subpaths](notes/filesystem/filewalk.ipynb)
- Write file: `f.write(str)`
- print without new line: `print(..., end="")`
- Get environment path (second param is optional): `import os; os.getenv(<PATH_NAME> : str, <alternative-return-value>: str)`
- [Get and set environment path](notes/filesystem/environment_setting.ipynb)
  - Set variable: `os.environ['redis'] = "localhost:6379"`
  - Get value with key: ```import os; os.environ["HOMEDIR"]```
  - Get value with default value: ```database_url = os.environ.get("DATABASE_URL", "default-value")```
- [Flush out print](notes/filesystem/stdoutflush.ipynb)
- Check if path is a folder: `os.path.isdir(<path>)`
- Get home path: `os.path.expanduser("~")`
- [Get file size](notes/filesystem/getfilesize.ipynb)
  - `from pathlib import Path; outsize : int = Path(inputfilepath).stat().st_size`
  - `import os; outsize : int = os.path.getsize(inputfilepath)`
- Create folder: `os.mkdir(<path>`
- Create folders recursively: `os.makedirs(<path>)`
- Rename file: `os.rename(<filepath-from>, <filepath-to>)` / `os.rename(<dirpath-from>, <dirpath-to>)`
- Get folder path out of given path with filename: `os.path.dirname(<path-to-file>)`
- Expand home directory: `os.path.expanduser('~')`
- Get current running script path: `os.getcwd()`
- Get the list of all files and directories in the specified directory (does not expand to items in the child folder: `os.listdir(<path>)`
- Get current file path (getcwd will point to the running script(main) path, this will get individually py path): `os.path.dirname(os.path.abspath(__file__))`
- Get filename from path: `os.path.basename(configfilepath)`
- Split extension from rest of path(Including .): `filename, ext = os.path.splitext(path)`
- Append certain path: `sys.path.append(<path>)`
- Check if path exist: `os.path.exists(<path>)`
- Remove a file: `os.remove()`
- Get size of current file in byte: `os.path.getsize(<path>)` or `from pathlib import Path; Path(<path>).stat().st_size`
- Removes an empty directory: `os.rmdir()`
- Deletes a directory and all its contents: `import shutil;shutil.rmtree(<path-to-directory>)`
- [Copy a file to another path](notes/filesystem/copyfile.ipynb)
- [Unzip file](notes/filesystem/uncompresszip.ipynb)
- [Readfile](notes/filesystem/readfile.ipynb)
  ```
  open(<path-to-file>, mode)
  ```
  <details>
    
  - `r`: Open for text file for reading text
  - `w`: Open a text file for writing text
  - `a`: Open a text file for appending text
  - [`b`: Open to read/write as bytes](notes/cv/image_as_byte.ipynb)
    Read file has 3 functions

  - `read()` or `read(size)`: read all / size as one string.
  - `readline()`: read **a single line** from a text file and return the line as a string.
  - `readlines()`: read all the lines of the text file into a list of strings.
  - `write(<param> : str)`: write in param. Need to explicitly add `\n` to split line.
  - `.close()`: close file iterator
  - check if file iterator is closed: `closed`
  </details>


### System

- [Get system input](notes/system/sysinput.py)
- Check operating system: `import platform; platform.system()`
- [Check if port is open/close](notes/system/check_port_open.ipynb)

### Time

- [Measure Time Performance with time.time() / time.perf_counter()](notebooks/performance/count_time.ipynb)
- Add delay to execution of the program by pausing: `import time;time.sleep(seconds)`
  - Note: stops the execution of current thread only
- [Point to a later time from now](notes/performance/update_time.ipynb)

### Plotting
- Matplotlib
  - [Plot with lines & dots](notes/matplotlib/matplotlib_plotting.ipynb)
  
## Advanced

### Class

- [Effective way to view object address and object](notes/class/class_object_view.ipynb)
- [Reserved methods in class](notes/class/reservedMethod.py)
- The magic variable \*args and \*\*kwargs: [Quick Review](notes/class/quick_review_args_kwargs.ipynb) [Elaborated Notes](notes/class/kwargsimp.py)
- [Check if object is of specified type](notes/class/isinstanceimp.ipynb): `isinstance(obj, MyClass)` / `isinstance(obj, (type1, type2) : tuple)`
- [Deep Copy, Shallow Copy](notes/class/deepcopy_shallowcopy.ipynb)
  - Copy list by value: `list_cp = list_ori[:]` (Note: `list_cp = list_ori` copy by reference)
- Define dataclass @dataclass
  - [dataclass 1](notes/class/dataclass/dataclass_helloworld_1.ipynb)
  - [dataclass 2](notes/class/dataclass/dataclass_helloworld_2.ipynb)
  - [dataclass 3](notes/class/dataclass/dataclass3.ipynb)
    - Compare normal class definition with dataclass definition
    - Layout output of __dict__ for dataclass class
  - [dict as constructor input](notes/class/dict_as_constructor.ipynb)
- Enum
  - Enum get key: `obj.name`
  - Enum get value: `obj.value`
  - [Implement Enum in Python](notes/class/enumimpl.ipynb)
    - Compare enum: `value == EnumObject.OPTION1`
    - [Enum with string](notes/class/enum_with_str.ipynb)
    - [str to enum](notes/class/str2enum.ipynb)
  - Get all the values of enum: `[e.value for e in Directions]`
- [Serialize class object](notes/class/serialize_classobj.ipynb)
- [Function/Module with error handling](notes/class/function_with error_handling.ipynb)
- [Identify if function did not return object. TLDR: if not test1()](notes/class/test_if_function_returns_object.ipynb)
- [Compare class object](notes/class/compare_class_object.ipynb)
- [Static Variable](https://favtutor.com/blogs/static-variable-python)
  
#### Magic Method

- [`__dict__` return all attributes of an object(only those defined in __init__): `obj.__dict__`](notes/class/values_in_dict.ipynb)
- `__str__` return string representation of the obj: `def __str__(self):`
- `__eq__` compare the instances of the class: `def __eq__(self, other):`
  - [Define **eq** function in class 1](notes/class/eq_function.ipynb)
  - [Define **eq** function in class 2](notes/class/dataclass/dataclass_helloworld_1.ipynb)
- [`__repr__`: represent a class's objects as a string. Call object with `repr(obj)`](notes/class/magic_repr.ipynb)
- [`__call__`: to make class instance callable `classinstance(variable)`](notes/class/magic_call.ipynb)

## [Regular Expression (Regex)](notes/regex)

- [Find matching word/character 1](notes/regex/charactermatch.ipynb)
  - Introduction of functions in _re_ library
  - Square brackets for upper and lower case `[Ww]oodchuck`
- [Find matching word/character 2](notes/regex/charactermatch2.ipynb)
  - Optional character with `?`
  - Optional 0 or more character with `*`
  - Optional 1 or more character with `+`
  - Any character with `.`
- [Find matching word/character 3](notes/regex/charactermatch3.ipynb)
  - Whitespace character find with `\s`
  - Non-whitespace character find with `\S`
- [Find matching word/character 4](notes/regex/charactermatch4.ipynb)
  - Caret before square bracket:`^[]` to indicate beginning
  - Dollar sign after square bracket:`[]$` to indicate ending
- [Negation](notes/regex/negation.ipynb)
- [Disjunction](notes/regex/disjunction.ipynb)
  - To match a series of patterns with parenthesis.
- [Extract hashtags](notes/regex/filterhashtag.ipynb)
- [Extract numbers from string](notes/regex/extractnumbersfromstr.ipynb)

### Data Structure - Processing iterables with a functional style

- yield instead of return [link1](notes/functional/yield/yieldimp.py) [yield, iterators, generators](notes/yield/yield_imp.ipynb)
- [Produce a new iterable with map()](notes/functional/mapimp.ipynb)
- [Generate a new iterable with Boolean-return function with filter()](notes/functional/filterimp.ipynb)
- [Produce a single cumulative value from iterable with reduce()](notes/functional/reduceimp.ipynb)
- [Condition checking with any(<iterable>)](notes/functional/anyimp.ipynb)
- [Multiple function declaration with singledispatch)](notes/functional/singledispatchimp.ipynb)
- Lambda function: `x = lambda a, b : a * b`
_Note: Functional style can be replaced with **list comprehension** or **generator expressions**_

### Algorithm
- [Number swapping](notes/algorithm/number_swapping.ipynb)
- [Reverse value](notes/algorithm/reverse_value.ipynb)
- [Fibonacci](notes/algorithm/fibonacci.ipynb) [Memoization](notes/algorithm/memoization1.ipynb)
- [Number of Pairs, Number of 3 value combination](notes/algorithm/memoization1.ipynb)
- [Factorial](notes/algorithm/memoization1.ipynb)
- Tree
  - [Breadth First Print](notes/tree/breadth_depth_print.ipynb)
  - [Depth First Print](notes/tree/breadth_depth_print.ipynb)
  
### Inheritance

- [from abs import ABC](notes/error_handling/error_types/notimplementederror.ipynb)
- [from abs import ABCMeta](notes/designpatterns/decorator/built-in-decorators/abstractmethod.py)
- [Difference between importance ABC or ABCMeta](https://stackoverflow.com/questions/33335005/is-there-any-difference-between-using-abc-vs-abcmeta)
  - TLDR: ABC is a wrapper of ABCMeta, both serves the purpose where former easy to write.

### Passing variables in from command line

- [Unnamed arguments](notes/command_line/sysarg.py)
- Named arguments: `:TODO`
- [Filename as argument](notes/command_line/fileargparse.py)


### Environment Setting

- [Read from config file](notes/configparser/testconfig.ipynb)
   -  How to comment on config file(*.ini): Put `#` sign in front of an empty line
- [Using .env Files for Environment Variables in Python Applications](notes/envsetting/envsetting_intro.ipynb)

```
When to use configparser? When to user .env?
#### TLDR:
Use .env to save string-variable value which should not at any cost being exposed in code versioning platform/docker

### use .env
- the . of filename make it hidden
- already excluded in preset .gitignore
- Nearly every programming language has a package or library that can be used to read environment variables from the .env file instead of from your local environment. 
- load_dotenv will find from host environment for variables when .env file is not file (for docker environment)

### use configparser
- import with more built in variable type (int, string, boolean) and checks to perform upon the value
```

### XML Parser
- [Read from xml file](notes/xmlparser)

### URL

- [Download URL to local file and checksum](notes/url/downloadurl.ipynb)

### Performance

- [Dataframe - column-major, Numpy - row-major](notes/performance/df_numpy_major.ipynb)
- [Memory Profiling](notes/memory_profiling)
- [Execution Time Profiling with line_profiler](notes/time_profiling)
### Multiprocessing
```
Difference of pool(from multiprocessing) from thread:
pool spins up different processes while thread stay in the same process
  
The goal of pool (multiprocessing) is to maximize the use of cpu cores.
```
- [Create workers according to number of cores](notes/multiprocess_ops/readme.md)
  - [Create worker with imap](notes/multiprocess_ops/createworker.py)
  - [Create worker with imap passing multiple parameters](notes/multiprocess_ops/createworker_multipleparam.py)
  - [Create worker with chunks of data](notes/multiprocess_ops/imap_chunk.py)

### Logging

#### Built-In Logging

- Basic:
  ```
  import logging
  logger = logging.getLogger(__name__)
  logging.basicConfig(stream=sys.stdout, level=logging.INFO)
  ```
- Logging Levels: DEBUG, INFO, WARN, ERROR, FATAL
- [Advanced configuration log to stdout](notes/logging/builtinlogging/log2stdout.ipynb)
- [Advanced configuration log to file](notes/logging/builtinlogging/log2file.ipynb)
- Log with variables: `logging.error(f"Keys {a} is missing")`
- [Log exception](notes/error_handling/suppress_error/urlcaller_logger.py)
- [Logging write to both stdout and file](notes/logging/builtinlogging/write_2_multiple_outputs.py)

#### Logging Others

- [Logging with module _icecream_](notes/logging/icecream)

## Design Patterns

- [Factory method](notes/designpatterns/factory_method.ipynb)
- [Abstract Factory](notes/designpatterns/abstractfactory.py)
- [Monkey Patching](notes/designpatterns/monkeypatching.py)
- [Singleton](notes/designpatterns/singleton.py): A singleton is a class with only one instance.
- [Decorator](notes/designpatterns/decorator)

### [Built-in Decorators](notes/designpatterns/decorator/built-in-decorators)

- [Class Method @classmethod](notes/designpatterns/decorator/built-in-decorators/classmethod_imp.ipynb): take `cls` as first parameter (have access to internal fields and methods)
- [Static Method @staticmethod](notes/designpatterns/decorator/built-in-decorators/staticmethod_imp.ipynb): can take no parameters, basically just a function
    - [When to use @classmethod](notes/designpatterns/decorator/built-in-decorators/classmethod_imp.ipynb), @staticmethod
      - Class method can modify the class state,it bound to the class and it contain cls as parameter.  
        `def test(cls, ): self.variable = ?`
      - Static method can not modify the class state,it bound to the class and it does't know class or instance  
        `def test(variable): ...`
- dataclass @dataclass
  - [dataclass hello world](notes/designpatterns/decorator/built-in-decorators/dataclass_helloworld.ipynb)
- [Abstract class with ABCMeta and @abstractmethod](notes/designpatterns/decorator/built-in-decorators/abstractmethod.ipynb)
- [Property Setting](notes/designpatterns/decorator/built-in-decorators/property.ipynb)
- [@property to prevent setting value](notes/designpatterns/decorator/built-in-decorators/property_notsetvalue.ipynb)
  1. Native Verbose Method
  2. Using built-in property function
  3. Using decorator
  - getter: @property
  - setter: @{variable}.setter
  - deleter: @{variable}.deleter
- [@lru_cache](notes/designpatterns/decorator/built-in-decorators/lru_cache.ipynb)
### Testing

- Simple check, raise AssertionError if wrong:
  format: `assert condition, message when error raised
  - `assert a == 20, "val a == 20"`
  - `assert isinstance(a, int)`

#### [Module _typing_: Type hint & annotations](notes/type_checking/typingimp.ipynb)

- List
- Tuple
- Set
  ```
  # Prior to python 3.9
  
  from typing import List, Tuple, Set

  items: List[str]
  values : Tuple[int, str, str]
  products : Set[bytes]
  
  # python 3.9 onwards
  # no need import 

  items: list[str]
  values : tuple[int, str, str]
  products : set[bytes]
  ```
- [Any](notes/type_checking/anyimp.ipynb) : `from typing import Any; varible : Any`
- [Union](notes/type_checking/unionimp.ipynb) / Optional
  - [Simplification of Union from python 3.10 onwards](notes/type_checking/union_evolution.py): `var1 : str | None`
- [Literal](notes/type_checking/literalimp.py)
- [Annotated](notes/type_checking/typing_annotated.ipynb)
  - Before python 3.9: `from typing_extensions import Annotated`
  - Python 3.9 onwards: `from typing import Annotated`
    
#### Pydantic : Data parsing and validation library 

- [BaseModel to correctly declare type](notes/pydanticops/basemodel_helloworld.ipynb)
- [Pydantic Settings](notes/pydantic-settings/test.py)
  - Checking [HTTPUrl](notes/pydanticops/httpurltest.py)

#### [Email Validation](notes/email-validation)

- [Basic checking of domain existence and email constructed correctly](notes/email-validation/helloworld_validate_email.ipynb)

#### Keywords
- [continue](notes/condition/continue_keywords.ipynb)
- [match<>case syntax (Supports after python 3.10)](notes/condition/match_case.ipynb)
  
### Others
- Jinja: Template Engine for Python. TLDR: Use text-based templates to tranformer `Hello, {{ user_name }}!` to `Hello, John!`
- [Kill after x amount of time if process not complete](notes/error_handling/timeout)
- [Context Managers](notes/yield/context_manager.ipynb)

### Webbrowser
- Open url with webbrowser module
  - [In script](notes/webbrowser/open_browser.ipynb)
  - In command: `python -m webbrowser -t "https://www.python.org"`

### [Redis](https://redis.io/docs/connect/clients/python/)
- Declare redis: `r = redis.Redis(host='127.0.0.1', port=6379)`
- Set key: `r.set('counter', 1)`
- Get key: `value : int = r.get('counter')`
- Check if key exist: `r.exists(<key>)`
- [Set expiry and check ttl](https://koalatea.io/python-redis-expire/)

### Networking
  
- Get IP from domain name: `import socket;socket.gethostbyname("www.google.com");`
- Get host name of the machine: `socket.gethostname()`

### Stock

- [Get stock price](notes/stock/get_stock_price.py)

### Concurrency

#### Built-in Concurrency Library: Asyncio

- [Simple example with asyncio](notes/concurrency/asyncio/asyncio_wait.py)

### Hashing 
 
- [Password hashing with library bcrypt - saltround](notes/hashing/bcrypt_password_hashing.ipynb)
- [Password hasing with passlib backed with bcrypt (Used in Fast API)](notes/hashing/passlib_password_hashing.ipynb)

### Web

- [Webhook](notes/web/webhook)
  
## Software Development  

### REST

#### FastAPI

- [Form Data](notes/rest/fastapi/formdataexample)
- [Send image via UploadFile](notes/postgresql-python/notes/image2postgres/server.py)
- [Client upload file to FastAPI Uploadfile and get response](notes/rest/fastapi/clientsendfile.ipynb)
- [Return content from url and write image](notes/postgresql-python/notes/image2postgres/client.py)

#### Requests

- [Get data from url](notes/rest/requests/download_from_url.ipynb)

### Database
  
  
- [Connect to db with sqlalchemy](notes/sqlalchemyops/readme.md)
  - Silence the log: `create_engine(..., echo = False)`
  - [SQLAlchemy query with name and value insertion](notes/sqlalchemyops/param_insertion.ipynb)

#### [PostgreSQL](notes/postgresql-python/readme.md)

- [Postgres connect to AWS RDS](notes/postgresql-python/notes/aws-rds)
- [Local Node](notes/postgresql-python/notes/local)
- ~[Save and load image between REST and Postgres](notes/postgresql-python/notes/restimage2postgres)~ `Obsolete: large files (including image) should be saved to storage`
- ~[Save and load video between REST and Postgres](notes/postgresql-python/notes/restvideo2postgres)~ `Obsolete: large files (including image) should be saved to storage`

### Cloud

#### AWS

- [Postgres connect to AWS RDS](notes/postgresql-python/notes/aws-rds)

#### [S3: Scalable Storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorials.html)

- [List name of buckets](notes/cloud/aws/getbucketlist.ipynb)
- [List objects in a specific bucket](notes/cloud/aws/getobjectinbucketlist.ipynb)
- [Upload file with function upload_file or upload_fileobj](notes/cloud/aws/upload2bucket.ipynb)
  - [Upload video file](notes/cloud/aws/uploadvideo2bucket.ipynb)
  - [Upload video file with progress counter](notes/cloud/aws/uploadvideo2bucketwithprogress.ipynb)
- [Upload multipart](notes/cloud/aws/uploadmultipart.ipynb)
- [Upload multipart with multiple workers](notes/cloud/aws/uploadmultipart_withworkers.py)
- [Get object from S3 with boto](notes/cloud/aws/get_s3_object_with_boto.ipynb)
- [Download s3 public from url with requests](notes/cloud/aws/download_s3_file.ipynb)
- [Create subfolder in bucket and upload file](notes/cloud/aws/create_subfolder_and_upload_file.ipynb)
- [Delete S3 object, objects and/or folder](notes/cloud/aws/boto3_delete_object.ipynb)
**Note:**

- **What is a bucket in S3**
  <details>

  A bucket is a container for objects stored in Amazon S3 which can contains files and folders.
  You can store any number of objects in a bucket and can have up to 100 buckets in your account

  </details>

## Machine Learning
  
### Pytorch

- Check if cuda is available - `import torch; torch.cuda.is_available()`
- [Softmax](notes/pytorch/torch_softmax.ipynb)

#### Torch Tensor

**Torch Tensor Creation**

- Create tensor of **zeros** with shape like another tensor: `torch.zeros_like(another_tensor)`
- Create tensor of **zeros** with shape (tuple): `torch.zeros(shape_in_tuple)`
- Create tensor of **ones** with shape like another tensor: `torch.ones_like(another_tensor)`
- Create tensor of **ones** with shape (tuple): `torch.ones(shape_in_tuple)`
- Create tensor of **random floating value** between 0-1 with shape like another tensor:  
  `torch.rand_like(another_tensor, dtype = torch.float)`
- Create tensor of **random floating value** between 0-1 with shape (tuple):  
  `torch.rand(shape_in_tuple)`

**Torch Tensor Info Extraction**

- Given torch.tensor `buffer = tensor(4)`, get the value by - `id = buffer.item()`
- Given torch.tensor, get the argmax of each row - `torch.argmax(buffer, dim=<(int)dimension_to_reduce>)`
- Tensor to cuda - `inputs = inputs.to("cuda:0")` or `inputs = inputs.cuda()`
- Tensor to cpu - `inputs = inputs.to("cpu")` or `inputs = inputs.cpu()`
- Tensor shape - `tensor.shape`
- Tensor data types - `tensor.dtype`
- Device tensor is stored on - `tensor.device`
- Torch tensor(single value) to value: `tensorarray.item()`
- Retrieve subset of torch tensor by row index: `tensor[<row_number>, :]` / `tensor[<row_number_from>:<row_number_to>, :]`
- Retrieve subset of torch tensor by column index: `tensor[:, <column_number_from>:<column_number_to>]`

**Torch Tensor Conversion**

- List to torch tensor - `torch.tensor(listimp)`
- Numpy array to torch tensor - `torch.from_numpy(np_array)`
- Torch tensor to numpy: `tensorarray.numpy()`
- [Image to torch tensor](notes/pytorch/torchtensor2image.ipynb)
- [Torch tensor to image](notes/pytorch/torchtensor2image.ipynb)

  
**Torch Tensor Operation**

- [Torch tensor value change by indexing and conditions](notes/pytorch/tensorvalue_manipulation.ipynb)
- [Concatenate tensor according to dimension (0 for adding rows, 1 for adding columns)](notes/pytorch/tensorvalue_manipulation_0.ipynb):  
  `torch.cat([<tensor_1>, <tensor_2>, ...], dim = <dimension_number>`

**Dataset Loader, Iterator**

- `torch.utils.data.DataLoader`: stores the samples and their corresponding labels,
- `torch.utils.data.Dataset`: wraps an iterable around the Dataset to enable easy access to the samples

**Torch Tensor In/Out**

- [Save torch tensor to file](notes/pytorch/save_write_torch.ipynb): `torch.save(x : torch.tensor, tensorfile :str)`
- [Load torch tensor from file](notes/pytorch/save_write_torch.ipynb): `torch.load(tensorfile :str)`

#### Torch Dataset

- [Image Datasets](https://pytorch.org/vision/stable/datasets.html)

  - Fashion MNIST [Torch](https://github.com/pytorch/vision/blob/main/torchvision/datasets/mnist.py)
      <details>

    Fashion-MNIST is a dataset of Zalando’s article images consisting of 60,000 training examples and 10,000 test examples.
    Each example comprises a 28×28 grayscale image and an associated label from one of 10 classes.

      </details>

- [Text Datasets](https://pytorch.org/text/stable/datasets.html)
- [Audio Datasets](https://pytorch.org/audio/stable/datasets.html)

### Huggingface

- Send model to cuda - `model.to('cuda:0')` or `model.cuda()`
- [Overview of DatasetDict](notes/huggingface/datasetdict_intro.ipynb)
- [DatasetDict from Pandas Dataframe](https://stackoverflow.com/questions/71618974/convert-pandas-dataframe-to-datasetdict)

### Computer Vision

#### Computer Vision - Basic

- Get image shape: `img.shape` (**Important:** shape[0] = height, shape[1] = width)
- Create a color image: `image = np.zeros((h,w,3), np.uint8)`
- Read/Write image:
  - [As byte](notes/cv/image_as_byte.ipynb)
  - [As Bytearray](notes/cv/image_as_bytearray.ipynb)
  - [As base64](notes/cv/image_as_base64.ipynb)
  - [From imageio (save with numpy array)](notes/cv/imageio_writeimage.ipynb)
    - Read only 3 channels: `im3d = imageio.imread('path/to/some/singlechannelimage.png', pilmode='RGB')`
- Read image 
  - [Read image from url](notes/cv/read_image_from_url.ipynb)
  - Read in image with Pillow
    - Pillow read in image from np.array: ```im = Image.fromarray(nprrayimage)```
  - [Read in image from imageio](notes/cv/imageio_readinimage.ipynb)
- Pause to display image or wait for an input: `cv2.waitKey(0)`
- Save an image: `cv2.imwrite(pathtoimg : str, img : numpy.ndarray)`
- Show an image in window: `cv2.imshow(windowname : str, frame : np.array)`
- Show an image in Jupyter notebok
  ```
  from IPython.display import Image
  Image(filename=pathtoimg : str)
  ```
- Crop image
    - numpy array: `image[y0:y1, x0: x1, :]`
- Flip image: `frame = cv2.flip(frame, flipcode : int)`
  - Positive flip code for flip on y axis (left right flip)
  - 0 for flip on x axis (up down)
  - Negative for flipping around both axes

#### Computer Vision - Intermediate

**Computer Vision - Filter**

- [Blur](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37) with averaging mask: `cv2.blur(img,(5,5))`
- GaussianBlur: `blur = cv2.GaussianBlur(img,(5,5),0)`
  - Note: Kernel size `(5, 5)` to be positive and odd. Read more [here](https://plantcv.readthedocs.io/en/v2.0/gaussian_blur/) on how kernel size influence the degree of blurring.
- [Blurring region of image](notes/cv/blur_region.ipynb)

**Computer Vision - Video Stream**
- [Play video in jupyter notebook/lab](notes/media/play_video.ipynb)
- Get total number of frames in the video: `int(cap.get(cv2.CAP_PROP_FRAME_COUNT))`
- [change video frame curent count to desired frame count](notes/cv/video_forward_to_frame_count.py)
- Concat multiple video streams to show side by side: [2 video streams](notes/cv/concat2windows.py) [3 video streams](notes/cv/concat3windows.py)
- Save stream to video output
  - [opencv method](notes/cv/opencv_save2video.py) (Face problem when replaying the video generated on AWS cloud services)
  - [imageio method](notes/cv/imageio_readin_write_video.ipynb)
- [Read in video stream from a file](notes/cv/readvideostream.py)
  - [Rread in video stream with imageio](notes/cv/imageio_readin_write_video.ipynb)
- [Read in stream from camera](notes/cv/save2video.py)
- [video arrays (in opencv) -> bytes -> np.array -> video arrays (in opencv)](notes/cv/video2bytes2nparray.py)
- [Merge audio with video](notes/cv/savevideowithaudio)
- [Check if video comes with audio](notes/cv/check_video_with_audio.ipynb)
- [Split audio from video](notes/cv/splitaudiofromvideo.py)

**Computer Vision - Other**

- [Overlay image](notes/cv/replaceroi.py)
- Resizing frame: `outframe = cv2.resize(frame, (w, h))`
- [Set color to rectangle region](notes/cv/setrectangle.ipynb)
- [RGB value to color text](notes/cv/rgb_to_color.ipynb)
- Color to gray image: `gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
- Draw circle: `image = cv2.circle(image, center_coordinates: set, example: (50, 100), radius: int, color : set, example: (255, 255, 255), thickness : int)`
- bgr to rgb channel: `img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)`
- [Draw rectangle and point on image with mouse activity](notes/cv/mouseprompt.py)
  - [Mouse Events](https://www.tutorialspoint.com/opencv_python/opencv_python_handling_mouse_events.htm)
- [Draw rectangle on image in jupyter](notes/cv/draw_rectangle_on_image(jupyter).ipynb)
- [Write text on image](notes/cv/writetext.py)
- [Remove background](notes/cv/remove_bg.ipynb)
- [Weighted blend two image with `cv2.addWeighted`](notes/notes/cv/weighted_blend_image.py)
- [Add channel to image](https://stackoverflow.com/questions/32290096/python-opencv-add-alpha-channel-to-rgb-image)
- [Draw contour](notes/cv/helloworld_contour.ipynb)

### [Audio](notes/audio)

- [Audio of .wav -> .flac](notes/audio/wav2flac.ipynb)
- [Get sampling rate of an audio file](notes/audio/getsamplingrate.ipynb)
- [Audio file <> Numpy Array](notes/audio/audiofile2array.ipynb)
- [Play audio file in Jupyter](notes/audio/load_audio_and_show_waveform.ipynb)

#### [Librosa](I/O operations for audio files, including resampling)

- [Read an audio file](notes/audio/load_audio_and_show_waveform.ipynb): `array, sampling_rate = librosa.load(audiopath)`
- [Get duration of audio](notes/audio/get_audio_duration.ipynb): `librosa.get_duration(path=x)`
- [Show waveform](notes/audio/load_audio_and_show_waveform.ipynb)
- [Show spectrogram, log mel spectrogram](notes/audio/load_audio_and_show_spectrogram.ipynb)

#### Huggingface Datasets
- [Upsample Datasets](notes/audio/upsample_with_hf_datasets.ipynb)
  
## Good To Read
- [Visual Studio Code Extension for Python](https://lightrun.com/vscode-python-extensions/)
  
## Medium Posts

- [Ctrl + c, Ctrl + v — Replicating Data Science Conda Environment](https://codenamewei.medium.com/ctrl-c-ctrl-v-replicating-data-science-conda-environment-c190ad0d93fd)
  - [Conda Commands Cheatsheet](conda-guidelines.md)
- [Displaying visuals with Markdown](https://medium.com/geekculture/displaying-visuals-with-markdown-c39f2495e146)
  - [Examples of displaying image in readme.md](notes/markdown/readme.md)
  - [Examples of displaying image in Jupyter](notes/markdown/markdown_guidelines.ipynb)
