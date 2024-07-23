import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.io.IOException;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class PaymentServiceImplTest {

    @Mock
    private CommisionServiceInvoker invokerMock;

    private PaymentServiceImpl paymentService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);
        paymentService = new PaymentServiceImpl(invokerMock);
    }

    @Test
    void testWithdrawCommission_Successful() throws IOException, DuplicateTransactionId, InvalidAmountException, InsufficientFundException {
        // Arrange
        double amount = 100.0;
        when(invokerMock.withdraw(anyString(), anyDouble())).thenReturn(true);

        // Act
        boolean result = paymentService.withdrawCommission(amount);

        // Assert
        assertTrue(result);
        verify(invokerMock).withdraw(anyString(), anyDouble());
    }

    @Test
    void testWithdrawCommission_ThrowsIOException() throws IOException, DuplicateTransactionId, InvalidAmountException, InsufficientFundException {
        // Arrange
        double amount = 100.0;
        when(invokerMock.withdraw(anyString(), anyDouble())).thenThrow(new IOException());

        // Act & Assert
        assertThrows(IOException.class, () -> paymentService.withdrawCommission(amount));
    }

    @Test
    void testRollbackCommission_Successful() throws InvalidTransactionId, IOException, AlreadyReversedException {
        // Arrange
        String transactionId = "TXN123";

        // Act
        boolean result = paymentService.rollbackCommission(transactionId);

        // Assert
        assertTrue(result);
        verify(invokerMock).rollback(transactionId);
    }

    @Test
    void testRollbackCommission_ThrowsIOException() throws InvalidTransactionId, IOException, AlreadyReversedException {
        // Arrange
        String transactionId = "TXN123";
        doThrow(new IOException()).when(invokerMock).rollback(transactionId);

        // Act & Assert
        assertThrows(IOException.class, () -> paymentService.rollbackCommission(transactionId));
    }
}
