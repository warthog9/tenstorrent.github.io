# reg_api

---
```cpp
void ckernel::tile_regs_acquire()void ckernel::tile_regs_acquire()
```

Acquire an exclusive lock on the DST register for the MATH thread. This register is an array of 16 tiles of 32x32 elements each. This is a blocking function, i.e. this function will wait until the lock is acquired. 

---
```cpp
void ckernel::tile_regs_wait()void ckernel::tile_regs_wait()
```

Acquire an exclusive lock on the DST register for the PACK thread. It waits for the MATH thread to commit the DST register. This is a blocking function, i.e. this function will wait until the lock is acquired. 

---
```cpp
void ckernel::tile_regs_commit()void ckernel::tile_regs_commit()
```

Release lock on DST register by MATH thread. The lock had to be previously acquired with tile_regs_acquire. 

---
```cpp
void ckernel::tile_regs_release()void ckernel::tile_regs_release()
```

Release lock on DST register by PACK thread. The lock had to be previously acquired with tile_regs_wait.
