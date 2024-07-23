import java.io.IOException;

public interface CommissionServiceInvoker {
    boolean withdraw(String transactionId, double amount) throws IOException;
    boolean rollback(String transactionId) throws IOException;
}
