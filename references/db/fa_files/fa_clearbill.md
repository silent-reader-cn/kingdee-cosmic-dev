# 资产清理单-fa_clearbill

## 关联子实体-子表 t_fa_clrbillentry_d_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_clrbillentry_d_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentrysid | fentrysid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clrbillentry_fentrysid |  | fentrysid |
| 2 | pk_t_fa_clrbillentry_d_lk |  | fpkid |

---

## 资产清理单-关联追踪表 t_fa_clrbill_tc

- **表名称：** 资产清理单-关联追踪表
- **表名：** t_fa_clrbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clrbill_tc_tid |  | ftid |
| 2 | idx_fa_clrbill_tc_tbill |  | ftbillid |
| 3 | t_fa_clrbill_tc_pkey |  | fid |
| 4 | idx_fa_clrbill_tc_sbid |  | fsbillid |

---

## 资产清理单-反写记录表 t_fa_clrbill_wb

- **表名称：** 资产清理单-反写记录表
- **表名：** t_fa_clrbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_clrbill_wb_pkey |  | fentryid |
| 2 | idx_fa_clrbill_wb |  | fid |

---

## 资产清理单-主表 t_fa_clrbill

- **表名称：** 资产清理单-主表
- **表名：** t_fa_clrbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fclearperiodid | fclearperiodid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fhasvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 8 | freason | 清理原因 | varchar | 255 |  |  | ' ' | 清理原因 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fchangemodeid | 减少方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 15 | fcleardate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fclearsource | 清理来源 | varchar | 50 |  | √ | 'APPLY' | 清理来源,枚举: ADDNEW :新增 APPLY :清理申请 DISPATCH :调拨 INVENTORY_LOSS :盘亏 LEASE_TERMINATION :租赁终止 MERGE :合并 SPLIT :拆分 |

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

---

## 资产条码-多选基础资料表 t_fa_clrbill_barcode

- **表名称：** 资产条码-多选基础资料表
- **表名：** t_fa_clrbill_barcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资产条码打印 barcm_barcodemainfile_fa](../barcm_files/barcm_barcodemainfile_fa.md) |
| 2 | fentrysid | fentrysid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_clrbill_barcode |  | fpkid |
| 2 | idx_fa_clrbill_bc_fdetail |  | fentrysid |

---

## 清理资产详情分录-子表 t_fa_clrbillentry_d

- **表名称：** 清理资产详情分录-子表
- **表名：** t_fa_clrbillentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddupdepre | 清理累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 清理累计折旧 |
| 3 | fnetamount | 清理资产净额 | numeric | 19 | 6 | √ | 0.000000 | 清理资产净额 |
| 4 | fclearloss | 清理净损失 | numeric | 19 | 6 | √ | 0 | 清理净损失 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcleancurrency | 清理币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fclearrevenue | 清理净收益 | numeric | 19 | 6 | √ | 0 | 清理净收益 |
| 8 | fdepredamount | 清理已折旧期间数 | numeric | 19 | 6 | √ | 0.000000 | 清理已折旧期间数 |
| 9 | fisclearall | 清理类型标识 | bpchar | 1 |  | √ | '1' | 清理类型标识,枚举: 0 :原值部分清理 1 :完全清理 2 :数量部分清理 |
| 10 | fisadjustdepre | 是否为调整后清理 | bpchar | 1 |  | √ | 0 | 是否为调整后清理 |
| 11 | fclearrate | 清理率 | numeric | 23 | 10 | √ | 0.0000000000 | 清理率 |
| 12 | fclearmethod | 清理累计折旧计算方法 | varchar | 8 |  | √ | ' ' | 清理累计折旧计算方法,枚举: ADJ :来自折旧调整 PRE :来自清理预提 FIN :来自财务卡片 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fdecval | 清理减值准备 | numeric | 19 | 6 | √ | 0.000000 | 清理减值准备 |
| 15 | floctaxamountentry | 税额（本位币） | numeric | 19 | 6 | √ | 0 | 税额（本位币） |
| 16 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 17 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 18 | fclearfare | 清理费用 | numeric | 19 | 6 | √ | 0.000000 | 清理费用 |
| 19 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 20 | flocclearfare | 清理费用（本位币） | numeric | 19 | 6 | √ | 0 | 清理费用（本位币） |
| 21 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 22 | ftaxamount | 税额 | numeric | 19 | 6 | √ | 0 | 税额 |
| 23 | fclearperiodid | 清理期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 24 | fclearincome | 清理收入（含税） | numeric | 19 | 6 | √ | 0.000000 | 清理收入（含税） |
| 25 | frevaluationreserve | 清理重估准备金 | numeric | 19 | 6 | √ | 0 | 清理重估准备金 |
| 26 | fassetqty | 资产数量 | numeric | 23 | 10 | √ | 0.0000000000 | 资产数量 |
| 27 | fcompfieldsv | 比较字段值 | varchar | 200 |  | √ | ' ' | 比较字段值 |
| 28 | fassetvalue | 清理资产原值 | numeric | 19 | 6 | √ | 0.000000 | 清理资产原值 |
| 29 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 30 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 31 | fclearqty | 清理数量 | numeric | 19 | 6 | √ | 0.000000 | 清理数量 |
| 32 | fpreresidualval | 清理资产残值 | numeric | 19 | 6 | √ | 0.000000 | 清理资产残值 |
| 33 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | flocclearincome | 清理收入（含税）（本位币） | numeric | 19 | 6 | √ | 0 | 清理收入（含税）（本位币） |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fcurrencyrate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 37 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fentrysid | fentrysid | int8 | 64 |  | √ | 0 | id |
| 39 | fnetval | fnetval | numeric | 19 | 6 | √ | 0.000000 |  |
| 40 | fentryid | 分录 | int8 | 64 |  | √ | 0 | 分录 |
| 41 | fmonthadjustdepreforcur | 本期调整折旧额当期卡片 | numeric | 19 | 6 | √ | 0 | 本期调整折旧额当期卡片 |
| 42 | fassetnumber | 资产编码 | varchar | 100 |  | √ | ' ' | 资产编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentrysid | fentrysid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_clrbillentry_d |  | fentrysid |
| 2 | idx_fa_clrbillentry_d_fid |  | fid |
| 3 | idx_fa_clrbilent_d_fentryid |  | fentryid |

---

## 清理收入/费用详情-子表 t_fa_clrbillentry_cost

- **表名称：** 清理收入/费用详情-子表
- **表名：** t_fa_clrbillentry_cost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 19 | 6 | √ | 0 | 税额 |
| 3 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcleancurrency | 清理币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fclearrevenue | 清理收入（含税） | numeric | 19 | 6 | √ | 0 | 清理收入（含税） |
| 7 | fassociation | 关联应收 | bpchar | 1 |  | √ | '0' | 关联应收 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fclearcost | 清理费用 | numeric | 19 | 6 | √ | 0 | 清理费用 |
| 10 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_clrbillentry_cost |  | fentryid |
| 2 | idx_fa_clrbillentry_cost_fid |  | fid |

---

## 关联子实体-子表 t_fa_clrbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_clrbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_clrbill_lk |  | fid |
| 2 | t_fa_clrbill_lk_pkey |  | fpkid |
