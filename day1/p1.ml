open List

let read_lines (fname : string) : string list =
  let ic = open_in fname in
  let rec loop acc =
    match input_line ic with
    | line -> loop (line :: acc)
    | exception End_of_file -> close_in ic; List.rev acc
  in
  loop []

let input = read_lines "input.txt"
let (tailSums, lastSum) = fold_left (fun (ls, head) -> fun x -> 
    match (int_of_string x) with
      | x -> (ls, head + x)
      | exception Failure _ -> (head :: ls, 0)
  ) ([], 0) input

let sums = lastSum :: tailSums
let max = List.fold_left max 0 sums
let () = print_int max