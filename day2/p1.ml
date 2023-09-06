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
let scoreMap = Hashtbl.create 100
let _ = 
  Hashtbl.add scoreMap ("A", "X") (1+3);
  Hashtbl.add scoreMap ("A", "Y") (2+6);
  Hashtbl.add scoreMap ("A", "Z") (3+0);

  Hashtbl.add scoreMap ("B", "X") (1+0);
  Hashtbl.add scoreMap ("B", "Y") (2+3);
  Hashtbl.add scoreMap ("B", "Z") (3+6);

  Hashtbl.add scoreMap ("C", "X") (1+6);
  Hashtbl.add scoreMap ("C", "Y") (2+0);
  Hashtbl.add scoreMap ("C", "Z") (3+3);;

let scores = List.map (fun line ->
  let line = String.split_on_char ' ' line in
    let move = List.nth line 0 in
    let player = List.nth line 1 in
    let score = Hashtbl.find scoreMap (move, player) in
    score
) input

let totalScore = List.fold_left (+) 0 scores
let _ = print_int totalScore

