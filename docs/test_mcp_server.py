#!/usr/bin/env python3
"""
Test script for the custom diagram MCP server
"""

import json
import subprocess
import sys

def test_mcp_server():
    """Test the MCP server functionality"""
    
    print("🧪 Testing Custom Diagram MCP Server...")
    
    # Test requests
    test_requests = [
        # Initialize request
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0.0"}
            }
        },
        # List tools request
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        },
        # Generate diagram request
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "generate_architecture_diagram",
                "arguments": {
                    "title": "Test Architecture Diagram",
                    "filename": "test_architecture",
                    "direction": "TB"
                }
            }
        }
    ]
    
    try:
        # Start the MCP server process
        process = subprocess.Popen(
            [sys.executable, "diagram_mcp_server.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send test requests
        for i, request in enumerate(test_requests):
            print(f"📤 Sending request {i+1}: {request['method']}")
            
            # Send request
            process.stdin.write(json.dumps(request) + "\n")
            process.stdin.flush()
            
            # Read response
            response_line = process.stdout.readline()
            if response_line:
                response = json.loads(response_line.strip())
                print(f"📥 Response {i+1}: {response.get('result', response.get('error', 'No result'))}")
            else:
                print(f"❌ No response for request {i+1}")
        
        # Clean up
        process.terminate()
        process.wait()
        
        print("✅ MCP Server test completed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        if 'process' in locals():
            process.terminate()

if __name__ == "__main__":
    test_mcp_server()