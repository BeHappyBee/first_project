#!/usr/bin/env python3

print("hello world")
print("New str")

# Секретики
from dotenv import load_dotenv
import os

load_dotenv()

autor = os.getenv('AUTHOR')
print(autor)
