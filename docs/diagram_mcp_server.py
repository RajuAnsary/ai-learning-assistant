#!/usr/bin/env python3
"""
Custom MCP Server for Architecture Diagram Generation
This creates an MCP server that can generate architecture diagrams through Kiro
"""

import asyncio
import json
import sys
from typing import Any, Dict, List, Optional

# MCP Server implementation
class DiagramMCPServer:
    def __init__(self):
        self.name = "diagram-generator"
        self.version = "1.0.0"
        
    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP requests"""
        method = request.get("method")
        params = request.get("params", {})
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": self.name,
                        "version": self.version
                    }
                }
            }
        
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "tools": [
                        {
                            "name": "generate_architecture_diagram",
                            "description": "Generate architecture diagram for AI-Powered Learning & Productivity Assistant",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "Title for the diagram",
                                        "default": "AI-Powered Learning & Productivity Assistant Architecture"
                                    },
                                    "filename": {
                                        "type": "string", 
                                        "description": "Output filename (without extension)",
                                        "default": "ai_learning_assistant_architecture"
                                    },
                                    "direction": {
                                        "type": "string",
                                        "description": "Diagram direction (TB, LR, BT, RL)",
                                        "default": "TB"
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        
        elif method == "tools/call":
            tool_name = params.get("name")
            if tool_name == "generate_architecture_diagram":
                return await self.generate_diagram(request.get("id"), params.get("arguments", {}))
        
        # Default response for unhandled methods
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "error": {
                "code": -32601,
                "message": f"Method not found: {method}"
            }
        }
    
    async def generate_diagram(self, request_id: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate the architecture diagram"""
        try:
            from diagrams import Diagram, Cluster
            from diagrams.aws.compute import ECS, Lambda
            from diagrams.aws.database import RDS, Dynamodb
            from diagrams.aws.network import ELB, APIGateway
            from diagrams.aws.storage import S3
            from diagrams.aws.ml import Sagemaker
            from diagrams.onprem.client import Users
            from diagrams.onprem.database import PostgreSQL
            from diagrams.programming.framework import React
            from diagrams.programming.language import Python, TypeScript
            
            title = args.get("title", "AI-Powered Learning & Productivity Assistant Architecture")
            filename = args.get("filename", "ai_learning_assistant_architecture")
            direction = args.get("direction", "TB")
            
            with Diagram(title, 
                        show=False, 
                        filename=filename,
                        direction=direction,
                        graph_attr={"fontsize": "45", "bgcolor": "white"}):
                
                # Users
                users = Users("Beginner Developers")
                
                # Frontend Layer
                with Cluster("User Interface Layer"):
                    web_ui = React("Web UI")
                    mobile_app = TypeScript("Mobile App")
                    cli_tool = Python("CLI Tool")
                    
                # API Gateway
                api_gateway = APIGateway("API Gateway\\n(Auth, Rate Limiting)")
                
                # Core Services Layer
                with Cluster("Core Services Layer"):
                    with Cluster("Developer Model"):
                        dev_service = ECS("Developer Model Service")
                        dev_db = RDS("Developer Database")
                        dev_service >> dev_db
                        
                    with Cluster("Domain Model"):
                        domain_service = ECS("Domain Model Service")
                        knowledge_base = PostgreSQL("Knowledge Base")
                        domain_service >> knowledge_base
                        
                    with Cluster("Tutoring Model"):
                        tutoring_service = ECS("Tutoring Model Service")
                        session_store = Dynamodb("Session Store")
                        tutoring_service >> session_store
                
                # Specialized Services
                with Cluster("Specialized Services"):
                    concept_explainer = Lambda("Concept Explainer")
                    learning_path = Lambda("Learning Path Generator")
                    productivity_helper = Lambda("Productivity Helper")
                
                # AI Engine Layer
                with Cluster("AI Engine Layer"):
                    llm_integration = Sagemaker("LLM Integration\\n(OpenAI API)")
                    vector_db = Dynamodb("Vector Database\\n(Embeddings)")
                    code_analyzer = Lambda("Code Parser\\n& Analyzer")
                
                # Storage Layer
                with Cluster("Data Storage"):
                    file_storage = S3("File Storage\\n(Code Examples)")
                    cache_layer = Dynamodb("Cache Layer")
                
                # Load Balancer
                load_balancer = ELB("Load Balancer")
                
                # Define connections
                users >> [web_ui, mobile_app, cli_tool]
                [web_ui, mobile_app, cli_tool] >> load_balancer
                load_balancer >> api_gateway
                
                api_gateway >> [dev_service, domain_service, tutoring_service]
                api_gateway >> [concept_explainer, learning_path, productivity_helper]
                
                [concept_explainer, learning_path, productivity_helper] >> llm_integration
                [concept_explainer, learning_path, productivity_helper] >> vector_db
                productivity_helper >> code_analyzer
                
                [dev_service, domain_service, tutoring_service] >> cache_layer
                domain_service >> file_storage
                
                llm_integration >> vector_db
                code_analyzer >> vector_db
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"✅ Architecture diagram generated successfully!\n📁 File saved as: {filename}.png\n🎨 Title: {title}\n📐 Direction: {direction}"
                        }
                    ]
                }
            }
            
        except ImportError as e:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"❌ Missing required package: {e}\n📦 Install with: pip install diagrams\n🔧 Also need: winget install graphviz"
                        }
                    ]
                }
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"❌ Error generating diagram: {e}\n💡 Check that Graphviz is installed and in PATH"
                        }
                    ]
                }
            }

async def main():
    """Main MCP server loop"""
    server = DiagramMCPServer()
    
    while True:
        try:
            # Read JSON-RPC request from stdin
            line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
            if not line:
                break
                
            request = json.loads(line.strip())
            response = await server.handle_request(request)
            
            # Write JSON-RPC response to stdout
            print(json.dumps(response), flush=True)
            
        except json.JSONDecodeError:
            continue
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {e}"
                }
            }
            print(json.dumps(error_response), flush=True)

if __name__ == "__main__":
    asyncio.run(main())