# MIT licensed
# Copyright (c) 2020 Felix Yan <felixonmars@archlinux.org>, et al.

import pytest
pytestmark = [
  pytest.mark.asyncio(scope="session"),
  pytest.mark.needs_net,
]

async def test_mercurial(get_version):
  assert await get_version("example", {
    "source": "mercurial",
    "mercurial": "https://repo.mercurial-scm.org/hg-website/json-tags",
  }) == "v1.0"
