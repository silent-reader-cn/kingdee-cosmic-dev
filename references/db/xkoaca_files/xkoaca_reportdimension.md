# 经营报表维度-xkoaca_reportdimension

## 经营报表维度-多语言表 t_xkoaca_rptdim_l

- **表名称：** 经营报表维度-多语言表
- **表名：** t_xkoaca_rptdim_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rptdim_l |  | fpkid |
| 2 | idx_xkoaca_rptdim_l |  | fid,flocaleid |

---

## 经营科目固定范围-多选基础资料表 t_xkoaca_rptdim_acct

- **表名称：** 经营科目固定范围-多选基础资料表
- **表名：** t_xkoaca_rptdim_acct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营科目 xkoac_account](../xkoac_files/xkoac_account.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoaca_rptdim_acct |  | fbasedataid |
| 2 | pk_xkoaca_rptdim_acct |  | fpkid |

---

## 经营报表维度-主表 t_xkoaca_rptdim

- **表名称：** 经营报表维度-主表
- **表名：** t_xkoaca_rptdim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimvaluebtngrp | 维度取值设置 | bpchar | 1 |  | √ | ' ' | 维度取值设置,枚举: 1 :按报表过滤界面选择范围 2 :按固定范围分项取值 3 :按固定范围汇总取值 |
| 3 | fdimfilter_tag | 经营核算维度过滤条件设置_详情 | text | 0 |  |  | null | 经营核算维度过滤条件设置_详情 |
| 4 | ftradetype | 交易类型 | varchar | 20 |  | √ | ' ' | 交易类型,枚举: 1 :日常业务 2 :内部交易 3 :内部分摊 4 :调整业务 5 :共享业务 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 10 | fisdisplaysum | 显示小计 | bpchar | 1 |  | √ | '0' | 显示小计 |
| 11 | fperiodtypebtngrp | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: 1 :无 2 :天 3 :月 4 :季 5 :年 6 :会计期间 7 :会计年度 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsrcdimension | 维度来源 | int8 | 64 |  | √ | 0 | [自定义报表维度来源 xkoaca_srcdimension](../xkoaca_files/xkoaca_srcdimension.md) |
| 15 | fdimfilterdesc | 经营核算维度过滤条件 | varchar | 2000 |  | √ | ' ' | 经营核算维度过滤条件 |
| 16 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fdimfixedvalues | 经营核算维度固定值 | varchar | 2000 |  | √ | ' ' | 经营核算维度固定值 |
| 18 | fdimvalueids | 经营核算维度固定值id集合 | text | 0 |  |  | null | 经营核算维度固定值id集合 |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | frelativeperiod | 相对期间 | int4 | 32 |  | √ | 0 | 相对期间 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbizdimension | 经营核算维度来源 | int8 | 64 |  | √ | 0 | [经营核算维度 xkoac_dimension](../basedata_files/xkoac_dimension.md) |
| 24 | fdimvalueids_tag | 经营核算维度固定值id集合_详情 | text | 0 |  |  | null | 经营核算维度固定值id集合_详情 |
| 25 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 26 | fvaluerangebtngrp | 取值期间 | bpchar | 1 |  | √ | ' ' | 取值期间,枚举: 1 :查询范围所有期间 2 :查询范围最大期间 3 :查询范围最小期间 4 :截止到查询范围的最大日期 5 :无 |
| 27 | fdimfilter | 经营核算维度过滤条件设置 | text | 0 |  |  | null | 经营核算维度过滤条件设置 |
| 28 | fdisableperson | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 30 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 31 | fdimtypebtngrp | 维度类型 | bpchar | 1 |  | √ | ' ' | 维度类型,枚举: 1 :经营主体 2 :时间维度 3 :经营指标 |
| 32 | fdimdispbtngroup | 维度显示 | bpchar | 1 |  | √ | ' ' | 维度显示,枚举: 1 :名称 2 :编码 3 :编码/名称 |
| 33 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rptdim |  | fid |
| 2 | idx_xkoaca_rptdim_fnum |  | fnumber |

---

## 经营单元固定范围-多选基础资料表 t_xkoaca_rptdim_amba

- **表名称：** 经营单元固定范围-多选基础资料表
- **表名：** t_xkoaca_rptdim_amba

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rptdim_amba |  | fpkid |
| 2 | idx_xkoaca_rptdim_amba |  | fbasedataid |

---

## 经营账簿-多选基础资料表 t_xkoaca_rptdim_opbk

- **表名称：** 经营账簿-多选基础资料表
- **表名：** t_xkoaca_rptdim_opbk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoaca_rptdim_opbk |  | fbasedataid |
| 2 | pk_xkoaca_rptdim_opbk |  | fpkid |
