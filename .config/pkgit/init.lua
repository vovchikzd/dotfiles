local home = os.getenv("HOME")
prefix = home.."/.local"
install_directories = {
  bin = prefix.."/bin"
  , include = prefix.."/include"
  , lib = prefix.."/lib"
  , src = prefix.."/share/pkgit"
}

build_systems = require("builds.init")
repositories = require("repos.init")
