{
  "targets": [
    {
      "target_name": "rgb_node",
      "sources": [ "swig_wrap.cxx" ],
      "libraries": [ '<(module_root_dir)/../../target/debug/libffi.so'],
      'include_dirs': [
          '../',
       ],
      "cflags!": ["-std=c++11"],
    }
  ]
}
