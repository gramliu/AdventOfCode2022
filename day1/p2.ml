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
let (a :: b :: c :: tail) = List.rev (List.sort compare sums)
let topThree = a :: b :: c :: []
let sumThree = List.fold_left (+) 0 topThree
let _ = print_int sumThree