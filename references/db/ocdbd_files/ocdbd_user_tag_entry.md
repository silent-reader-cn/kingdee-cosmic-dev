# 会员标签单据体-ocdbd_user_tag_entry

## 会员标签单据体-主表 t_ocdbd_user_tag_entry

- **表名称：** 会员标签单据体-主表
- **表名：** t_ocdbd_user_tag_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 会员用户 | int8 | 64 |  | √ | 0 | [顾客信息 ocdbd_user](../ocdbd_files/ocdbd_user.md) |
| 2 | ftagid | 标签 | int8 | 64 |  | √ | 0 | [标签定义 ocdbd_user_tag](../ocdbd_files/ocdbd_user_tag.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_tag_entry |  | fentryid |
| 2 | idx_ocdbd_usertagentry_ct |  | fcreatetime |
| 3 | idx_ocdbd_usertagentry_fid |  | fid |
| 4 | idx_ocdbd_usertagentry_tid |  | ftagid |
