"""
Environment variable reader utility for Aetherius AI Assistant.
This module provides functions to read API keys and configuration from .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_openai_api_key():
    """Get OpenAI API key from environment variables."""
    return os.getenv('OPEN_AI_API_KEY', '')

def get_google_api_key():
    """Get Google API key from environment variables."""
    return os.getenv('GOOGLE_API_KEY', '')

def get_google_cse_id():
    """Get Google Custom Search Engine ID from environment variables."""
    return os.getenv('GOOGLE_CSE_ID', '')

def get_qdrant_api_key():
    """Get Qdrant API key from environment variables."""
    return os.getenv('QDRANT_API_KEY', '')

def get_qdrant_url():
    """Get Qdrant URL from environment variables."""
    return os.getenv('QDRANT_URL', '')

def get_anthropic_api_key():
    """Get Anthropic API key from environment variables."""
    return os.getenv('ANTHROPIC_API_KEY', '')

def get_gemini_api_key():
    """Get Gemini API key from environment variables."""
    return os.getenv('GEMINI_API_KEY', '')

def get_xai_api_key():
    """Get XAI API key from environment variables."""
    return os.getenv('XAI_API_KEY', '')

def get_serper_api_key():
    """Get Serper API key from environment variables."""
    return os.getenv('SERPER_API_KEY', '')

def get_zai_api_key():
    """Get ZAI API key from environment variables."""
    return os.getenv('ZAI_API_KEY', '')
