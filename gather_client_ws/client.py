import asyncio
import logging
from random import randint

import websockets
from tapioca_gather import Gather

from .actions import set_actions_methods
from .events_pb2 import ServerClientBatch
from .helpers import get_logger


def get_txn_id() -> int:
    return randint(0, 4294967295)


class GatherClient:
    def __init__(
        self,
        api_key,
        space_id,
        callback=None,
        log_level=logging.INFO,
        hearbeat_interval=15,
    ):
        self._api_key = api_key
        self._space_id = space_id.replace("/", "\\")
        self._callback = callback
        self._ws = None
        self._logger = get_logger(log_level=log_level)
        self._heartbeat_interval = hearbeat_interval
        self._user_id = None
        set_actions_methods(self)

    async def _consumer(self):
        if self._ws is None or not self._ws.open:
            self._logger.warning("Not connected")
            return
        self._logger.debug("Receiving messages")
        while True:
            message = await self._ws.recv()
            server_response = ServerClientBatch()
            server_response.ParseFromString(message)
            if self._callback is not None:
                await self._callback(self, server_response)
            self._logger.debug(f"Message received: {server_response}")

    async def _heartbeat(self):
        if self._ws is None or not self._ws.open:
            self._logger.warning("Not connected")
            return
        while True:
            await self.client_heartbeat()
            self._logger.debug("Heartbeat sent")
            await asyncio.sleep(self._heartbeat_interval)

    async def _connect(self):
        api = Gather(api_key=self._api_key)
        url = api.game_server_assignment(space_id=self._space_id).get()().data
        while True:
            try:
                self._ws = await websockets.connect(url)
                self._logger.info(f"Connected to {url}")
                break
            except Exception as e:
                self._logger.error(f"Conenction error: {e}")
                await asyncio.sleep(3)
                self._logger.debug("Retrying to connect")
        await self.init(space_id=self._space_id, api_key=self._api_key)
        message = await self._ws.recv()
        server_response = ServerClientBatch()
        server_response.ParseFromString(message)
        if len(server_response.events) == 0:
            self._logger.error("Connection not ready")
            await self._ws.close()
            return
        event = server_response.events[0]
        if event.WhichOneof("event") != "ready":
            self._logger.error("Connection not ready")
            await self._ws.close()
            return
        self._user_id = event.ready.id
        self._logger.info(f"Connected as user {self._user_id}")

    async def run(self, producer, *args, **kwargs):
        await self._connect()
        _, pending = await asyncio.wait(
            [
                asyncio.create_task(self._consumer()),
                asyncio.create_task(self._heartbeat()),
                asyncio.create_task(producer(self, *args, **kwargs)),
            ],
            return_when=asyncio.FIRST_COMPLETED,
        )
        if self._ws is not None:
            await self._ws.close()
        for task in pending:
            task.cancel()
