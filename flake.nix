{
  description = "Rotisserie Chicken";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        rotisserie-chicken = pkgs.callPackage ./nix/buildPackage.nix {};
      in
      {
        packages = {
          default = rotisserie-chicken;
          rotisserie-chicken = rotisserie-chicken;
        };

        devShells.default = pkgs.callPackage ./nix/devShell.nix {};
      });
}
