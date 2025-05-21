"""Initial database migration for Quiz Application

Revision ID: 001_initial
Revises: 
Create Date: 2025-05-21
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create quizzes table
    op.create_table(
        'quizzes',
        sa.Column('id', sa.String(), primary_key=True, index=True),
        sa.Column('category', sa.Integer(), index=True),
        sa.Column('num_questions', sa.Integer()),
        sa.Column('current_score', sa.Integer(), default=0),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('user_id', sa.String(), index=True, nullable=True)
    )
    
    # Create questions table
    op.create_table(
        'questions',
        sa.Column('id', sa.String(), primary_key=True, index=True),
        sa.Column('quiz_id', sa.String(), sa.ForeignKey('quizzes.id')),
        sa.Column('question', sa.Text()),
        sa.Column('correct_answer', sa.String())
    )
    
    # Create question_options table
    op.create_table(
        'question_options',
        sa.Column('id', sa.String(), primary_key=True, index=True),
        sa.Column('question_id', sa.String(), sa.ForeignKey('questions.id')),
        sa.Column('text', sa.String())
    )
    
    # Create user_answers table
    op.create_table(
        'user_answers',
        sa.Column('id', sa.String(), primary_key=True, index=True),
        sa.Column('question_id', sa.String(), sa.ForeignKey('questions.id')),
        sa.Column('selected_option_id', sa.String(), sa.ForeignKey('question_options.id')),
        sa.Column('is_correct', sa.Boolean(), default=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('user_id', sa.String(), index=True, nullable=True)
    )
    
    # Create quiz_results table
    op.create_table(
        'quiz_results',
        sa.Column('id', sa.String(), primary_key=True, index=True),
        sa.Column('quiz_id', sa.String(), sa.ForeignKey('quizzes.id')),
        sa.Column('score', sa.Integer()),
        sa.Column('total_questions', sa.Integer()),
        sa.Column('percentage', sa.Float()),
        sa.Column('feedback', sa.Text()),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('user_id', sa.String(), index=True, nullable=True)
    )


def downgrade():
    # Remove tables in reverse order to avoid foreign key constraints
    op.drop_table('quiz_results')
    op.drop_table('user_answers')
    op.drop_table('question_options')
    op.drop_table('questions')
    op.drop_table('quizzes')