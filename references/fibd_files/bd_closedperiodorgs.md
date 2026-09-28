# 月结组织-bd_closedperiodorgs

## 月结组织-主表 t_bd_closedperiodorgs

- **表名称：** 月结组织-主表
- **表名：** t_bd_closedperiodorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forgtype | 组织职能 | varchar | 30 |  | √ | '0' | 组织职能 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_closedperiodorgs |  | forgid,forgtype,fuserid |
| 2 | t_bd_closedperiodorgs_pkey |  | fid |
