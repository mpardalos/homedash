{
  description = "Homedash";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { nixpkgs, ... }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      pythonDeps = p: [
        p.jinja2
        p.starlette
        p.sse-starlette
        p.uvicorn
      ];
    in
    {
      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          default = pkgs.python3Packages.buildPythonApplication {
            pname = "homedash";
            version = "0.1.0";
            pyproject = true;
            src = pkgs.lib.fileset.toSource {
              root = ./.;
              fileset = pkgs.lib.fileset.unions [
                ./pyproject.toml
                ./src
              ];
            };
            build-system = [ pkgs.python3Packages.setuptools ];
            dependencies = pythonDeps pkgs.python3Packages;
            meta.mainProgram = "homedash";
          };
        }
      );

      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python3.withPackages pythonDeps;
          dev = pkgs.writeShellScriptBin "dev" ''
            exec ${python}/bin/python -m uvicorn homedash.app:app --app-dir src --reload "$@"
          '';
        in
        {
          default = pkgs.mkShell {
            packages = [
              python
              dev
            ];
          };
        }
      );
    };
}
