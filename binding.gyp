{
  "targets": [
    {
      "target_name": "FileWatcher",
      "sources": [
        "src/FileWatcher.cpp",
        "src/FileWatcherLinux.cpp",
        "src/FileWatcherOSX.cpp",
        "src/FileWatcherWin32.cpp",
        "src/NodeSentinelFileWatcher.cpp",
        "includes/FileWatcher.h",
        "includes/FileWatcherImpl.h",
        "includes/FileWatcherLinux.h",
        "includes/FileWatcherOSX.h",
        "includes/FileWatcherWin32.h",
        "includes/NodeSentinelFileWatcher.h"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "includes"
      ]
    }
  ]
}
