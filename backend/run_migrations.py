from sql_app.migrations import CreateProductTableMigration
from sql_app.migrations import CreateProductsPriceTableMigration
from sql_app.migrations import CreateUserTableMigration
from sql_app.migrations import CreateUsersProductsTable

if __name__ == '__main__':
    CreateUserTableMigration().up()
    CreateProductTableMigration().up()
    CreateUsersProductsTable().up()
    CreateProductsPriceTableMigration().up()
