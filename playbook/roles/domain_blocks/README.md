# Block domains

We consider the `domain_blocks.csv` file at the root of this repo to be the canonical list. This role turns that list into a YAML file, suitable for Ansible, then hits the `/api/v1/admin/domain_blocks` for each domain. This operation is idempotent - if a domain is already blocked the API returns a `422 Unprocessable Entity`, which we just absorb.

---

API keys required:

|Secret name|scope|
|---|---|
|MASTODON_READ_ONLY_TOKEN|admin:read|
|MASTODON_DOMAIN_BLOCK_TOKEN|admin:write:domain_blocks|
