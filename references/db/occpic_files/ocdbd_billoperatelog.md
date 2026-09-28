# 单据操作日志-ocdbd_billoperatelog

## 单据操作日志-主表 t_ocdbd_billoperatelog

- **表名称：** 单据操作日志-主表
- **表名：** t_ocdbd_billoperatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillid | 来源单据Id | int8 | 64 |  | √ | 0 | 来源单据Id |
| 3 | foperatedate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fsrcbillentity | 来源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | foperation | 单据业务操作 | varchar | 50 |  | √ | ' ' | 单据业务操作,枚举: delete :删除 exception :异常 |
| 6 | fdatatype | 业务取数规则 | varchar | 10 |  | √ | ' ' | 业务取数规则,枚举: A :预算取数规则 B :返利取数规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_billoperatelog_sid |  | fsrcbillid |
| 2 | pk_ocdbd_billoperatelog |  | fid |
