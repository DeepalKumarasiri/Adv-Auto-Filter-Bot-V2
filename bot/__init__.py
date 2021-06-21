#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", "3206260"))

API_HASH = os.environ.get("API_HASH", "fbc8918eed3b68ccfd80283cf53db785")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1822577927:AAF1rmYtTmKV3dtWVJF8IigR2E3eIomkNVU")

DB_URI = os.environ.get("DB_URI", "mongodb+srv://Gamy_Gamin:Gamy_Gamin@cluster0.89qnu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("USER_SESSION", "BQCsZ-lMkKtGL2e5RKjCmORRzivRWbw0YhH7KhG2nPdwudBDCbSuEGNclG5dnMhqRfDVc8Z1bV5LvUirwACqnO2Id6D9np92MxqrLDLMVdm_et09igjXNK8VTxgO7Ww9eJyMkfbF7tsRyRhFdJzP5V-DxM-n6QmxIxPx_o3BwWUv05dUgjsw0T1cc2cltRXboZsJm5DmjElhubPjjzJHu8OsJCTBlFXHte2-BN720qoLU4fGJSPubk0t-U-W6VV-2iR5B1MIlWokHwZMyN9oqlVhrI-cBEpDuWH9ExcOzd39L2BUp0tpQpETanIakSoIJRNb29HxNkgdZ82lAr4gVus7ZS2DfgA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
