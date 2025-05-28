package kafka_tutorial.exercise_04_ksql;

import java.util.Date;

public class Order {

    private String orderId;
    private int customerId;
    private String product;
    private int amount;
    private double price;
    private Date orderedAt;

    public Order(String orderId, int customerId, String product, int amount, double price, Date orderedAt) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.product = product;
        this.amount = amount;
        this.price = price;
        this.orderedAt = orderedAt;
    }

    public String getOrderId() {
        return orderId;
    }

    public int getCustomerId() {
        return customerId;
    }

    public String getProduct() {
        return product;
    }

    public int getAmount() {
        return amount;
    }

    public double getPrice() {
        return price;
    }

    public Date getOrderedAt() {
        return orderedAt;
    }

    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    public void setCustomerId(int customerId) {
        this.customerId = customerId;
    }

    public void setProduct(String product) {
        this.product = product;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setOrderedAt(Date orderedAt) {
        this.orderedAt = orderedAt;
    }

    @Override
    public String toString() {
        return "Order{" +
                "orderId='" + orderId + '\'' +
                ", customerId='" + customerId + '\'' +
                ", product='" + product + '\'' +
                ", amount=" + amount +
                ", price=" + price +
                ", orderedAt=" + orderedAt +
                '}';
    }
}
