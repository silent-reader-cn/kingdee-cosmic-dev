# 收款条件到期日设置-bd_recconditionset

## 收款条件到期日设置-主表 t_bd_recconditionset

- **表名称：** 收款条件到期日设置-主表
- **表名：** t_bd_recconditionset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fseqnum | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 3 | fkey | 唯一标识 | varchar | 5 |  | √ | ' ' | 唯一标识 |
| 4 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 5 | fenable | 使用状态 | varchar | 5 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fdatafield | 到期日来源字段 | varchar | 255 |  | √ | ' ' | 到期日来源字段,枚举: |
| 7 | fbilltype | 到期日来源单据 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_uq_rec_key |  | fkey |
| 2 | pk_t_bd_recconditionset |  | fid |
