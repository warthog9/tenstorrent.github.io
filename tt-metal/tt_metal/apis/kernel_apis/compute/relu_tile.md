# relu_tile

```cpp
void ckernel::relu_tile_init()
```

Please refer to documentation for any_init. 

```cpp
void ckernel::relu_tile(uint32_t idst)
```

Performs element-wise computation of relu (0 if negative else 1) on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |

# relu_max_tile

```cpp
void ckernel::relu_max_tile_init()
```

Please refer to documentation for any_init. 

```cpp
void ckernel::relu_max_tile(uint32_t idst, uint32_t param0)
```

Performs element-wise computation of relu max (relu(max(x, upper_limit))) on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
| upper_limit   | Upper limit of relu_min                                                    | uint32_t  | Greater than 0                                        | True           |

# relu_min_tile

```cpp
void ckernel::relu_min_tile_init()
```

Please refer to documentation for any_init. 

```cpp
void ckernel::relu_min_tile(uint32_t idst, uint32_t param0)
```

Performs element-wise computation of relu min (relu(min(x, lower_limit))) on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
| lower_limit   | Upper limit of relu_min                                                    | uint32_t  | Greater than 0                                        | True           |

# leaky_relu_tile

```cpp
void ckernel::leaky_relu_tile_init()
```

Please refer to documentation for any_init. 

```cpp
void ckernel::leaky_relu_tile(uint32_t idst, uint32_t param0)
```

Performs element-wise computation of leaky relu (relu(x) + slope\*-relu(-x)) on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
| slope         | slope used in leaky relu calculation                                       | uint32_t  | Greater than 0                                        | True           |
