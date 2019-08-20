"""Added exams table

Revision ID: 7949fc1eec4f
Revises: 31b6ca19635d
Create Date: 2019-08-21 00:22:33.444489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7949fc1eec4f"
down_revision = "31b6ca19635d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "exams",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("pass_value", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_exams_id"), "exams", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_exams_id"), table_name="exams")
    op.drop_table("exams")
    # ### end Alembic commands ###
