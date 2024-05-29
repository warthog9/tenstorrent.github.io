# get_arg_addr

### static uint32_t get_arg_addr(int arg_idx)

Returns the address in L1 for a given runtime argument index for unique (per core) runtime arguments set via SetRuntimeArgs() API.

Return value: Associated L1 address of given unique runtime argument index

| Argument      | Description                   | Type      | Valid Range      | Required       |
|---------------|-------------------------------|-----------|------------------|----------------|
| arg_idx       | Unique Runtime argument index | uint32_t  | 0 to 255         | True           |
