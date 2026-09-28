# 清理单基础资料-fa_clearbill_base

## 清理单基础资料-主表 t_fa_clrbill

- **表名称：** 清理单基础资料-主表
- **表名：** t_fa_clrbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fclearperiodid | fclearperiodid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 8 | freason | 清理原因 | varchar | 255 |  |  | ' ' | 清理原因 |
| 9 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fchangemodeid | 减少方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 14 | fcleardate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 17 | fclearsource | 清理来源 | varchar | 50 |  | √ | 'APPLY' | 清理来源,枚举: ADDNEW :新增 APPLY :清理申请 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 INVENTORY_LOSS :盘亏 LEASE_TERMINATION :租赁终止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clrbil_fbillno |  | fbillno |
| 2 | idx_fa_clrbil_orgid |  | forgid,fcleardate |
| 3 | t_fa_clrbill_pkey |  | fid |
