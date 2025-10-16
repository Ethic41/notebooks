# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-07-31 16:20:23
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


let
  nixpkgs = import <nixpkgs> { };
  pkgs = import <nixpkgs> { config = { allowUnfree = true; }; overlays = []; };
in

pkgs.mkShellNoCC {
  name = "recon-shell";

  packages = with pkgs; [
    cowsay
    nmap
    subfinder
    amass
    httpx
    waybackurls
    gau
    ffuf
    feroxbuster
    docker
    docker-compose
  ];

  GREETINGS = "Greetings from Vice City!!! ~ Tommy Vercetti";
}
