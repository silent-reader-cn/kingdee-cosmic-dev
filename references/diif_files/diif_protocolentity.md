# 协议信息实体-diif_protocolentity

## 协议信息实体-主表 t_diif_protocolentity

- **表名称：** 协议信息实体-主表
- **表名：** t_diif_protocolentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsignerid | 签署人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fagreeprotocol | 同意协议 | bpchar | 1 |  | √ | '0' | 同意协议 |
| 5 | fsigndate | 签署日期 | timestamp | 0 |  |  | null | 签署日期 |
| 6 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_protocolentity |  | fid |
| 2 | idx_diif_protocolentity_signer |  | fsignerid |
