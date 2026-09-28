# 卡片库组织权限-bos_nocode_card_orgauth

## 卡片库组织权限-主表 t_nocode_card_orgauth

- **表名称：** 卡片库组织权限-主表
- **表名：** t_nocode_card_orgauth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardid | 卡片ID | int8 | 64 |  | √ | 0 | 卡片ID |
| 3 | forgid | 被授权组织 | int8 | 64 |  | √ | 0 | 被授权组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_card_orgauth |  | fid |
| 2 | idx_nc_co_cid |  | fcardid |
| 3 | idx_nc_co_oid |  | forgid |
