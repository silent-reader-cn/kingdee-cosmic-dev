# 维护打印模板-bas_manageprinttpl

## 维护打印模板-主表 t_bas_printtplinfo

- **表名称：** 维护打印模板-主表
- **表名：** t_bas_printtplinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillformid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fname | fname | varchar | 256 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 6 | fprinttplid | 打印模板 | varchar | 36 |  |  | ' ' | [打印模板 bos_printtemplate](../mdl_files/bos_printtemplate.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreateorg | 创建组织 | int8 | 64 |  | √ | '-1' | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '5' | 控制策略,枚举: 2 :自由分配 5 :全局共享 7 :私有 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 模版类型 | bpchar | 1 |  | √ | 'A' | 模版类型,枚举: A :旧模版 B :新模版 |
| 13 | fenable | 模板状态 | varchar | 36 |  | √ | '1' | 模板状态,枚举: 0 :禁用 1 :启用 |
| 14 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 15 | fisdefault | 默认模板 | bpchar | 1 |  |  | null | 默认模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_printtplinfo_pkey |  | fid |
| 2 | idx_bas_printtplinfo_n |  | fnumber |
| 3 | idx_bas_printtplinfo |  | fbillformid |
