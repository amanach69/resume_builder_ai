"""Logging configuration module."""
import os
import logging
from typing import Dict, Any
from src.config.config_loader import ConfigLoader

def setup_logging(config: Dict[str, Any] = None) -> None:
    """Set up logging configuration.
    
    Args:
        config (Dict[str, Any], optional): Logging configuration. Defaults to None.
    """
    if config is None:
        config = ConfigLoader().get_logging_config()
        
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(config['file'])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, config['level']),
        format=config['format'],
        handlers=[
            logging.FileHandler(config['file']),
            logging.StreamHandler()
        ]
    )
    
    # Set third-party loggers to WARNING
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('streamlit').setLevel(logging.WARNING)
    
    logger = logging.getLogger(__name__)
    logger.info("Logging configured successfully")
