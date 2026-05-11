# Homebrew formula for Entroly.
#
# Deployment: copy this file to Formula/entroly.rb in a separate repo named
# `juyterman1000/homebrew-entroly`. Users then install with:
#
#   brew tap juyterman1000/entroly
#   brew install entroly
#
# Bumping versions:
#   1. Bump `version` to match the PyPI release.
#   2. Update `url` to the matching sdist on PyPI.
#   3. Update `sha256` to the new tarball's sha256.
#      Get it via: shasum -a 256 entroly-<version>.tar.gz
#      Or:        brew fetch --build-from-source entroly
#
# CI tip: a tiny GitHub Action in the tap repo can run `brew test entroly`
# on every push so a broken formula is caught before users hit it.

class Entroly < Formula
  include Language::Python::Virtualenv

  desc "Token-saving proxy and context compression engine for AI coding agents"
  homepage "https://entroly.dev"
  url "https://files.pythonhosted.org/packages/source/e/entroly/entroly-0.15.1.tar.gz"
  sha256 "c3d0df61fe106b6654410d3474761ef449ceef2b4e28d0d19df618dad5e5d884"
  license "Apache-2.0"
  head "https://github.com/juyterman1000/entroly.git", branch: "main"

  depends_on "python@3.12"
  depends_on "rust" => :build

  def install
    venv = virtualenv_create(libexec, "python3.12")
    venv.pip_install_and_link buildpath, link_manpages: false
  end

  test do
    # Version should match the formula's version after install.
    assert_match version.to_s, shell_output("#{bin}/entroly --version")

    # Sub-commands wired up.
    assert_match "proxy", shell_output("#{bin}/entroly --help")
    assert_match "wrap",  shell_output("#{bin}/entroly --help")

    # Doctor self-check should exit 0 on a healthy install.
    system bin/"entroly", "doctor"
  end
end
