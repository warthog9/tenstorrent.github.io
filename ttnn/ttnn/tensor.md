# Tensor

A `ttnn.Tensor` is a multi-dimensional matrix containing elements of a single data type.

## Shape

`ttnn.Tensor` uses `ttnn.Shape` to store its shape.

`ttnn.Shape` can be used to store dimensions for a tensor of rank 1 to rank 8 (inclusive).

`ttnn.Shape` stores the shape of both the actual data and the data padded to tile dimensions. Which can be different due to hardware requirements.

`ttnn.Shape([16, 32])` is a shape of 2D tensor with 16 rows and 32 columns. Where the number of actual rows and columns is 16 and 32 respectively.
And the padded dimensions match the actual dimensions. The tensor of this shape has 16 \* 32 elements in the storage.

![Tensor](ttnn/images/tensor.png)

Printing the shape would show the actual shape:

```python
>>> print(ttnn.Shape([16, 32]))
ttnn.Shape([16, 32])
```

`ttnn.Shape([14, 28], [32, 32])` is a shape of 2D tensor with 14 rows and 28 columns.
Where the number of actual rows and columns is 14 and 28 respectively and the number of padded rows and columns is 32 and 32 respectively.
The tensor of this shape has 32 \* 32 elements in the storage.

![Tensor With Padded Shape](ttnn/images/tensor_with_tile_padding.png)

Printing the shape would show the actual shape with the padded shape next to it in the square brackets:

```python
>>> print(ttnn.Shape([14, 28], [32, 32]))
ttnn.Shape([14[32], 28[32]])
```

Shape with tile padding can be obtained by calling with_tile_padding() method of `ttnn.Shape`

```python
>>> print(ttnn.Shape([14, 28], [32, 32]).with_tile_padding())
ttnn.Shape([32, 32])
```

<a id="ttnn-layout"></a>

## Layout

<a id="ttnn-row-major-layout"></a>

**ttnn.ROW_MAJOR_LAYOUT**

Row major layout has the consecutive elements of a row next to each other.

![Tensor With Row-Major Layout](ttnn/images/tensor_with_row_major_layout.png)

<a id="ttnn-tile-layout"></a>

**ttnn.TILE_LAYOUT**

In tile layout, the elements themselves are placed within a 32x32 square called a tile.
The tiles themselves are then still stored in a row-major order. In order to transition to TILE_LAYOUT, [ttnn.to_layout](ttnn/to_layout.md#ttnn-to-layout) can be used.
When the height or width of the tensor are not divisible by 32, padding is automatically provided.

![Tensor With Tile Layout](ttnn/images/tensor_with_tile_layout.png)

<a id="ttnn-datatype"></a>

## Data Type

ttnn supports the following data types:

- **uint16**
- **uint32**
- **float32**
- **bfloat16**
- **bfloat8_b**

#### NOTE
`ttnn.Tensor` uses a minimum of 4 bytes to store a row of the tensor in [ttnn.ROW_MAJOR_LAYOUT](#ttnn-row-major-layout) on the device.
That means that the width of a tensor on the device must be a multiple of 4 / sizeof(dtype). The exact numbers are shown below:

#### Required Width Multiples for Data Types

| Data Type      | Required Width Multiple                                       |
|----------------|---------------------------------------------------------------|
| ttnn.uint16    | 2                                                             |
| ttnn.uint32    | 1                                                             |
| ttnn.float32   | 1                                                             |
| ttnn.bfloat16  | 2                                                             |
| ttnn.bfloat8_b | 32 (Special case because the tensor has to be in tile layout) |

<a id="ttnn-storage"></a>

## Storage

**OWNED_HOST_STORAGE**

> The buffer of the tensor is on the host and its allocation/deallocation is owned by ttnn.

**BORROWED_HOST_STORAGE**

> The buffer of the tensor is on the host and it was borrowed from `torch` / `numpy` / an external buffer.

**DEVICE_STORAGE**

> The buffer of the tensor is on a ttnn device. And its allocation/deallocation is owned by ttnn.

## Tensor Sharding

Sharding refers to a tensor that is split across a distributed memory space, with that distribution ideally being abstracted away.
Currently we support L1 sharding, which refers to the distribution of a tensor across the L1 memory space of different cores.

Sharded tensors are represented in two dimensions, we compress a higher rank tensor into two-dims by compressing all upper dims in dim 0 and keeping the last dimension the same.
For example a [1,2,3,4] tensor will be represented as a [6,4] 2D tensor before sharding.
Data in a `ttnn.Tensor` is organized in tiles, and these tiles are typically in row-major order.
The size of the tile depends on the `ttnn.Layout` and `ttnn.Shape` of the tensor.
Refer to the section about [Layout](#ttnn-layout) to learn more.

**Data Organization on Host**

A sharded tensor’s tiles are organized in sharded order on the device which we will highlight with an example.
A tensor is only sharded on device and on the host the tiles remain in row-major order.
Below is an example of a tensor on the host, with each tile labelled.

![A tensor on the host before it is sharded](ttnn/images/host_tensor.png)

There are a few key attributes that needs to be defined with respect to sharding (specifically in L1):

- **Core Grid**: Represents the cores who’s L1 will have a shard of a tensor. Each core will have a single shard.
- **Shard Shape**: The shape in elements of a single shard, this is the subset of the tensor that will be on each core.
- **Sharding Strategy**: Represents how the tensor will be split. Height sharded represents splitting a tensor in rows. Width sharding represents splitting a tensor in columns. Block sharding represents splitting a tensor along a 2D grid.
- **Shard Orientation**: Represents the order of the cores in the 2D shard grid that we read and write our shards to. This can be either row-major or column-major.

**Data Organization on Device**

Now that we know the key attributes and understand how an unsharded 2D tensor looks like.
Lets shard this tensor.
Using the [ttnn.to_memory_config](ttnn/to_memory_config.md#ttnn-to-memory-config) we can take an unsharded host tensor and write it to a sharded device tensor.
In the example below we have a 2x2 core grid, a shard shape of [64,64] ([2,2] in tiles), a sharding strategy of block sharding, and a sharded orientation of row-major.

![A tensor that is block sharded](ttnn/images/sharded_tensor.png)

<a id="ttnn-memoryconfig"></a>

## Memory Config

**ttnn.DRAM_MEMORY_CONFIG**

> The buffer of the tensor is interleaved and is stored in DRAM.

**ttnn.L1_MEMORY_CONFIG**

> The buffer of the tensor is interleaved and is stored in the the local cache of a core

**ttnn.create_sharded_memory_config**

> The buffer of the tensor is sharded (physically distributed). Currently the tensor can only be physically distributed across different cores’ L1.
> Use [ttnn.create_sharded_memory_config](ttnn/create_sharded_memory_config.md#ttnn-create-sharded-memory-config) to create a sharded memory config.

## APIs
