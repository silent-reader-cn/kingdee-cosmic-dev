# 废弃-fa_consignation_record

## 废弃-主表 t_fa_consignation_record

- **表名称：** 废弃-主表
- **表名：** t_fa_consignation_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifference | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 5 | finventorytaskid | 盘点任务 | int8 | 64 |  | √ | 0 | 我的盘点任务 fa_inventory_task |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fconsignorid | 委托人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillstate | fbillstate | bpchar | 1 |  | √ | '1' |  |
| 11 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | finventschemeentryid | 盘点方案 | int8 | 64 |  | √ | 0 | 盘点方案 fa_inventscheme_new |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fconsigneeid | 被委托人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fnumber | 资产编码 | varchar | 50 |  | √ | ' ' | 资产编码 |
| 17 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_consignation_record |  | fid |
| 2 | idx_fa_consignation_record |  | finventschemeentryid,finventorytaskid |
