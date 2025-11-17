from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "urls",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("short", sa.String, unique=True),
        sa.Column("long", sa.String),
        sa.Column("clicks", sa.Integer, default=0),
        sa.Column("created_at", sa.DateTime),
        sa.Column("last_accessed", sa.DateTime),
    )

def downgrade():
    op.drop_table("urls")
