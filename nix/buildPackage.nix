{ lib, python3, stdenv }:

python3.pkgs.buildPythonApplication rec {
  pname = "rotisserie-chicken";
  version = "0.1.0";
  format = "other";

  src = ../src;

  propagatedBuildInputs = with python3.pkgs; [
  ];

  dontBuild = true;

  installPhase = ''
    runHook preInstall

    mkdir -p $out/lib/rotisserie-chicken
    mkdir -p $out/bin

    cp -r $src/* $out/lib/rotisserie-chicken/

    cat > $out/bin/rotisserie-chicken << 'EOF'
    #!${python3.interpreter}
    import sys
    import os

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../lib/rotisserie-chicken"))

    from main import main
    import curses

    curses.wrapper(main)
    EOF

    chmod +x $out/bin/rotisserie-chicken

    ln -s $out/bin/rotisserie-chicken $out/bin/rchicken

    runHook postInstall
  '';

  meta = with lib; {
    description = "A terminal-based rotisserie chicken cooking mini-game";
    license = licenses.wtfpl;
    platforms = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
    mainProgram = "rotisserie-chicken";
  };
}
