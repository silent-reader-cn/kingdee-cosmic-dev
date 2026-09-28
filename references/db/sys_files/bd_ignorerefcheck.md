# 基础数据删除引用检查白名单-bd_ignorerefcheck

## 基础数据删除引用检查白名单-主表 t_bd_ignorerefcheck

- **表名称：** 基础数据删除引用检查白名单-主表
- **表名：** t_bd_ignorerefcheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbaseentitynumber | 指定不做引用检查的基础资料 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fignoreall | 本单不做任何基础资料引用检查 | bpchar | 1 |  | √ | '0' | 本单不做任何基础资料引用检查 |
| 4 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 5 | fentitynumber | 白名单单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fenable | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态,枚举: 0 :禁用 1 :启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_ignorerefcheck |  | fid |
| 2 | idx_bd_ignorerefcheck_bill |  | fentitynumber |
