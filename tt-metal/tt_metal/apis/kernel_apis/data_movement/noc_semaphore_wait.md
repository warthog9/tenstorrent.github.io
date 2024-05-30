# noc_semaphore_wait

```cpp
void noc_semaphore_wait(volatile uint32_t *sem_addr, uint32_t val)
```

A blocking call that waits until the value of a local L1 memory address on the Tensix core executing this function becomes equal to a target value. This L1 memory address is used as a semaphore of size 4 Bytes, as a synchronization mechanism. Also, see *noc_semaphore_set*.

Return value: None

| Argument      | Description                          | Type      | Valid Range        | Required       |
|---------------|--------------------------------------|-----------|--------------------|----------------|
| sem_addr      | Semaphore address in local L1 memory | uint32_t  | 0..1MB             | True           |
| val           | The target value of the semaphore    | uint32_t  | Any uint32_t value | True           |
