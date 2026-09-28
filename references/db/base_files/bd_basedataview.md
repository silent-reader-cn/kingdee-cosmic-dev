# 基础数据视图关系-bd_basedataview

## 基础数据视图关系-主表 t_bd_basedataview

- **表名称：** 基础数据视图关系-主表
- **表名：** t_bd_basedataview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbasedataid | 基础数据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 5 | fctrlview | 管控视图 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_basedataview_basedata |  | fbasedataid |
| 2 | t_bd_basedataview_pkey |  | fid |
