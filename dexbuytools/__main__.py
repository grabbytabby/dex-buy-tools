import click
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dexbuytools.helpers import get_helper
import dexbuytools.config as config
import yaml

@click.group()
def dexbuy():
    pass


@dexbuy.command()
@click.argument('network_name')
@click.argument('token_address')
@click.option('--buy_params_path', default=None)
@click.option('--wallet_data_path', default=None)
@click.option('--general_params_path', default=None)
@click.option('--dex_name', default=None)
@click.option('--custom_rpc', default=None)
def instant(network_name, token_address, buy_params_path, wallet_data_path, general_params_path, dex_name, custom_rpc):
    configuration = config.get_config(
        buy_params_path=buy_params_path,
        wallet_data_path=wallet_data_path,
        general_params_path=general_params_path)
    helper = get_helper(network_name, configuration, dex_name, custom_rpc)
    helper.buy_instantly(token_address)


@dexbuy.command()
# TODO: address, name or symbol have to be given
@click.argument('network_name')
@click.option('token_address', default=None)
@click.option('search_term', default=None)
@click.option('--buy_params_path', default=None)
@click.option('--wallet_data_path', default=None)
@click.option('--general_params_path', default=None)
def onliquidity(network_name, token_address, search_term, buy_params_path, wallet_data_path, general_params_path):
    """
        Buy once liquidity gets added for token of given address or any token that matches the given search_name or
        search_term
    """
    if token_address is None and search_term is None:
        raise ValueError("No token_address or search_term provided")

    configuration = config.get_config(
        buy_params_path=buy_params_path,
        wallet_data_path=wallet_data_path,
        general_params_path=general_params_path)
    helper = get_helper(network_name, configuration)
    helper.buy_on_liquidity(token_address, search_term)

if __name__ == '__main__':
    dexbuy()
