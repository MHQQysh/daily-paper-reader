from __future__ import annotations

import os
import re
from datetime import datetime, timezone
from typing import Any


RUN_DATE_ENV = "DPR_RUN_DATE"
RUN_ID_ENV = "DPR_RUN_ID"
RUN_LABEL_ENV = "DPR_RUN_LABEL"
RUN_STARTED_AT_ENV = "DPR_RUN_STARTED_AT"
PROFILE_TAG_ENV = "DPR_FILTER_PROFILE_TAG"

DATE_TOKEN_RE = re.compile(r"^\d{8}$")
RANGE_TOKEN_RE = re.compile(r"^(\d{8})-(\d{8})$")
RUN_META_FILENAME = "run.meta.json"


def get_run_date_token(now: datetime | None = None) -> str:
    token = str(os.getenv(RUN_DATE_ENV) or "").strip()
    if token:
        return token
    anchor = now or datetime.now(timezone.utc)
    if anchor.tzinfo is None:
        anchor = anchor.replace(tzinfo=timezone.utc)
    return anchor.astimezone(timezone.utc).strftime("%Y%m%d")


def get_run_id(default: str | None = None, now: datetime | None = None) -> str:
    token = str(os.getenv(RUN_ID_ENV) or "").strip()
    if token:
        return token
    return str(default or "").strip() or get_run_date_token(now=now)


def get_run_label(default: str | None = None) -> str:
    token = str(os.getenv(RUN_LABEL_ENV) or "").strip()
    if token:
        return token
    return str(default or "").strip()


def get_profile_tag(default: str | None = None) -> str:
    token = str(os.getenv(PROFILE_TAG_ENV) or "").strip()
    if token:
        return token
    return str(default or "").strip()


def is_legacy_date_token(token: Any) -> bool:
    text = str(token or "").strip()
    return bool(DATE_TOKEN_RE.fullmatch(text) or RANGE_TOKEN_RE.fullmatch(text))


def format_run_date_token(token: Any) -> str:
    text = str(token or "").strip()
    matched = RANGE_TOKEN_RE.fullmatch(text)
    if matched:
        start_text, end_text = matched.groups()
        return (
            f"{start_text[:4]}-{start_text[4:6]}-{start_text[6:]} ~ "
            f"{end_text[:4]}-{end_text[4:6]}-{end_text[6:]}"
        )
    if DATE_TOKEN_RE.fullmatch(text):
        return f"{text[:4]}-{text[4:6]}-{text[6:]}"
    return text


def sanitize_run_component(text: Any, fallback: str = "all") -> str:
    raw = str(text or "").strip()
    if not raw:
        return fallback
    raw = re.sub(r'[<>:"/\\|?*]+', "-", raw)
    raw = re.sub(r"\s+", "-", raw)
    raw = re.sub(r"-{2,}", "-", raw)
    raw = raw.strip(" -._")
    return raw or fallback


def build_run_id(profile_tag: str = "", now: datetime | None = None) -> str:
    anchor = now or datetime.now().astimezone()
    if anchor.tzinfo is None:
        anchor = anchor.replace(tzinfo=timezone.utc)
    prefix = sanitize_run_component(profile_tag or "all", fallback="all")
    timestamp = anchor.strftime("%Y%m%d-%H%M%S-%f")
    return f"{prefix}__{timestamp}"


def build_run_label(
    run_date_token: str,
    profile_tag: str = "",
    now: datetime | None = None,
    business_label: str | None = None,
) -> str:
    anchor = now or datetime.now().astimezone()
    if anchor.tzinfo is None:
        anchor = anchor.replace(tzinfo=timezone.utc)
    run_time_text = anchor.strftime("%Y-%m-%d %H:%M:%S")
    safe_profile = str(profile_tag or "").strip()
    safe_business_label = str(business_label or "").strip() or format_run_date_token(run_date_token)

    parts = []
    if safe_profile:
        parts.append(safe_profile)
    if safe_business_label:
        parts.append(safe_business_label)
    parts.append(run_time_text)
    return " · ".join(part for part in parts if part)
