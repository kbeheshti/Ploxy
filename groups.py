from utils.requests import RequestClient


class Group:
    def __init__(self, group_id, requests: RequestClient):
        self.member_count = None
        self.description = None
        self.name = None
        self.group_id = group_id
        self.requests = requests
        self.base = "https://groups.roblox.com"

    async def update_group_info(self):
        data = await self.requests.request(
            "GET", f"{self.base}/v1/groups/{self.group_id}"
        )
        self.name = data.get("name")
        self.description = data.get("description")
        self.member_count = data.get("memberCount")

    async def update_user_role(self, user_id, new_role):
        await self.requests.request(
            "PATCH",
            f"{self.base}/v1/groups/{self.group_id}/users/{user_id}",
            data={"roleId": new_role},
        )
