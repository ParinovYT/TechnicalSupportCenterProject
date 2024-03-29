from flask import Flask, Blueprint, redirect, render_template, request, session, url_for
from src.core.classes.user import User
from src.core.classes.report import Report
from src.core.classes.mysql import MySqlBase
from src.core.classes.template_issue import TemplateIssue
from src.tools import generate_password, is_valid_password, is_valid_username
from routes import routes
from src.examples_ui import examples_ui