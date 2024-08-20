import flwr as fl

if __name__ == "__main__":
    # Define strategy
    strategy = fl.server.strategy.FedAvg(
        fraction_fit=1.0,
        fraction_evaluate=1.0,min_fit_clients= 2,
        min_evaluate_clients= 2,
        min_available_clients= 2,
    )

    # Start server
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=2),
        strategy=strategy,
    )
