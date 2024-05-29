# get_common_arg_val

### template<typename T> T get_common_arg_val(int arg_idx)

Returns the value at a given runtime argument index for common (all cores) runtime arguments set via SetCommonRuntimeArgs() API.

Return value: The value associated with the common runtime argument index

| Argument              | Description                        | Type                  | Valid Range      | Required       |
|-----------------------|------------------------------------|-----------------------|------------------|----------------|
| arg_idx               | Common Runtime argument index      | uint32_t              | 0 to 255         | True           |
| T (template argument) | Data type of the returned argument | Any 4-byte sized type | N/A              | True           |
