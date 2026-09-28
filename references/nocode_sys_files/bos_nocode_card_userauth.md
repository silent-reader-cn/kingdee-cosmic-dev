# 卡片库用户权限-bos_nocode_card_userauth

## 卡片库用户权限-主表 t_nocode_card_userauth

- **表名称：** 卡片库用户权限-主表
- **表名：** t_nocode_card_userauth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardid | 卡片ID | int8 | 64 |  | √ | 0 | 卡片ID |
| 3 | fuserid | 被授权用户 | int8 | 64 |  | √ | 0 | 被授权用户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_cu_cid |  | fcardid |
| 2 | pk_nocode_card_userauth |  | fid |
| 3 | idx_nc_cu_uid |  | fuserid |
