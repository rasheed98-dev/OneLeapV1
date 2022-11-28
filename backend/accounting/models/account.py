from django.db import models
from djmoney.models.fields import MoneyField
from treenode.models import TreeNodeModel


class TransactionTypeChoices(models.TextChoices):
    pass


class Account(TreeNodeModel):
    name = models.CharField('Name', max_length=255)
    code = models.IntegerField(unique=True)

    treenode_display_field = "name"


class Transaction(models.Model):
    pass


class JournalEntry(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    amount = MoneyField(max_digits=19, decimal_places=2, null=True)
