"""Genetic Programming in Python, with a scikit-learn inspired API

``gplearn`` is a set of algorithms for learning genetic programming models.

"""
import importlib.metadata
import os

# 从pyproject.toml中获取版本号，实现版本号的单一管理
try:
    __version__ = importlib.metadata.version('gplearn')
except ImportError:
    # 如果无法导入，使用默认版本号（开发环境可能需要）
    __version__ = '0.5.dev0'

__all__ = ['genetic', 'functions', 'fitness']
