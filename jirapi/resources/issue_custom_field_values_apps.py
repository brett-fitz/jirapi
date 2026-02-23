"""Resource classes for the Issue custom field values (apps) API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import CustomFieldValueUpdateDetails, MultipleCustomFieldValuesUpdateDetails


class IssueCustomFieldValuesApps(SyncAPIResource):
    """Synchronous resource for the Issue custom field values (apps) API group."""

    def update_multiple_custom_field_values(
        self,
        body: MultipleCustomFieldValuesUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom fields"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        resp = self._client._request(
            "POST",
            "/rest/api/3/app/field/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def update_custom_field_value(
        self,
        field_id_or_key: str,
        body: CustomFieldValueUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom field value"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        resp = self._client._request(
            "PUT",
            f"/rest/api/3/app/field/{field_id_or_key}/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncIssueCustomFieldValuesApps(AsyncAPIResource):
    """Asynchronous resource for the Issue custom field values (apps) API group."""

    async def update_multiple_custom_field_values(
        self,
        body: MultipleCustomFieldValuesUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom fields"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/app/field/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def update_custom_field_value(
        self,
        field_id_or_key: str,
        body: CustomFieldValueUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom field value"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        resp = await self._client._request(
            "PUT",
            f"/rest/api/3/app/field/{field_id_or_key}/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
