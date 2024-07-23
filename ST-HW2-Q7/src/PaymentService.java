import java.io.IOException;

public interface PaymentService {
    boolean withdrawCommission(double amount) throws IOException, DuplicateTransactionId, InvalidAmountException, InsufficientFundException;
    boolean rollbackCommission(String transactionId) throws IOException, InvalidTransactionId, AlreadyReversedException;
}


