import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.io.IOException;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class PaymentServiceImplTest {

    @Mock
    private CommissionServiceInvoker invokerMock;

    private PaymentServiceImpl paymentService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);
        paymentService = new PaymentServiceImpl(invokerMock);
    }

    @Test
    void testWithdrawCommission_Successful() throws IOException, InvalidAmountException, DuplicateTransactionId, InsufficientFundException {
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
    void testWithdrawCommission_ThrowsIOException() throws IOException {
        // Arrange
        double amount = 100.0;
        when(invokerMock.withdraw(anyString(), anyDouble())).thenThrow(new IOException());

        // Act & Assert
        assertThrows(IOException.class, () -> paymentService.withdrawCommission(amount));
    }

    @Test
    void testWithdrawCommission_InvalidAmount() {
        // Arrange
        double amount = -100.0; // Invalid amount

        // Act & Assert
        assertThrows(InvalidAmountException.class, () -> paymentService.withdrawCommission(amount));
    }


    @Test
    void testWithdrawCommission_ThrowsDuplicateTransactionId() throws IOException, InvalidAmountException, DuplicateTransactionId, InsufficientFundException {
        // Arrange
        String transactionId = "TXN123";
        double amount = 100.0;

        // Create a mock for PaymentServiceImpl
        PaymentServiceImpl paymentServiceMock = mock(PaymentServiceImpl.class);

        // Stub the behavior of isDuplicateTransactionId to return true on the mock object
        when(paymentServiceMock.isDuplicateTransactionId(transactionId)).thenReturn(true);

        // Act & Assert
        assertThrows(DuplicateTransactionId.class, () -> paymentServiceMock.withdrawCommission(amount));

        // Verify that isDuplicateTransactionId was invoked with the correct arguments on the mock object
        verify(paymentServiceMock).isDuplicateTransactionId(transactionId);
    }




    @Test
    void testWithdrawCommission_ThrowsInsufficientFundException() throws IOException, InvalidAmountException, DuplicateTransactionId {
        // Arrange
        double amount = 70.0; // Invalid amount

        // Act & Assert
        assertThrows(InsufficientFundException.class, () -> paymentService.withdrawCommission(amount));
    }


    @Test
    void testRollbackCommission_Successful() throws IOException, InvalidTransactionId, AlreadyReversedException {
        // Arrange
        String transactionId = "TXN123";
        when(invokerMock.rollback(transactionId)).thenReturn(true);

        // Act
        boolean result = paymentService.rollbackCommission(transactionId);

        // Assert
        assertTrue(result);
        verify(invokerMock).rollback(transactionId);
    }

    @Test
    void testRollbackCommission_ThrowsIOException() throws IOException {
        // Arrange
        String transactionId = "TXN123";
        doThrow(new IOException()).when(invokerMock).rollback(transactionId);

        // Act & Assert
        assertThrows(IOException.class, () -> paymentService.rollbackCommission(transactionId));
    }

    @Test
    void testRollbackCommission_ThrowsInvalidTransactionId() throws IOException {
        // Arrange
        String transactionId = "invalid_id";

        // Act & Assert
        assertThrows(InvalidTransactionId.class, () -> paymentService.rollbackCommission(transactionId));
    }

    @Test
    void testRollbackCommission_ThrowsAlreadyReversedException() throws IOException {
        // Arrange
        String transactionId = "already_reversed_id";
        doThrow(new AlreadyReversedException("Transaction already reversed")).when(invokerMock).rollback(transactionId);

        // Act & Assert
        assertThrows(AlreadyReversedException.class, () -> paymentService.rollbackCommission(transactionId));
    }
}
