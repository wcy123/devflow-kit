```
brew install --cask macfuse
brew list --cask macfuse

```

download it and install both https://osxfuse.github.io

1. https://github.com/osxfuse/osxfuse/releases/download/macfuse-4.4.3/macfuse-4.4.3.dmg
2. https://github.com/osxfuse/sshfs/releases/download/osxfuse-sshfs-2.5.0/sshfs-2.5.0.pkg

```
sshfs -p 10022 localhost:/workspace $HOME/workspace
ls -l ~/workspace
```
