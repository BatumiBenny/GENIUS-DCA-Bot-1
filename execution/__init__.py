# execution/__init__.py
# Package marker - Python module initialization

"""
Execution package for GENIUS-DCA-Bot
Handles trading execution, order management, and regime detection
"""

__version__ = "1.0.0"
__author__ = "GENIUS Trading Bot"
__all__ = [
    'MarketRegimeEngine',
    'OrderExecutor',
]

# Try to import key modules
try:
    from execution.regime_engine import MarketRegimeEngine
except ImportError:
    pass

try:
    from execution.order_executor import OrderExecutor
except ImportError:
    pass
