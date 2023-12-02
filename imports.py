from flask import Flask, Blueprint, redirect, render_template, request, session, url_for
from src.core.classes.user import User
from src.tools import generate_password, getConfigurate, is_valid_password, is_valid_username
from routes import routes
from src.examples_ui import examples_ui
