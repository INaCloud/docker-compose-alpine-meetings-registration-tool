"""cascade participant for activity log

Revision ID: 1a1703217f7b
Revises: 233aaf9866c6
Create Date: 2015-05-06 17:44:19.495748

"""

# revision identifiers, used by Alembic.
revision = '1a1703217f7b'
down_revision = '233aaf9866c6'

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('activity_log_participant_id_fkey', 'activity_log',
                       type_='foreignkey')
    op.create_foreign_key('activity_log_participant_id_fkey',
                          'activity_log', 'participant',
                          ['participant_id'], ['id'],
                          ondelete='CASCADE')

    op.drop_constraint('custom_field_value_participant_id_fkey',
                       'custom_field_value',
                       type_='foreignkey')
    op.create_foreign_key('custom_field_value_participant_id_fkey',
                          'custom_field_value', 'participant',
                          ['participant_id'], ['id'],
                          ondelete='CASCADE')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('activity_log_participant_id_fkey', 'activity_log',
                       type_='foreignkey')
    op.create_foreign_key('activity_log_participant_id_fkey',
                          'activity_log', 'participant',
                          ['participant_id'], ['id'])

    op.drop_constraint('custom_field_value_participant_id_fkey',
                       'custom_field_value',
                       type_='foreignkey')
    op.create_foreign_key('custom_field_value_participant_id_fkey',
                          'custom_field_value', 'participant',
                          ['participant_id'], ['id'])

    ### end Alembic commands ###