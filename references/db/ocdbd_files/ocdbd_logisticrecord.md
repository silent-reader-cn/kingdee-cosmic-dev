# 物流记录单-ocdbd_logisticrecord

## 物流记录单-主表 t_ocdbd_logisticrecord

- **表名称：** 物流记录单-主表
- **表名：** t_ocdbd_logisticrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 收、寄件电话号码 | varchar | 80 |  | √ | ' ' | 收、寄件电话号码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fphone_enp | fphone_enp | text | 0 |  |  | null |  |
| 5 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fsrcbillid | 来源单据主键 | int8 | 64 |  | √ | 0 | 来源单据主键 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flogisticcompid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 bd_logisticcomp](../sbd_files/bd_logisticcomp.md) |
| 10 | fsourcebilltypeid | 生成物流记录的来源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fdeliveryid | 生成物流记录的来源单据ID | int8 | 64 |  | √ | 0 | 生成物流记录的来源单据ID |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | flogisticno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 16 | fsrcbillentity | 来源单据类型 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_logisticrecord_no |  | fbillno |
| 2 | pk_ocdbd_logisticrecord |  | fid |
