# 基础资料升级关系-pbd_basedatalink

## 基础资料升级关系-主表 t_pur_basedatalink

- **表名称：** 基础资料升级关系-主表
- **表名：** t_pur_basedatalink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbasedata | 原基础资料 | varchar | 100 |  | √ | ' ' | 原基础资料 |
| 3 | fbasedatatype | 基础资料类型 | varchar | 100 |  | √ | ' ' | 基础资料类型 |
| 4 | fdestbasedata | 目标基础资料 | varchar | 100 |  | √ | ' ' | 目标基础资料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_basedatalink_pkey |  | fid |
| 2 | idx_pur_basedatalink |  | fbasedatatype |
