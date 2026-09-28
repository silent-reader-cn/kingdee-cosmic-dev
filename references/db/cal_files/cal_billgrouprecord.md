# 成组关系记录-cal_billgrouprecord

## 成组关系记录-主表 t_cal_billgrouprecord

- **表名称：** 成组关系记录-主表
- **表名：** t_cal_billgrouprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcdate | 来源单据业务日期 | timestamp | 0 |  |  | null | 来源单据业务日期 |
| 3 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 5 | fdestbillentryid | 目标单据分录ID | int8 | 64 |  | √ | 0 | 目标单据分录ID |
| 6 | fcreatedatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdestdate | 目标单据业务日期 | timestamp | 0 |  |  | null | 目标单据业务日期 |
| 8 | fislastentry | 是否全部结转 | bpchar | 1 |  | √ | '0' | 是否全部结转 |
| 9 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 10 | fsrcbillqty | 来源单据分录数量 | numeric | 23 | 10 | √ | 0.0000000000 | 来源单据分录数量 |
| 11 | fdestbillno | 目标单据编号 | varchar | 80 |  | √ | ' ' | 目标单据编号 |
| 12 | fdestbillid | 目标单据ID | int8 | 64 |  | √ | 0 | 目标单据ID |
| 13 | fsrcmaterialid | 来源单据物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fdestbillqty | 目标单据分录数量 | numeric | 23 | 10 | √ | 0.0000000000 | 目标单据分录数量 |
| 15 | fgroupsettingid | 来源成组配置 | int8 | 64 |  | √ | 0 | [成组关系配置 cal_billgroupsetting](../cal_files/cal_billgroupsetting.md) |
| 16 | fdestmaterialid | 目标单据物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 17 | fdestownerid | 目标单据货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fjoinedqty | 参与成组数量 | numeric | 23 | 10 | √ | 0.0000000000 | 参与成组数量 |
| 19 | fisloop | 是否循环 | bpchar | 1 |  | √ | '0' | 是否循环 |
| 20 | fsrcownerid | 来源单据货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fgroupnum | 组别 | int8 | 64 |  | √ | 0 | 组别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_billgrouprecord_src |  | fsrcbillid |
| 2 | idx_cal_billgrouprecord_dest |  | fdestbillid |
| 3 | t_cal_billgrouprecord_pkey |  | fid |
