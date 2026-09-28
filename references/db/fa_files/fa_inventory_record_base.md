# 盘点记录基础资料-fa_inventory_record_base

## 盘点记录基础资料-主表 t_fa_inventory_record

- **表名称：** 盘点记录基础资料-主表
- **表名：** t_fa_inventory_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifference | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |
| 3 | finventoryuser | 盘点人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 5 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 6 | finventorytime | 盘点日期 | timestamp | 0 |  |  | null | 盘点日期 |
| 7 | finventoryquantity | 盘点数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fgroupnumber | fgroupnumber | varchar | 30 |  | √ | ' ' |  |
| 10 | fbillstate | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :待审核 C :已审核 |
| 11 | fheaduserid | fheaduserid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbarcode | 条形码 | varchar | 60 |  | √ | ' ' | 条形码 |
| 14 | fstoreplaceid | fstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fheadusedeptid | fheadusedeptid | int8 | 64 |  | √ | 0 |  |
| 17 | finventoryway | 盘点方式 | bpchar | 1 |  | √ | ' ' | 盘点方式,枚举: A :人人盘点 B :手工盘点 |
| 18 | finventorystate | 状态 | bpchar | 1 |  | √ | 'B' | 状态,枚举: A :已盘 B :未盘 |
| 19 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 20 | fbookquantity | 账面数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账面数量 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
| 23 | finventorytaskid | 盘点任务 | int8 | 64 |  | √ | 0 | 我的盘点任务 fa_inventory_task |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | freason | 盘亏原因 | varchar | 100 |  | √ | ' ' | 盘亏原因 |
| 29 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 30 | finventschemeentryid | 盘点方案 | int8 | 64 |  | √ | 0 | 盘点方案 fa_inventscheme_new |
| 31 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_inventory_record_pkey |  | fid |
| 2 | idx_fa_inventory_record |  | finventschemeentryid,finventorytaskid |
| 3 | idx_fa_inventory_red_fgid |  | fgroupid |
