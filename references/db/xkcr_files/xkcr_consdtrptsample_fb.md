# 附表合并报表模板-xkcr_consdtrptsample_fb

## 主表项目-多选基础资料表 t_xkrpt_rpt_rptitem

- **表名称：** 主表项目-多选基础资料表
- **表名：** t_xkrpt_rpt_rptitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frptid | frptid | varchar | 36 |  | √ | ' ' |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_rpt_rptitem_rptid |  | frptid |
| 2 | pk_t_xkrpt_rpt_rptitem |  | fpkid |

---

## 附表合并报表模板-主表 t_xkrpt_rpt

- **表名称：** 附表合并报表模板-主表
- **表名：** t_xkrpt_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [附表合并报表模板分组 xkcr_congroup_fb](../xkcr_files/xkcr_congroup_fb.md) |
| 2 | fwiserpt | fwiserpt | text | 0 |  |  | null |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceid | 源报表Id | varchar | 36 |  | √ | ' ' | 源报表Id |
| 5 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 6 | fdocumentstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisautocreate | fisautocreate | bpchar | 1 |  | √ | '0' |  |
| 9 | fverifyresult | fverifyresult | varchar | 255 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | frptstyletype | 样式类型 | varchar | 10 |  | √ | ' ' | 样式类型,枚举: 1 :固定样式 2 :动态样式 |
| 13 | fday | 日期 | timestamp | 0 |  |  | null | 日期 |
| 14 | ftranssourceid | 迁移源模版Id | varchar | 36 |  | √ | ' ' | 迁移源模版Id |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 17 | fverifydate | fverifydate | timestamp | 0 |  |  | null |  |
| 18 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 19 | frptstyle | 报表Style内容 | text | 0 |  |  | null | 报表Style内容 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | frptid | frptid | varchar | 36 |  | √ | ' ' | id |
| 24 | facctsystemid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fissample | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | farchivestatus | farchivestatus | bpchar | 1 |  | √ | '0' |  |
| 29 | fisautoshare | fisautoshare | bpchar | 1 |  | √ | '0' |  |
| 30 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 31 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 32 | fkeyword | fkeyword | varchar | 255 |  | √ | ' ' |  |
| 33 | fsampleid | fsampleid | varchar | 36 |  | √ | ' ' |  |
| 34 | frptmodel | 报表model内容 | text | 0 |  |  | null | 报表model内容 |
| 35 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 36 | fperiod | 期 | int8 | 64 |  | √ | 0 | 期 |
| 37 | fcreatestyle | 创建方式 | varchar | 10 |  | √ | ' ' | 创建方式,枚举: 0 :标准 1 :舍位平衡 2 :共享 3 :共享(未检查) 8 :外币折算 4 :自动生成 5 :分发 |
| 38 | fismain | 是否主表 | bpchar | 1 |  | √ | '0' | 是否主表 |
| 39 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 41 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 42 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 80 :附表汇总报表模板 90 :附表合并报表模板 |
| 44 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 45 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 46 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fverifystatus | fverifystatus | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | frptid | frptid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rpt |  | frptid |
| 2 | idx_xkrpt_rpt_fnumber |  | fnumber |

---

## 单据体-子表 t_xkcr_distribute

- **表名称：** 单据体-子表
- **表名：** t_xkcr_distribute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | frptid | frptid | varchar | 36 |  | √ | ' ' |  |
| 3 | facctsystemid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnewsampleid | 新模板id | varchar | 36 |  | √ | ' ' | 新模板id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 8 | fallowedit | 允许修改 | bpchar | 1 |  | √ | ' ' | 允许修改 |
| 9 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 10 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_distribute |  | frptid |
| 2 | pk_xkcr_distribute |  | fid |

---

## 单据体-子表 t_xkrpt_sheet

- **表名称：** 单据体-子表
- **表名：** t_xkrpt_sheet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsheetcurrunit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 2 | frptid | frptid | varchar | 36 |  | √ | ' ' |  |
| 3 | fsheetsampleid | 表页模板ID | varchar | 36 |  | √ | ' ' | 表页模板ID |
| 4 | fsheetname | 表页名称 | varchar | 255 |  | √ | ' ' | 表页名称 |
| 5 | fsheetsamplesheetid | 报表模板表页ID | varchar | 36 |  | √ | ' ' | 报表模板表页ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frptcontent | 表页内容 | text | 0 |  |  | null | 表页内容 |
| 8 | fsheetid | fsheetid | varchar | 36 |  | √ | ' ' | id |
| 9 | fsheettype | 表页类型 | varchar | 10 |  | √ | ' ' | 表页类型 |
| 10 | fsheetday | 报表日期 | timestamp | 0 |  |  | null | 报表日期 |
| 11 | fsheetyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 12 | fsheetperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 13 | fsheetcycleid | 表页周期类型 | varchar | 10 |  | √ | ' ' | 表页周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 14 | fsheetcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fsheetid | fsheetid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_sheet_frptid |  | frptid |
| 2 | pk_xkrpt_sheet |  | fsheetid |

---

## 附表合并报表模板-多语言表 t_xkrpt_rpt_l

- **表名称：** 附表合并报表模板-多语言表
- **表名：** t_xkrpt_rpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | frptid | frptid | varchar | 36 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rpt_l |  | fpkid |
| 2 | idx_xkrpt_rpt_l_frptid |  | frptid |
