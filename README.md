# whoDare - AI vs Human Code Contribution Tracker

A VS Code extension that automatically tracks and visualizes AI-generated vs human-written code contributions in real-time.

![whoDare Demo](whoDare.gif)

## 🚀 Features

- **Real-time Tracking**: Automatically monitors all text changes across your workspace
- **AI Detection**: Intelligently identifies AI-generated code using:
  - VS Code inline completion API (Copilot, etc.)
  - Heuristic analysis of large insertions and multi-line changes
  - Pattern recognition for formatted code blocks and paste operations
- **Plain JSON Storage**: All statistics saved in readable `.whodare/stats.json` format
- **Per-file Breakdown**: Track contributions on a file-by-file basis
- **Historical Tracking**: Complete history of every code change event with timestamps
- **Daily Statistics**: Track your coding activity day by day
- **Visual Stats Dashboard**: Beautiful in-editor statistics panel with charts and tables
- **Status Bar Integration**: Quick view of your Human vs AI percentage right in the status bar

## 📦 Installation

### For Cursor Users (Easiest Method)

If you're using **Cursor IDE**, you can install the extension directly from the Extensions tab:

1. Open Cursor IDE
2. Click on the Extensions icon in the sidebar (or press `Ctrl+Shift+X`)
3. Search for **"whoDare"** in the search bar
4. Click **Install**
5. The extension will activate automatically!

### Download and Install from Website

You can download the extension directly from our website:

1. **Download the Extension**:

   - Visit [https://whodare.joshsparks.dev/](https://whodare.joshsparks.dev/)
   - Download the `.vsix` file from the website

2. **Install in VS Code/Cursor**:

   - Open VS Code or Cursor
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
   - Type `Extensions: Install from VSIX...` and select it
   - Navigate to the downloaded `.vsix` file and select it
   - The extension will install automatically

3. **Verify Installation**:
   - After installation, you may need to reload your editor
   - You should see the `whoDare` status bar item in the bottom-left corner
   - The extension is now ready to use!

### Alternative: Command Line Installation

You can also install the `.vsix` file using the command line:

```bash
code --install-extension path/to/whodare-1.0.4.vsix
```

Replace `path/to/whodare-1.0.4.vsix` with the actual path to your downloaded file.

## How It Works

### Automatic Activation

1. Open any workspace in VS Code
2. The extension activates automatically when you start coding
3. All code changes are tracked in real-time - no configuration needed!

### Tracking Process

The extension monitors:

- **Text insertions**: New code you write or AI suggests
- **Text deletions**: Code you remove
- **Text modifications**: Code you edit or replace

Each change is automatically classified as:

- **Human-written**: Small, incremental changes you type manually
- **AI-generated**: Large insertions, multi-line completions, or accepted inline suggestions

### Viewing Your Statistics

#### In VS Code

- **Status Bar**: Click the `whoDare` status bar item (bottom-left) to see your Human vs AI percentage
- **Command Palette**: Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and run `whoDare: Show Code Statistics`
- **Statistics Panel**: View detailed breakdowns including:
  - Total lines and characters (Human vs AI)
  - Per-file contribution breakdown
  - Historical event timeline
  - Visual pie charts

#### On the Web

1. **Commit your stats**: Push the `.whodare/stats.json` file to your GitHub repository
2. **Visit the web viewer**: Go to [https://whodare.joshsparks.dev/](https://whodare.joshsparks.dev/)
3. **Enter your repo URL**: Paste your GitHub repository URL (e.g., `https://github.com/username/repo`)
4. **View visualizations**: See beautiful charts, timelines, and daily breakdowns!

The web viewer automatically fetches your `stats.json` file from GitHub and displays rich visualizations including:

- Interactive pie charts
- Daily activity timelines
- Detailed file-by-file tables
- Dark/light mode support

## Data Storage

All statistics are saved in `.whodare/stats.json` in your workspace root. This file contains:

- **Per-file statistics**: Lines and characters for each file
- **Session totals**: Overall human vs AI contribution counts
- **Daily breakdown**: Day-by-day activity tracking
- **Complete history**: Every code change event with timestamps

The data format is plain JSON, making it easy to:

- Commit to version control
- Share with others
- Analyze programmatically
- View in the web viewer

### Example Data Structure

```json
{
  "version": "1.0",
  "workspaceId": "workspace-path",
  "files": {
    "src/example.ts": {
      "humanLines": 145,
      "aiLines": 67,
      "humanChars": 3421,
      "aiChars": 1523,
      "history": [...]
    }
  },
  "sessionStats": {
    "totalHumanLines": 145,
    "totalAiLines": 67,
    "totalHumanChars": 3421,
    "totalAiChars": 1523
  },
  "dailyStats": [
    {
      "date": "2025-01-15",
      "humanLines": 145,
      "aiLines": 67,
      "humanChars": 3421,
      "aiChars": 1523,
      "events": 42
    }
  ],
  "lastUpdated": 1705401234567
}
```

## AI Detection Methods

The extension uses multiple methods to accurately classify code:

1. **Inline Completion API**: Tracks when you accept VS Code inline completions (GitHub Copilot, etc.)
2. **Heuristic Analysis**: Identifies large insertions (>50 characters) or multi-line changes as likely AI-generated
3. **Pattern Recognition**: Detects formatted code blocks and paste operations
4. **Smart Defaults**: Small, incremental changes are classified as human-written

## What Gets Tracked

- All code files in your workspace
- Lines of code (human vs AI)
- Character count
- File-by-file breakdown
- Historical timeline of all changes
- Operation types (add/delete/modify)
- Timestamps for every event

## What Doesn't Get Tracked

The extension automatically skips:

- `.whodare/` directory (to avoid tracking itself)
- `node_modules/` directories
- `.git/` directories
- `dist/`, `build/`, `out/` directories
- `.log` files
- Other auto-generated files

## Getting Started

1. **Download & Install**: Download the `.vsix` file from [https://whodare.joshsparks.dev/](https://whodare.joshsparks.dev/) and install it in VS Code (see Installation section above)
2. **Start Coding**: Just write code normally - tracking happens automatically!
3. **Check Status Bar**: See your Human vs AI percentage in real-time in the bottom-left status bar
4. **View Detailed Stats**: Click the status bar item or run the `whoDare: Show Code Statistics` command
5. **Share Your Stats**: Commit `.whodare/stats.json` to GitHub
6. **Visualize Online**: Visit [https://whodare.joshsparks.dev/](https://whodare.joshsparks.dev/) and enter your repo URL to see beautiful visualizations

## Configuration

The extension works out of the box with no configuration needed. Optional settings:

- **Custom Encryption Key**: Set `whoDare.encryptionKey` in VS Code settings if you want to use a custom encryption key for your statistics file

## Sharing Your Statistics

1. Make sure `.whodare/stats.json` is committed to your repository
2. Push to GitHub
3. Share the link: `https://whodare.joshsparks.dev/?repo=YOUR_GITHUB_REPO_URL`
4. Others can view your coding statistics with beautiful visualizations!

## Support

For issues, questions, or suggestions, please open an issue on [GitHub](https://github.com/TheSecondChance/WhoDare_extension/issues).

## License

MIT License - feel free to use this extension for any purpose.

## Acknowledgments

Built with love to help developers understand their coding patterns and AI tool usage.
