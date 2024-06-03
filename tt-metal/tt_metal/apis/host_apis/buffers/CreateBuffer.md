# CreateBuffer

---
```cpp
std::shared_ptr<Buffer> tt::tt_metal::CreateBuffer(const InterleavedBufferConfig &config)std::shared_ptr<Buffer> tt::tt_metal::CreateBuffer(const InterleavedBufferConfig &config)
```

Allocates an interleaved DRAM or L1 buffer on device

Return value: std::shared_ptr<Buffer>

| Argument      | Description       | Type                    | Valid Range      | Required       |
|---------------|-------------------|-------------------------|------------------|----------------|
| config        | config for buffer | InterleavedBufferConfig |                  | Yes            |

---
```cpp
std::shared_ptr<Buffer> tt::tt_metal::CreateBuffer(const ShardedBufferConfig &config)std::shared_ptr<Buffer> tt::tt_metal::CreateBuffer(const ShardedBufferConfig &config)
```

Allocates a sharded DRAM or L1 buffer on device

Return value: std::shared_ptr<Buffer>

| Argument      | Description       | Type                | Valid Range      | Required       |
|---------------|-------------------|---------------------|------------------|----------------|
| config        | config for buffer | ShardedBufferConfig |                  | Yes            |
