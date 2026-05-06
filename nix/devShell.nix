{ mkShell, python3 }:

mkShell {
  name = "rotisserie-chicken-dev";

  buildInputs = [
    python3
  ];
}
