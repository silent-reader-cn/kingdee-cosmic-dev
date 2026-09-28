# 租户隐私协议签署状态-gai_tenant_agreement

## 租户隐私协议签署状态-主表 t_gai_tenant_agreement

- **表名称：** 租户隐私协议签署状态-主表
- **表名：** t_gai_tenant_agreement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisagree | 是否签署 | bpchar | 1 |  |  | '0' | 是否签署 |
| 3 | fagreetimestamp | 签署时间戳 | int8 | 64 |  | √ | 0 | 签署时间戳 |
| 4 | ftenantid | 租户id | varchar | 50 |  |  | ' ' | 租户id |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fagreetime | 签署时间 | timestamp | 0 |  |  | null | 签署时间 |
| 7 | fversion | 版本 | varchar | 255 |  |  | null | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_tenant_agreement |  | fuserid |
| 2 | pk_t_gai_tenant_agreement |  | fid |
