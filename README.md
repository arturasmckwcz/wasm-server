# wasm-server

For dev of WebAssembly functions in Rust, C++, etc.

The first run the fileserver on an arbitrary port (8090 by default):

```
$ PORT_FS=8090 python server.py
```

then you may fetch a `.wasm` in browsers `.js` script like:

```
fetch("localhost:8090/someRustFunction.wasm").then
  // code for loading .wasm
```

## Rust

Works.

1. write a function in a `.rs` file
2. make sure the file is located in `rust/` folder and you have `cd`ed to it
3. use `makewasm` shell script like:

```
$ makewasm someRustFunction.rs
```

4. `.wasm` file is stored and ready to be fetched

## C++

Doesn't work. `makewasm` script still is missing.
