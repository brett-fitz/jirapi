"""Resource classes for the JQL functions (apps) API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    JqlFunctionPrecomputationGetByIdRequest,
    JqlFunctionPrecomputationGetByIdResponse,
    JqlFunctionPrecomputationUpdateRequestBean,
    JqlFunctionPrecomputationUpdateResponse,
    PageBean2JqlFunctionPrecomputationBean,
)


class JqlFunctionsApps(SyncAPIResource):
    """Synchronous resource for the JQL functions (apps) API group."""

    def get_precomputations(
        self,
        *,
        function_key: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
    ) -> PageBean2JqlFunctionPrecomputationBean:
        """Get precomputations (apps)"""
        params = self._client._build_params(
            **{
                "functionKey": function_key,
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
            }
        )
        resp = self._client._request("GET", "/rest/api/3/jql/function/computation", params=params)
        return PageBean2JqlFunctionPrecomputationBean.model_validate(resp.json())

    def update_precomputations(
        self,
        body: JqlFunctionPrecomputationUpdateRequestBean,
        *,
        skip_not_found_precomputations: bool | None = None,
    ) -> JqlFunctionPrecomputationUpdateResponse:
        """Update precomputations (apps)"""
        params = self._client._build_params(
            **{"skipNotFoundPrecomputations": skip_not_found_precomputations}
        )
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationUpdateResponse.model_validate(resp.json())

    def get_precomputations_by_id(
        self, body: JqlFunctionPrecomputationGetByIdRequest, *, order_by: str | None = None
    ) -> JqlFunctionPrecomputationGetByIdResponse:
        """Get precomputations by ID (apps)"""
        params = self._client._build_params(**{"orderBy": order_by})
        resp = self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation/search",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationGetByIdResponse.model_validate(resp.json())


class AsyncJqlFunctionsApps(AsyncAPIResource):
    """Asynchronous resource for the JQL functions (apps) API group."""

    async def get_precomputations(
        self,
        *,
        function_key: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
    ) -> PageBean2JqlFunctionPrecomputationBean:
        """Get precomputations (apps)"""
        params = self._client._build_params(
            **{
                "functionKey": function_key,
                "startAt": start_at,
                "maxResults": max_results,
                "orderBy": order_by,
            }
        )
        resp = await self._client._request(
            "GET", "/rest/api/3/jql/function/computation", params=params
        )
        return PageBean2JqlFunctionPrecomputationBean.model_validate(resp.json())

    async def update_precomputations(
        self,
        body: JqlFunctionPrecomputationUpdateRequestBean,
        *,
        skip_not_found_precomputations: bool | None = None,
    ) -> JqlFunctionPrecomputationUpdateResponse:
        """Update precomputations (apps)"""
        params = self._client._build_params(
            **{"skipNotFoundPrecomputations": skip_not_found_precomputations}
        )
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationUpdateResponse.model_validate(resp.json())

    async def get_precomputations_by_id(
        self, body: JqlFunctionPrecomputationGetByIdRequest, *, order_by: str | None = None
    ) -> JqlFunctionPrecomputationGetByIdResponse:
        """Get precomputations by ID (apps)"""
        params = self._client._build_params(**{"orderBy": order_by})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/jql/function/computation/search",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JqlFunctionPrecomputationGetByIdResponse.model_validate(resp.json())
