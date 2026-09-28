# 清理申请单-fa_clearapplybill

## 清理资产详情分录-子表 t_fa_clrapplybillentry

- **表名称：** 清理资产详情分录-子表
- **表名：** t_fa_clrapplybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclearqty | 清理数量 | numeric | 19 | 6 | √ | 0.000000 | 清理数量 |
| 3 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clrappbilent_fseq |  | fseq |
| 2 | t_fa_clrapplybillentry_pkey |  | fentryid |

---

## 清理申请单-主表 t_fa_clrapplybill

- **表名称：** 清理申请单-主表
- **表名：** t_fa_clrapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 7 | fhandlerid | 经办人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | freason | 清理原因 | varchar | 255 |  |  | ' ' | 清理原因 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fchangemodeid | 减少方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 12 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcleardate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 15 | fbillno | 清理单号 | varchar | 30 |  | √ | ' ' | 清理单号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_clrapplybill_pkey |  | fid |
| 2 | idx_fa_clrappbill_fbillno |  | fbillno |
