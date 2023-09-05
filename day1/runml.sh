#!/bin/bash

# Run an OCaml .ml file

target=$(echo "$1" | cut -f 1 -d ".")
ocamlopt -o "$target" "$1" || exit
./"$target"

rm "$target" "$target.cmi" "$target.cmx" "$target.o"
