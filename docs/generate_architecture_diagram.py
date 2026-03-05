#!/usr/bin/env python3
"""
Generate architecture diagram for AI-Powered Learning & Productivity Assistant

This script creates a visual architecture diagram using the Python diagrams library
and AWS service icons to represent the system components and their relationships.

Requirements:
- Python 3.x
- diagrams library (pip install diagrams)
- Graphviz (winget install graphviz)

Usage:
    python generate_architecture_diagram.py

Output:
    ai_learning_assistant_architecture.png
"""

try:
    from diagrams import Diagram, Cluster, Edge
    from diagrams.aws.compute import ECS, Lambda
    from diagrams.aws.database import RDS, Dynamodb
    from diagrams.aws.network import ELB, APIGateway
    from diagrams.aws.storage import S3
    from diagrams.aws.ml import Sagemaker
    from diagrams.onprem.client import Users
    from diagrams.onprem.database import PostgreSQL
    from diagrams.programming.framework import React
    from diagrams.programming.language import Python, TypeScript
    
    print("🎨 Creating AI-Powered Learning & Productivity Assistant Architecture Diagram...")
    
    with Diagram("AI-Powered Learning & Productivity Assistant Architecture", 
                 show=False, 
                 filename="ai_learning_assistant_architecture",
                 direction="TB",
                 graph_attr={"fontsize": "45", "bgcolor": "white"}):
        
        # Users
        users = Users("Beginner Developers")
        
        # Frontend Layer
        with Cluster("User Interface Layer"):
            web_ui = React("Web UI")
            mobile_app = TypeScript("Mobile App")
            cli_tool = Python("CLI Tool")
            
        # API Gateway
        api_gateway = APIGateway("API Gateway\n(Auth, Rate Limiting)")
        
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
            llm_integration = Sagemaker("LLM Integration\n(OpenAI API)")
            vector_db = Dynamodb("Vector Database\n(Embeddings)")
            code_analyzer = Lambda("Code Parser\n& Analyzer")
        
        # Storage Layer
        with Cluster("Data Storage"):
            file_storage = S3("File Storage\n(Code Examples)")
            cache_layer = Dynamodb("Cache Layer")
        
        # Load Balancer
        load_balancer = ELB("Load Balancer")
        
        # Define connections with proper flow
        users >> [web_ui, mobile_app, cli_tool]
        [web_ui, mobile_app, cli_tool] >> load_balancer
        load_balancer >> api_gateway
        
        # API Gateway to core services
        api_gateway >> [dev_service, domain_service, tutoring_service]
        api_gateway >> [concept_explainer, learning_path, productivity_helper]
        
        # Specialized services to AI engine
        [concept_explainer, learning_path, productivity_helper] >> llm_integration
        [concept_explainer, learning_path, productivity_helper] >> vector_db
        productivity_helper >> code_analyzer
        
        # Core services to storage
        [dev_service, domain_service, tutoring_service] >> cache_layer
        domain_service >> file_storage
        
        # AI Engine internal connections
        llm_integration >> vector_db
        code_analyzer >> vector_db
    
    print("✅ Architecture diagram generated successfully!")
    print("📁 File saved as: ai_learning_assistant_architecture.png")
    print("🔗 Referenced in: .kiro/specs/student-ai-assistant/design.md")
    
except ImportError as e:
    print(f"❌ Missing required package: {e}")
    print("� To install required packages:")
    print("   pip install diagrams")
    print("   winget install graphviz")

except Exception as e:
    print(f"❌ Error generating diagram: {e}")
    print("💡 Alternative: The ASCII diagram in the design document provides a comprehensive view.")
    print("🔧 Troubleshooting:")
    print("   - Ensure Graphviz is installed: winget install graphviz")
    print("   - Add Graphviz to PATH: C:\\Program Files\\Graphviz\\bin")