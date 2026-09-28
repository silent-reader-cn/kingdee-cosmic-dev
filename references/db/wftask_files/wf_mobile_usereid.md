# 单租户配置信息-wf_mobile_usereid

## 单租户配置信息-主表 t_wftask_eiduser

- **表名称：** 单租户配置信息-主表
- **表名：** t_wftask_eiduser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建时间1 | timestamp | 0 |  |  | null | 创建时间1 |
| 3 | fmodifydate | 修改时间1 | timestamp | 0 |  |  | null | 修改时间1 |
| 4 | fcreaterid | 创建人1 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcomname | 企业名称 | varchar | 100 |  | √ | ' ' | 企业名称 |
| 6 | fuserid | 企业用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wftask_eiduser |  | fuserid |
| 2 | t_wftask_eiduser_pkey |  | fid |
