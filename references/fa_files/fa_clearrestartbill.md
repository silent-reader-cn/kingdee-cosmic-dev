# 清理重启单-fa_clearrestartbill

## 清理重启单-主表 t_fa_clearrsbill

- **表名称：** 清理重启单-主表
- **表名：** t_fa_clearrsbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | frestartdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | freason | 重启原因 | varchar | 255 |  |  | ' ' | 重启原因 |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | frestartperiodid | 重启期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_clearrsbill_pkey |  | fid |
| 2 | idx_fa_clearrsbill_fbillno |  | fbillno |

---

## 清理资产详情分录-子表 t_fa_clearrsbillentry

- **表名称：** 清理资产详情分录-子表
- **表名：** t_fa_clearrsbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddupdepre | 累计折旧（本币） | numeric | 19 | 6 | √ | 0.000000 | 累计折旧（本币） |
| 3 | fnetamount | 资产净额（本币） | numeric | 19 | 6 | √ | 0.000000 | 资产净额（本币） |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fclearid | 清理单id | int8 | 64 |  | √ | 0 | 清理单id |
| 6 | fisclearall | 清理类型标识 | bpchar | 1 |  | √ | '1' | 清理类型标识,枚举: 0 :原值部分清理 1 :完全清理 2 :数量部分清理 |
| 7 | fclearrate | 清理率(清理原值/原值) | numeric | 23 | 10 | √ | 0.0000000000 | 清理率(清理原值/原值) |
| 8 | fdecval | 减值准备（本币） | numeric | 19 | 6 | √ | 0.000000 | 减值准备（本币） |
| 9 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 10 | fcleardate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 11 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |
| 12 | fclearfare | 清理费用（本币） | numeric | 19 | 6 | √ | 0.000000 | 清理费用（本币） |
| 13 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 14 | fclearperiodid | 清理单期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 15 | fclearincome | 清理收入（本币） | numeric | 19 | 6 | √ | 0.000000 | 清理收入（本币） |
| 16 | fassetvalue | 资产原值（本币） | numeric | 19 | 6 | √ | 0.000000 | 资产原值（本币） |
| 17 | frealcardid | 卡片编号 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 18 | fclearqty | 清理数量 | numeric | 23 | 10 | √ | 0.0000000000 | 清理数量 |
| 19 | fpreresidualval | 清理资产残值（本币） | numeric | 19 | 6 | √ | 0.000000 | 清理资产残值（本币） |
| 20 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fclearentryid | 清理分录id | int8 | 64 |  | √ | 0 | 清理分录id |
| 22 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 23 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fnetval | fnetval | numeric | 19 | 6 | √ | 0.000000 |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fassetnumber | 资产编码 | varchar | 100 |  | √ | ' ' | 资产编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clearrsbillentry_fid |  | fid |
| 2 | t_fa_clearrsbillentry_pkey |  | fentryid |
