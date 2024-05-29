<a id="matmul-multi-core-example"></a>

# Matmul (Multi Core Optimized)

The Tensix core architecture’s secret weapon is its full user control over memory workload spread, core communication style, novel block matmul kernels, and compute patterns. In this section, we will harness real power through 3 shiny optimizations, each building off one another: data reuse, data multicast, and multidimensional systolic arrays (coming soon).

```default
export ARCH_NAME=<arch name>
export TT_METAL_HOME=<this repo dir>
make build
make programming_examples/matmul_multi_core
./build/programming_examples/matmul_multi_core_reuse
./build/programming_examples/matmul_multi_core_reuse_mcast
```

* [Data Reuse in matmul_multicore_reuse](matmul_multi_core_optimizations/data_reuse.md)
  * [Fine-Grained Block Size Control](matmul_multi_core_optimizations/data_reuse.md#fine-grained-block-size-control)
  * [Intermediate Circular Buffer Configuration](matmul_multi_core_optimizations/data_reuse.md#intermediate-circular-buffer-configuration)
  * [Stride Kernel Arguments](matmul_multi_core_optimizations/data_reuse.md#stride-kernel-arguments)
  * [Intermediate Results Handling](matmul_multi_core_optimizations/data_reuse.md#intermediate-results-handling)
  * [Conclusion](matmul_multi_core_optimizations/data_reuse.md#conclusion)
* [Data Multicasting in matmul_multicore_reuse_mcast](matmul_multi_core_optimizations/data_mcast.md)
  * [Additional Compile-Time Argument](matmul_multi_core_optimizations/data_mcast.md#additional-compile-time-argument)
  * [Configuring Core Ranges for Tile Distribution](matmul_multi_core_optimizations/data_mcast.md#configuring-core-ranges-for-tile-distribution)
  * [Circular Buffer Creation for CoreGrid](matmul_multi_core_optimizations/data_mcast.md#circular-buffer-creation-for-coregrid)
  * [Multicast Reader/Writer Kernel Setup](matmul_multi_core_optimizations/data_mcast.md#multicast-reader-writer-kernel-setup)
  * [New Compute Kernel: Fused Bias Addition and Activation Functions](matmul_multi_core_optimizations/data_mcast.md#new-compute-kernel-fused-bias-addition-and-activation-functions)
  * [Semaphores](matmul_multi_core_optimizations/data_mcast.md#semaphores)
  * [Kernel Runtime Arguments](matmul_multi_core_optimizations/data_mcast.md#kernel-runtime-arguments)
