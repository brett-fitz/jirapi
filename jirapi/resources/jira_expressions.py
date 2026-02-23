"""Resource classes for the Jira expressions API group."""

from __future__ import annotations

from jirapi._resource import AsyncAPIResource, SyncAPIResource
from jirapi.models import (
    JExpEvaluateJiraExpressionResultBean,
    JiraExpressionEvaluateRequestBean,
    JiraExpressionForAnalysis,
    JiraExpressionsAnalysis,
)


class JiraExpressions(SyncAPIResource):
    """Synchronous resource for the Jira expressions API group."""

    def analyse_expression(
        self, body: JiraExpressionForAnalysis, *, check: str | None = None
    ) -> JiraExpressionsAnalysis:
        """Analyse Jira expression"""
        params = self._client._build_params(**{"check": check})
        resp = self._client._request(
            "POST",
            "/rest/api/3/expression/analyse",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JiraExpressionsAnalysis.model_validate(resp.json())

    def evaluate_jsis_jira_expression(
        self, body: JiraExpressionEvaluateRequestBean, *, expand: str | None = None
    ) -> JExpEvaluateJiraExpressionResultBean:
        """Evaluate Jira expression using enhanced search API"""
        params = self._client._build_params(**{"expand": expand})
        resp = self._client._request(
            "POST",
            "/rest/api/3/expression/evaluate",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JExpEvaluateJiraExpressionResultBean.model_validate(resp.json())


class AsyncJiraExpressions(AsyncAPIResource):
    """Asynchronous resource for the Jira expressions API group."""

    async def analyse_expression(
        self, body: JiraExpressionForAnalysis, *, check: str | None = None
    ) -> JiraExpressionsAnalysis:
        """Analyse Jira expression"""
        params = self._client._build_params(**{"check": check})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/expression/analyse",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JiraExpressionsAnalysis.model_validate(resp.json())

    async def evaluate_jsis_jira_expression(
        self, body: JiraExpressionEvaluateRequestBean, *, expand: str | None = None
    ) -> JExpEvaluateJiraExpressionResultBean:
        """Evaluate Jira expression using enhanced search API"""
        params = self._client._build_params(**{"expand": expand})
        resp = await self._client._request(
            "POST",
            "/rest/api/3/expression/evaluate",
            params=params,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )
        return JExpEvaluateJiraExpressionResultBean.model_validate(resp.json())
