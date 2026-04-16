from connector import cursor, connection
from terminal.cli import begin_cmd

begin_cmd(cursor, connection)

# free resources
cursor.close()
connection.close()
