# 自动合并方案-xkcr_smart_merge_plan

## 合并报表生成范围-子表 t_xkcr_sm_cr_entry

- **表名称：** 合并报表生成范围-子表
- **表名：** t_xkcr_sm_cr_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrycycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 3 | fsample | 报表模板 | varchar | 36 |  | √ | ' ' | [合并报表模板（分发后） xkcr_consolidsample_dised](../xkcr_files/xkcr_consolidsample_dised.md) |
| 4 | frptadjust | 报表调整分录 | bpchar | 1 |  | √ | '0' | 报表调整分录 |
| 5 | facctsystem | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 6 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_sm_cr_entry |  | fentryid |
| 2 | idx_xkcr_sm_cr_entry_fid |  | fid |

---

## 折算方案-多选基础资料表 t_xkcr_sm_cur_schemes

- **表名称：** 折算方案-多选基础资料表
- **表名：** t_xkcr_sm_cur_schemes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [折算方案 xkrpt_currencyscheme](../xkrpt_files/xkrpt_currencyscheme.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_sm_cur_schemes |  | fpkid |
| 2 | idx_xkcr_sm_cur_sch_fentryid |  | fentryid |

---

## 工作底稿生成顺序-子表 t_xkcr_sm_work_seqentry

- **表名称：** 工作底稿生成顺序-子表
- **表名：** t_xkcr_sm_work_seqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsamplenumber | 报表模板编码 | varchar | 30 |  | √ | ' ' | 报表模板编码 |
| 3 | fsamplename | 报表模板名称 | varchar | 255 |  | √ | ' ' | 报表模板名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_sm_work_seqentry |  | fentryid |
| 2 | idx_xkcr_sm_work_seqentry_fid |  | fid |

---

## 个别模板编码-子表 t_xkcr_sm_singlenum_entry

- **表名称：** 个别模板编码-子表
- **表名：** t_xkcr_sm_singlenum_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fscopesamplename | 报表模板名称 | varchar | 255 |  | √ | ' ' | 报表模板名称 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fscopesamplenumber | 报表模板编码 | varchar | 30 |  | √ | ' ' | 报表模板编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_sm_singlenum_entry |  | fentryid |
| 2 | idx_xkcr_sm_snum_entry_fid |  | fid |

---

## 个别报表生成顺序-子表 t_xkcr_sm_single_seqentry

- **表名称：** 个别报表生成顺序-子表
- **表名：** t_xkcr_sm_single_seqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsamplenumber | 报表模板编码 | varchar | 30 |  | √ | ' ' | 报表模板编码 |
| 3 | fsamplename | 报表模板名称 | varchar | 255 |  | √ | ' ' | 报表模板名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_sm_single_seqentry |  | fentryid |
| 2 | idx_xkcr_sm_sin_seqentry_fid |  | fid |

---

## 个别报表生成范围-子表 t_xkcr_sm_single_entry

- **表名称：** 个别报表生成范围-子表
- **表名：** t_xkcr_sm_single_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensionfilter | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 3 | facctsystem | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 4 | facctorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpolicy | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 8 | fisfilldimension | 维度填充 | varchar | 1 |  | √ | ' ' | 维度填充,枚举: 2 :覆盖填充 3 :追加填充 |
| 9 | fentrycycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 10 | fsample | 报表模板 | varchar | 36 |  | √ | ' ' | [报表模板 xkrpt_rptsample](../xkrpt_files/xkrpt_rptsample.md) |
| 11 | frptadjust | 报表调整分录 | bpchar | 1 |  | √ | '0' | 报表调整分录 |
| 12 | fdimenfilterdetail_tag | 维度过滤值_详情 | text | 0 |  |  | null | 维度过滤值_详情 |
| 13 | fdimenfilterdetail | 维度过滤值 | varchar | 255 |  | √ | ' ' | 维度过滤值 |
| 14 | fiscompre | 综合本位币 | bpchar | 1 |  | √ | '1' | 综合本位币 |
| 15 | fisadjust | 报表调整 | varchar | 1 |  | √ | '0' | 报表调整 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | facctbook | 取数账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 18 | funit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_sm_single_entry_fid |  | fid |
| 2 | pk_xkcr_sm_single_entry |  | fentryid |

---

## 合并报表生成顺序-子表 t_xkcr_sm_cr_seqentry

- **表名称：** 合并报表生成顺序-子表
- **表名：** t_xkcr_sm_cr_seqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsamplenumber | 报表模板编码 | varchar | 30 |  | √ | ' ' | 报表模板编码 |
| 3 | fsamplename | 报表模板名称 | varchar | 255 |  | √ | ' ' | 报表模板名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_sm_cr_seqentry_fid |  | fid |
| 2 | pk_t_xkcr_sm_cr_seqentry |  | fentryid |

---

## 工作底稿生成范围-子表 t_xkcr_sm_work_entry

- **表名称：** 工作底稿生成范围-子表
- **表名：** t_xkcr_sm_work_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrycycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 3 | fsample | 报表模板 | varchar | 36 |  | √ | ' ' | [合并报表模板（分发后） xkcr_consolidsample_dised](../xkcr_files/xkcr_consolidsample_dised.md) |
| 4 | facctsystem | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 5 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_sm_work_entry |  | fentryid |
| 2 | idx_xkcr_sm_work_entry_fid |  | fid |

---

## 自动合并方案-主表 t_xkcr_smart_merge

- **表名称：** 自动合并方案-主表
- **表名：** t_xkcr_smart_merge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcrsampleseq | 合并模板顺序 | bpchar | 1 |  | √ | '1' | 合并模板顺序,枚举: 1 :按系统默认顺序 2 :自定义顺序 |
| 3 | fworksamplescope | 底稿模板范围 | bpchar | 1 |  | √ | '1' | 底稿模板范围,枚举: 1 :合并方案的所有报表模板 2 :指定报表模板 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fautolock | 执行锁 | bpchar | 1 |  | √ | '0' | 执行锁 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | felimcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fgenperiod | 生成本期或上期 | bpchar | 1 |  | √ | '1' | 生成本期或上期,枚举: 1 :生成本期 2 :生成上期 |
| 11 | fprocesscount | 第 | int8 | 64 |  | √ | 0 | 第 |
| 12 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | flastexetime | 最后生成执行时间 | timestamp | 0 |  |  | null | 最后生成执行时间 |
| 14 | ffrequency | 执行时间为 | bpchar | 1 |  | √ | '2' | 执行时间为,枚举: 1 :每日 2 :每期 3 :每月 4 :不执行 |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fadjustcreatemode | 模板重复生成 | bpchar | 1 |  | √ | '0' | 模板重复生成,枚举: 0 :覆盖已生成分录 1 :追加生成分录 |
| 18 | fsinglesamplescope | 个别模板范围 | bpchar | 1 |  | √ | '1' | 个别模板范围,枚举: 1 :合并方案的所有报表模板 2 :指定报表模板 3 :选择部分报表模板 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fadjustcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 21 | faddlock | 入队锁 | bpchar | 1 |  | √ | '0' | 入队锁 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fperiodvalues | 期间值 | varchar | 100 |  | √ | ' ' | 期间值 |
| 24 | flastaddqueue | 最后加入队列时间 | timestamp | 0 |  |  | null | 最后加入队列时间 |
| 25 | fcrsamplescope | 合并模板范围 | bpchar | 1 |  | √ | '1' | 合并模板范围,枚举: 1 :合并方案的所有报表模板 |
| 26 | fworksampleseq | 底稿生成顺序 | bpchar | 1 |  | √ | '1' | 底稿生成顺序,枚举: 1 :按系统默认顺序 2 :自定义顺序 |
| 27 | fdateforperiod | 天 | int4 | 32 |  | √ | 0 | 天 |
| 28 | fcurrencyscheme | fcurrencyscheme | int8 | 64 |  | √ | 0 |  |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | felimcurcreatemode | 模板重复生成 | bpchar | 1 |  | √ | '0' | 模板重复生成,枚举: 0 :覆盖已生成分录 1 :追加生成分录 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fcycleid | 周期类型 | varchar | 10 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 33 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 34 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fsinglesampleseq | 个别模板顺序 | bpchar | 1 |  | √ | '1' | 个别模板顺序,枚举: 1 :按系统默认顺序 2 :自定义顺序 |
| 37 | fscope | 方案适用范围 | bpchar | 1 |  | √ | '1' | 方案适用范围,枚举: 1 :所有期间 2 :指定期间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_smart_merge |  | fid |
| 2 | idx_xkcr_smart_merge_num |  | fnumber |

---

## 自动合并方案-多语言表 t_xkcr_smart_merge_l

- **表名称：** 自动合并方案-多语言表
- **表名：** t_xkcr_smart_merge_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 2000 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_smart_merge_l |  | fpkid |
| 2 | idx_xkcr_smart_merge_l_fid |  | fid,flocaleid |

---

## 报表折算-子表 t_xkcr_sm_currency_entry

- **表名称：** 报表折算-子表
- **表名：** t_xkcr_sm_currency_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrencyscheme | 折算方案 | int8 | 64 |  | √ | 0 | [折算方案 xkrpt_currencyscheme](../xkrpt_files/xkrpt_currencyscheme.md) |
| 3 | fsccurrency | 储备币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_sm_currency_entry_fid |  | fid |
| 2 | pk_xkcr_sm_currency_entry |  | fentryid |
