"""Resource classes for fields.custom_field_values_apps."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import CustomFieldValueUpdateDetails, MultipleCustomFieldValuesUpdateDetails


class FieldCustomFieldValuesApps(SyncAPIResource):
    """Synchronous resource for fields.custom_field_values_apps."""

    def update_multiple(
        self,
        body: MultipleCustomFieldValuesUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom fields"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        self._client._request(
            "POST",
            "/rest/api/3/app/field/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    def update(
        self,
        field_id_or_key: str,
        body: CustomFieldValueUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom field value"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        self._client._request(
            "PUT",
            f"/rest/api/3/app/field/{field_id_or_key}/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None


class AsyncFieldCustomFieldValuesApps(AsyncAPIResource):
    """Asynchronous resource for fields.custom_field_values_apps."""

    async def update_multiple(
        self,
        body: MultipleCustomFieldValuesUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom fields"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        await self._client._request(
            "POST",
            "/rest/api/3/app/field/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None

    async def update(
        self,
        field_id_or_key: str,
        body: CustomFieldValueUpdateDetails,
        *,
        generate_changelog: bool | None = None,
    ) -> None:
        """Update custom field value"""
        params = self._client._build_params(**{"generateChangelog": generate_changelog})
        await self._client._request(
            "PUT",
            f"/rest/api/3/app/field/{field_id_or_key}/value",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return None
