# get_arg_val

### template<typename T> T get_arg_val(int arg_idx)

Returns the value at a given runtime argument index for unique (per-core) runtime arguments set via SetRuntimeArgs() API.

Return value: The value associated with the unique runtime argument index

| Argument              | Description                        | Type                  | Valid Range      | Required       |
|-----------------------|------------------------------------|-----------------------|------------------|----------------|
| arg_idx               | Unique Runtime argument index      | uint32_t              | 0 to 255         | True           |
| T (template argument) | Data type of the returned argument | Any 4-byte sized type | N/A              | True           |
