# 折算过程-xkrpt_transtation_track

## 折算过程-主表 t_xkrpt_trans_track

- **表名称：** 折算过程-主表
- **表名：** t_xkrpt_trans_track

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | ftargetcurrency | 目标币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | frptitem | 报表项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsrccurrency | 原币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 11 | fsrcrpt | 原报表 | varchar | 36 |  | √ | ' ' | 原报表 |
| 12 | frptdimension | 维度信息 | text | 0 |  |  | null | 维度信息 |
| 13 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 14 | ftargetrpt | 目标报表 | varchar | 36 |  | √ | ' ' | 目标报表 |
| 15 | ftransmethod | 折算方法 | int8 | 64 |  | √ | 0 | [外币折算方法 xkrpt_translation_method](../xkrpt_files/xkrpt_translation_method.md) |
| 16 | fsrcitemdata | 源报表项目数据 | int8 | 64 |  | √ | 0 | [项目数据 xkbd_rptitemdata](../fibd_files/xkbd_rptitemdata.md) |
| 17 | ftransscheme | 折算方案 | int8 | 64 |  | √ | 0 | [折算方案 xkrpt_currencyscheme](../xkrpt_files/xkrpt_currencyscheme.md) |
| 18 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_trans_track |  | fid |
| 2 | idx_t_xkrpt_trans_track_rptid |  | frptitem,fitemdatatype,fsrcrpt |

---

## 单据体-子表 t_xkrpt_trans_track_entry

- **表名称：** 单据体-子表
- **表名：** t_xkrpt_trans_track_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | ftargetamount | 折算后金额 | numeric | 23 | 10 | √ | 0 | 折算后金额 |
| 4 | frate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcamount | 折算前金额 | numeric | 23 | 10 | √ | 0 | 折算前金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkrpt_trans_track_efid |  | fid |
| 2 | pk_t_xkrpt_trans_track_entry |  | fentryid |
