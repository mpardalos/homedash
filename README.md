# Homedash

A minimal Starlette app with a Nix development shell and deployment package.
The flake supports Linux and macOS on x86_64 and aarch64. The application is
packaged with `buildPythonApplication` using `pyproject.toml`.

## Develop

```sh
nix develop
dev
```

Run `dev` from the project root. Open <http://127.0.0.1:8000>.
`/health` returns `{"status":"ok"}`. The server reloads on changes;
pass Uvicorn options with e.g. `dev --port 8080`.

## Deploy

```sh
nix build
./result/bin/homedash --host 0.0.0.0 --port 8000
```

The package includes the app, Python, and dependencies, and runs without the
source checkout. Run this command under your deployment host's service manager.
You can also start it with `nix run . -- --port 8000`.

`flake.lock` pins dependencies. Update them with `nix flake update`.
When using Git, add the project files before running Nix commands.
