# 报表模板-xkrpt_rptsample

## 报表模板-主表 t_xkrpt_rpt

- **表名称：** 报表模板-主表
- **表名：** t_xkrpt_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [报表模板分组 xkrpt_basegroup](../xkrpt_files/xkrpt_basegroup.md) |
| 2 | fwiserpt | fwiserpt | text | 0 |  |  | null |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceid | 源报表Id | varchar | 36 |  | √ | ' ' | 源报表Id |
| 5 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 6 | fdocumentstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisautocreate | 是否自动生成 | bpchar | 1 |  | √ | '0' | 是否自动生成 |
| 9 | fverifyresult | 报表检查结果 | varchar | 255 |  | √ | ' ' | 报表检查结果,枚举: 0 :未检查 1 :检查不通过 2 :检查通过 3 :无勾稽关系 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | frptstyletype | 样式类型 | varchar | 10 |  | √ | ' ' | 样式类型,枚举: 1 :固定样式 2 :动态样式 |
| 13 | fday | 日期 | timestamp | 0 |  |  | null | 日期 |
| 14 | ftranssourceid | ftranssourceid | varchar | 36 |  | √ | ' ' |  |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 17 | fverifydate | 报表检查日期 | timestamp | 0 |  |  | null | 报表检查日期 |
| 18 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
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
| 29 | fisautoshare | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 30 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 31 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 32 | fkeyword | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |
| 33 | fsampleid | 报表模板 | varchar | 36 |  | √ | ' ' | 报表模板 |
| 34 | frptmodel | 报表model内容 | text | 0 |  |  | null | 报表model内容 |
| 35 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 36 | fperiod | 期 | int8 | 64 |  | √ | 0 | 期 |
| 37 | fcreatestyle | 创建方式 | varchar | 10 |  | √ | ' ' | 创建方式,枚举: 0 :标准 1 :舍位平衡 2 :共享 3 :共享(未检查) 8 :外币折算 4 :自动生成 5 :分发 |
| 38 | fismain | 是否主表 | bpchar | 1 |  | √ | '0' | 是否主表 |
| 39 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 41 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 42 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 3 :报表模板 10 :个别报表模板 30 :抵销表模板 70 :附表个别报表模板 |
| 44 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 45 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 46 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fverifystatus | 保存时检查审核 | bpchar | 1 |  | √ | '0' | 保存时检查审核 |

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

## 报表模板-多语言表 t_xkrpt_rpt_l

- **表名称：** 报表模板-多语言表
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
