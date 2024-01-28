
from flwr.server.app import ServerConfig

from slower.simulation.app import start_simulation
from slower.server.strategy import PlainSlStrategy


from cifar_client import CifarClient
from server_segment import SimpleServerModelSegment
from constants import N_CLIENT_LAYERS, CLIENT_RESOURCES, N_CLIENTS, N_EPOCHS


def main():
    client_fn = CifarClient
    strategy = PlainSlStrategy(
        common_server=False,
        init_server_model_segment_fn=SimpleServerModelSegment,
    )
    start_simulation(
        client_fn=client_fn,
        num_clients=N_CLIENTS,
        strategy=strategy,
        client_resources=CLIENT_RESOURCES,
        config=ServerConfig(num_rounds=N_EPOCHS)
    )


if __name__ == "__main__":
    main()
