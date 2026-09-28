---
title: "操作API请求量数据限制规范"
entityId: "606932884078957056"
category: "动态与公告 / 重要通知"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/606932884078957056?productLineId=29&lang=zh-CN"
createdAt: "2024-08-01 19:34:36"
updatedAt: "2025-03-10 11:05:34"
views: 2971
---

# 操作API请求量数据限制规范

尊敬的用户：

为了保障公有云集群服务的稳定性和性能，我们对API使用规范进行了更新，请您在使用API时遵循以下规范：

1. **查询类操作API**：
  - 默认每次查询不超过2000条数据。
  - 最多查询量不得超过100,000条数据。
2. **保存类操作API**：
  - 默认每次批量保存数据不超过10,000条（含分录）。
  - 最多保存量不得超过100,000条数据。
3. **状态变更类（提交、审核等）操作API**：
  - 默认每次操作不超过2000条数据。
  - 最多操作量不得超过5000条数据。
4. 所有OpenAPI：为保障系统安全和稳定性，API请求参数和返回参数最大不允许超过**30M**。

请您务必遵守上述规范，以免对系统性能和稳定性造成影响。若有任何疑问或需要进一步的技术支持，请随时联系OpenAPI产品团队。

感谢您的理解与配合。

祝使用愉快！
