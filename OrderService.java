package com.demo.order;

public class OrderService {

    private String apiKey = "secret123";

    public void createOrder(String userId) {

        String query =
                "SELECT * FROM USERS WHERE ID='"
                + userId + "'";

        System.out.println(query);

        System.out.println(
                "Order created"
        );
    }
}