# Custom Diagram MCP Server

This is a custom Model Context Protocol (MCP) server that generates architecture diagrams for the AI-Powered Learning & Productivity Assistant project.

## 🚀 Features

- **Architecture Diagram Generation**: Creates professional AWS-style architecture diagrams
- **MCP Integration**: Works seamlessly with Kiro's MCP system
- **Customizable**: Supports different titles, filenames, and diagram directions
- **Auto-approved**: Pre-configured for automatic execution in Kiro

## 📋 Prerequisites

1. **Python 3.8+** with required packages:
   ```bash
   pip install diagrams graphviz
   ```

2. **Graphviz** system installation:
   ```bash
   winget install graphviz
   ```

3. **Kiro IDE** with MCP support

## ⚙️ Installation

### Method 1: Direct Configuration (Current Setup)

The MCP server is already configured in your `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "custom-diagram": {
      "command": "python",
      "args": ["diagram_mcp_server.py"],
      "env": {
        "PYTHONPATH": "."
      },
      "disabled": false,
      "autoApprove": ["generate_architecture_diagram"]
    }
  }
}
```

### Method 2: Package Installation (Optional)

For system-wide installation:

```bash
pip install -e .
```

Then update MCP config to use:
```json
{
  "command": "diagram-mcp-server"
}
```

## 🎯 Usage

### Through Kiro Chat

Once configured, you can use the MCP server directly in Kiro:

```
Generate an architecture diagram for the AI learning assistant
```

### Available Parameters

- **title**: Diagram title (default: "AI-Powered Learning & Productivity Assistant Architecture")
- **filename**: Output filename without extension (default: "ai_learning_assistant_architecture")  
- **direction**: Diagram layout direction - TB, LR, BT, RL (default: "TB")

### Example MCP Tool Call

```json
{
  "name": "generate_architecture_diagram",
  "arguments": {
    "title": "My Custom Architecture",
    "filename": "my_architecture",
    "direction": "LR"
  }
}
```

## 🧪 Testing

Test the MCP server functionality:

```bash
python test_mcp_server.py
```

## 📁 Generated Files

The server creates PNG files in the current directory:
- `ai_learning_assistant_architecture.png` (default)
- Custom filenames as specified

## 🔧 Troubleshooting

### Common Issues

1. **"Graphviz not found"**
   - Install Graphviz: `winget install graphviz`
   - Add to PATH: `C:\Program Files\Graphviz\bin`

2. **"diagrams module not found"**
   - Install: `pip install diagrams`

3. **MCP server not connecting**
   - Check Kiro MCP panel for connection status
   - Verify file paths in mcp.json are correct
   - Restart Kiro after configuration changes

### Debug Mode

Enable debug logging by setting:
```json
{
  "env": {
    "PYTHONPATH": ".",
    "DEBUG": "true"
  }
}
```

## 🏗️ Architecture Components

The generated diagram includes:

- **User Interface Layer**: Web UI, Mobile App, CLI Tool
- **API Gateway**: Authentication and rate limiting
- **Core Services**: Developer Model, Domain Model, Tutoring Model
- **Specialized Services**: Concept Explainer, Learning Path Generator, Productivity Helper
- **AI Engine Layer**: LLM Integration, Vector Database, Code Parser
- **Data Storage**: File Storage, Cache Layer, Databases

## 🔄 Updates

To update the diagram generation logic:

1. Edit `diagram_mcp_server.py`
2. Restart Kiro or reload MCP servers
3. Test with new parameters

## 📞 Support

If you encounter issues:

1. Check the MCP server logs in Kiro
2. Verify all dependencies are installed
3. Test the server independently with `test_mcp_server.py`
4. Check file permissions and paths