# 自动关闭信用的记录-ccm_autocloseinfo

## 自动关闭信用的记录-主表 t_ccm_autocloseinfo

- **表名称：** 自动关闭信用的记录-主表
- **表名：** t_ccm_autocloseinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 5 | fentitykey | 单据标识 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_autocloseinfo |  | fid |
| 2 | idx_ccm_atclsinfo_ety |  | fbillentryid |
