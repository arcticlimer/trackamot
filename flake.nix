{
  inputs.flake-utils.url = "github:numtide/flake-utils";
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (
      system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          pythonPackages = python-packages: with python-packages; [
            npyscreen
          ];
        in
          rec {
            devShell = pkgs.mkShell {
              packages = with pkgs; [ (python3.withPackages pythonPackages) ];
            };
          }
    );
}
