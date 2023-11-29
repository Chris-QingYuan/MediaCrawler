import pytest

from media_platform.xhs.client import XHSClient
from media_platform.xhs.core import XiaoHongShuCrawler


@pytest.fixture
def xhs_crawler():
    return XiaoHongShuCrawler()


@pytest.fixture
def xhs_client(xhs_crawler: XiaoHongShuCrawler):
    _, _, httpx_proxy = xhs_crawler.create_proxy_info()
    return xhs_crawler.create_xhs_client(httpx_proxy)


@pytest.mark.asyncio
async def test_get_note_by_id(xhs_client: XHSClient):
    """test get note by id"""
    note_id = (
        "65588c9c000000003203219d"  # a random note manually copied from xiaohongshu
    )
    note = await xhs_client.get_note_by_id(note_id)
    assert note["note_id"] == note_id
