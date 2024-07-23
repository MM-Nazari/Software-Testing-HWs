
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

// Implement PaymentService interface
class PaymentServiceImpl implements PaymentService {
    // It will set at Constructor
    private CommissionServiceInvoker invoker;

    PaymentServiceImpl(CommissionServiceInvoker invoker) {
        this.invoker = invoker;
    }

    @Override
    public boolean withdrawCommission(double amount) throws IOException, InvalidAmountException, DuplicateTransactionId, InsufficientFundException {
        if (isInvalidAmount(amount)) {
            throw new InvalidAmountException("Invalid amount: " + amount);
        }

        String transactionId = generateTransactionId();

        // Check for duplicate transaction ID
        if (isDuplicateTransactionId(transactionId)) {
            throw new DuplicateTransactionId("Duplicate transaction ID: " + transactionId);
        }

        // Check for insufficient funds
        if (isInsufficientFunds(amount)) {
            throw new InsufficientFundException("Insufficient funds for withdrawal: " + amount);
        }

        try {
            invoker.withdraw(transactionId, amount);
            return true;
        } catch (IOException e) {
            throw e;
        }
    }

    boolean isInvalidAmount(double amount) {
        // amount should be positive
        if (amount <= 0) {
            return true;
        } else
            return false;
    }

    // Method to check if the transaction ID is duplicate
    boolean isDuplicateTransactionId(String transactionId) {
        // example of duplicate transaction id is TXN123
        if (transactionId.equals("TXN123"))
            return true;
        else
            return false;
    }

    // Method to check if there are insufficient funds
    private boolean isInsufficientFunds(double amount) {
        // consider only amount >=100 is sufficient
        if (amount < 100.0)
            return true;
        else
            return false;
    }

    @Override
    public boolean rollbackCommission(String transactionId) throws IOException, InvalidTransactionId, AlreadyReversedException {
        if (!isValidTransactionId(transactionId)) {
            throw new InvalidTransactionId("Invalid transaction ID: " + transactionId);
        }

        // Implement logic to check if the transaction is already reversed
        if (isAlreadyReversed(transactionId)) {
            throw new AlreadyReversedException("Transaction already reversed: " + transactionId);
        }

        try {
            invoker.rollback(transactionId);
            return true;
        } catch (IOException e) {
            throw e;
        }
    }

    // Method to check if the transaction ID is in the correct format
    private boolean isValidTransactionId(String transactionId) {
        // Check if the transaction ID starts with "TXN" and followed by a long number
        return transactionId != null && transactionId.startsWith("TXN") && transactionId.length() > 3;
    }

    private boolean isAlreadyReversed(String transactionId) {
        // Implement logic to check if the transaction is already reversed
        // Here, you could have a data structure to store reversed transaction IDs
        // For simplicity, let's assume we have a Set to store reversed transaction IDs
        Set<String> reversedTransactions = new HashSet<>();

        // Check if the provided transaction ID is in the set of reversed transactions
        return reversedTransactions.contains(transactionId);
    }


    // Method to generate a unique transaction ID (for simulation purpose)
    private String generateTransactionId() {
        return "TXN" + System.currentTimeMillis();
    }
}
