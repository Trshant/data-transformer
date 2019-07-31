# Need for this tool

We all do data transformation, but the solution is unelegant and thoroughly not literate. By using pure functions in a functional programming paradigm, we speed up data transformations without compromising on elegance.  

Do read through the uses and let me know via the issues or email me ( trshant at gmail dot com ) if something can be made better. You can email me if i did it right - i'd love to hear that!  

# Documentation.

only one function needs to be called post importing: `process`.  
```python
process(data, process_line_definition)
```  
data is an imput object.
the process_line_definition is what we use to define what we need done. The format for it is:  

```
[ data_path , directive , function_called_on_data_object_after_going_on_data_path , further_process_line_directive ]
```  
