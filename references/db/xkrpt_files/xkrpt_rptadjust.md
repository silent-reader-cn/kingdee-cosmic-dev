# 报表调整分录-xkrpt_rptadjust

## 报表调整分录-多语言表 t_xkcr_rptadjust_l

- **表名称：** 报表调整分录-多语言表
- **表名：** t_xkcr_rptadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_rptadjust_l |  | fid,flocaleid |
| 2 | pk_t_xkcr_rptadjust_l |  | fpkid |

---

## 报表调整分录-主表 t_xkcr_rptadjust

- **表名称：** 报表调整分录-主表
- **表名：** t_xkcr_rptadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdebittotal | 借方调整总额 | numeric | 23 | 10 | √ | 0 | 借方调整总额 |
| 4 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 5 | fmaintype | fmaintype | bpchar | 1 |  | √ | '0' |  |
| 6 | fisperpetuate | fisperpetuate | bpchar | 1 |  | √ | '0' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | foriginid | foriginid | int8 | 64 |  | √ | 0 |  |
| 9 | fbuildtype | 创建方式 | bpchar | 1 |  | √ | ' ' | 创建方式,枚举: 1 :手工录入 2 :自动生成 3 :导入 4 :模版生成 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcompanytype | fcompanytype | varchar | 50 |  | √ | ' ' |  |
| 12 | fcompanyid2 | fcompanyid2 | int8 | 64 |  | √ | 0 |  |
| 13 | fdate | fdate | timestamp | 0 |  |  | null |  |
| 14 | fbillno | 分录编码 | varchar | 30 |  | √ | ' ' | 分录编码 |
| 15 | fcredittotal | 贷方调整总额 | numeric | 23 | 10 | √ | 0 | 贷方调整总额 |
| 16 | ftranstypeid | ftranstypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | frptid | 报表 | varchar | 36 |  | √ | ' ' | [报表 xkrpt_report](../xkrpt_files/xkrpt_report.md) |
| 20 | ftemplateid | 调整分录模板 | int8 | 64 |  | √ | 0 | [报表调整分录模板 xkrpt_adjusttemplate](../xkrpt_files/xkrpt_adjusttemplate.md) |
| 21 | fdimvaluekey | fdimvaluekey | varchar | 2000 |  |  | null |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | facctsystemid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | felimtypeid | felimtypeid | int8 | 64 |  | √ | 0 |  |
| 27 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 28 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 29 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 30 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 31 | fcycleid | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 32 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 33 | fcurrencyid | 调整币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_rptadjust_yearperiod |  | fyear,fperiod |
| 2 | idx_xkcr_rptadjust_rptid |  | frptid |
| 3 | idx_xkcr_rptadjust_createdate |  | fcreatetime |
| 4 | idx_xkcr_rptadjust_tmpid |  | fcompanyid |
| 5 | idx_xkcr_rptadjust_billno |  | fbillno |
| 6 | pk_t_xkcr_rptadjust |  | fid |

---

## 分录-多语言表 t_xkcr_rptadjustentry_l

- **表名称：** 分录-多语言表
- **表名：** t_xkcr_rptadjustentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_rptadjustentry_l |  | fentryid,flocaleid |
| 2 | pk_t_xkcr_rptadjustentry_l |  | fpkid |

---

## 分录-子表 t_xkcr_rptadjustentry

- **表名称：** 分录-子表
- **表名：** t_xkcr_rptadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forigin | forigin | varchar | 50 |  | √ | ' ' |  |
| 3 | frptitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 4 | fdebit | 借方调整 | numeric | 23 | 10 | √ | 0 | 借方调整 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetaildim | 维度值 | varchar | 2000 |  | √ | ' ' | 维度值 |
| 7 | frptitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 8 | fislinkage | fislinkage | bpchar | 1 |  | √ | '0' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 11 | fcredit | 贷方调整 | numeric | 23 | 10 | √ | 0 | 贷方调整 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_rptadjustentry_fid |  | fid |
| 2 | pk_t_xkcr_rptadjustentry |  | fentryid |
