# 个人自盘表-fa_inventory_backlog

## 个人自盘表-主表 t_fa_inventory_record

- **表名称：** 个人自盘表-主表
- **表名：** t_fa_inventory_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifference | fdifference | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | finventoryuser | finventoryuser | int8 | 64 |  | √ | 0 |  |
| 4 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 5 | fgroupid | 关联盘点表id | int8 | 64 |  | √ | 0 | 关联盘点表id |
| 6 | fismanual | fismanual | bpchar | 1 |  | √ | '0' |  |
| 7 | finventorytime | 盘点日期 | timestamp | 0 |  |  | null | 盘点日期 |
| 8 | finventoryquantity | 盘点数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量 |
| 9 | ficheadusepersonid | ficheadusepersonid | int8 | 64 |  | √ | 0 |  |
| 10 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 11 | fgroupnumber | 盘点编码 | varchar | 30 |  | √ | ' ' | 盘点编码 |
| 12 | fbillstate | 盘点记录状态 | bpchar | 1 |  | √ | '0' | 盘点记录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fheaduserid | fheaduserid | int8 | 64 |  | √ | 0 |  |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbarcode | fbarcode | varchar | 60 |  | √ | ' ' |  |
| 16 | ficstoreplaceid | ficstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 17 | fstoreplaceid | fstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fheadusedeptid | fheadusedeptid | int8 | 64 |  | √ | 0 |  |
| 20 | finventoryway | finventoryway | bpchar | 1 |  | √ | ' ' |  |
| 21 | finventorystate | 盘点状态 | bpchar | 1 |  | √ | 'B' | 盘点状态,枚举: A :已盘 B :未盘 C :已生成差异 |
| 22 | fchangebillid | fchangebillid | int8 | 64 |  | √ | 0 |  |
| 23 | fisnewadd | fisnewadd | bpchar | 1 |  | √ | '0' |  |
| 24 | fisconfirm | fisconfirm | bpchar | 1 |  | √ | '0' |  |
| 25 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 26 | fbookquantity | 资产数量 | numeric | 23 | 10 | √ | 0.0000000000 | 资产数量 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
| 29 | finventorytaskid | 盘点任务 | int8 | 64 |  | √ | 0 | [我的盘点任务 fa_inventory_task](../fa_files/fa_inventory_task.md) |
| 30 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fadheadusedeptid | fadheadusedeptid | int8 | 64 |  | √ | 0 |  |
| 34 | finvresult | finvresult | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 36 | freason | 盘点说明 | varchar | 100 |  | √ | ' ' | 盘点说明 |
| 37 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 38 | fadstoreplaceid | fadstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 39 | ficheadusedeptid | ficheadusedeptid | int8 | 64 |  | √ | 0 |  |
| 40 | finventschemeentryid | 盘点方案 | int8 | 64 |  | √ | 0 | [盘点方案 fa_inventscheme_new](../fa_files/fa_inventscheme_new.md) |
| 41 | finvdifferid | finvdifferid | int8 | 64 |  | √ | 0 |  |
| 42 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 43 | fadheadusepersonid | fadheadusepersonid | int8 | 64 |  | √ | 0 |  |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
