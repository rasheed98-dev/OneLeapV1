from django.db import models
from djmoney.models.fields import MoneyField
from treenode.models import TreeNodeModel


# class TransactionTypeChoices(models.TextChoices):
#     Expenses= "Expenses Transactions"
#     Assets= "assets Transactions"
#     Liabilities="Liabilities Transactions"
#     Income="Income Transactions"

class TransactionTypeChoices(models.TextChoices):
    Sales = "Sales"
    SalesReturn="Sales Return"
    AccountsReceivable ="Receivable"
    AccountsPayable="Accounts Payable"
    CashReceipts="Cash Receipts"
    Purchases="Purchases"
    Payroll= "Payroll"


class Account(TreeNodeModel):
    name = models.CharField('Name', max_length=255)
    code = models.IntegerField(unique=True)
    statement= models.CharField('Statement', max_length=255,
     choices=(
            ('BS', 'Balance Statement'),
            ('IS', 'Income Statement'),
            
            
        )
    
    )
    type = models.CharField(
        max_length=255,
        choices=(
            ('As', 'Asset'),
            ('Eq', 'Equity'),
            ('Li', 'Liability'),
            ('In', 'Income'),
            ('Ex', 'Expense')
        ),
        default="Ex"
    )

    treenode_display_field = "name"


class Transaction(models.Model):

   type= models.CharField(
        max_length=35,
        choices=TransactionTypeChoices.choices,
         
    )
   description= models.CharField('description', max_length=255)


class JournalEntry(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    amount = MoneyField(max_digits=19, decimal_places=2, null=True)
    type = models.CharField(
        max_length=255,
        choices=(
            ('Opening entries', 'Opening entries'),
            ('Transfer entries', 'Transfer entries'),
            ('Closing entries', 'Closing entries'),
            ('Adjusting entries', 'Adjusting entries'),
            ('Reversing entries', 'Reversing entries')
        ),
        default="Reversing entries"
    )
