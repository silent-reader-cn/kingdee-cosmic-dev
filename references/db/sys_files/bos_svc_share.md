# 分享-bos_svc_share

## 分享-主表 t_bas_share_url

- **表名称：** 分享-主表
- **表名：** t_bas_share_url

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | expiretime | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 3 | sharecontext | 详情 | varchar | 255 |  | √ | ' ' | 详情 |
| 4 | state | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :正常 |
| 5 | sharetype | 分享类型 | bpchar | 1 |  | √ | '0' | 分享类型,枚举: 0 :0 |
| 6 | sharecontext_tag | 详情_详情 | text | 0 |  |  | ' ' | 详情_详情 |
| 7 | url | 分享链接 | varchar | 500 |  | √ | ' ' | 分享链接 |
| 8 | sharetime | 分享时间 | timestamp | 0 |  |  | null | 分享时间 |
| 9 | ftextfield | 分享名称 | varchar | 50 |  | √ | ' ' | 分享名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_share_url |  | fid |
| 2 | idx_bas_index_sharetype |  | sharetype |
