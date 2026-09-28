# 资产拆分单-fa_assetsplitbill

## 资产拆分单-主表 t_fa_assetsplitbill

- **表名称：** 资产拆分单-主表
- **表名：** t_fa_assetsplitbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsplitperiod | fsplitperiod | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fsplittype | 拆分方式 | varchar | 50 |  | √ | 'A' | 拆分方式,枚举: A :按数量拆分 B :按金额拆分 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 11 | fsplitqty | 拆分数量 | int8 | 64 |  | √ | 0 | 拆分数量 |
| 12 | frealcardid | 拆分卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbiztype | 拆分类型 | bpchar | 1 |  | √ | 'A' | 拆分类型,枚举: A :保留原卡片 B :不保留原卡片 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fappliantid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fsplitrate | 拆分比例 | varchar | 50 |  | √ | ' ' | 拆分比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_assetsplitbill_fno |  | fbillno |
| 2 | t_fa_assetsplitbill_pkey |  | fid |

---

## 拆分后卡片-子表 t_fa_assetsplitentry_d

- **表名称：** 拆分后卡片-子表
- **表名：** t_fa_assetsplitentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 4 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 5 | fpartcleardepre | 部分清理累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 部分清理累计折旧 |
| 6 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 7 | fyearorigvalchg | 本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本年原值变动 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 10 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 13 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 14 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 15 | fmonthdeprechg | 本期减值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期减值变动 |
| 16 | fcardbillno | 卡片编号 | varchar | 80 |  | √ | ' ' | 卡片编号 |
| 17 | fmonthorigvalchg | 本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期原值变动 |
| 18 | fassetname | 资产名称 | varchar | 300 |  | √ | ' ' | 资产名称 |
| 19 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fmonthaccumdeprechg | 拆分本期累计折旧变动 | numeric | 23 | 10 | √ | 0 | 拆分本期累计折旧变动 |
| 22 | frealcardid | 资产名称 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 23 | fassetamount | 资产数量 | numeric | 19 | 6 | √ | 0.000000 | 资产数量 |
| 24 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 25 | fcardindex | 卡片序列 | int8 | 64 |  | √ | 0 | 卡片序列 |
| 26 | fsupplierid | 供应商 | int8 | 64 |  |  | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpreresidualval | 净残值 | numeric | 19 | 6 | √ | 0.000000 | 净残值 |
| 28 | fbasecurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 30 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fcardnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_assetsplitentry_d |  | fentryid |
| 2 | t_fa_assetsplitentry_d_pkey |  | fdetailid |

---

## 拆分前卡片-子表 t_fa_assetsplitentry

- **表名称：** 拆分前卡片-子表
- **表名：** t_fa_assetsplitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetamount | 净额 | numeric | 19 | 6 | √ | 0.000000 | 净额 |
| 3 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 4 | fincometax | 进项税额 | numeric | 19 | 6 | √ | 0.000000 | 进项税额 |
| 5 | fpartcleardepre | 部分清理累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 部分清理累计折旧 |
| 6 | fbakfincardbakid | 财务卡片备份 | int8 | 64 |  | √ | 0 | [财务卡片变更备份 fa_changebak_fin](../fa_files/fa_changebak_fin.md) |
| 7 | faccumdepre | 累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 累计折旧 |
| 8 | fyearorigvalchg | 本年原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本年原值变动 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 11 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 12 | fdecval | 减值准备 | numeric | 19 | 6 | √ | 0.000000 | 减值准备 |
| 13 | faddupyeardepre | 本年累计折旧 | numeric | 19 | 6 | √ | 0.000000 | 本年累计折旧 |
| 14 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 15 | fmonthdeprechg | 本期减值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期减值变动 |
| 16 | fmonthorigvalchg | 本期原值变动 | numeric | 19 | 6 | √ | 0.000000 | 本期原值变动 |
| 17 | fmonthdepre | 本期折旧 | numeric | 19 | 6 | √ | 0.000000 | 本期折旧 |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | frealcardid | 资产名称 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 20 | fassetamount | 资产数量 | numeric | 19 | 6 | √ | 0.000000 | 资产数量 |
| 21 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 22 | fsupplierid | 供应商 | int8 | 64 |  |  | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | fpreresidualval | 净残值 | numeric | 19 | 6 | √ | 0.000000 | 净残值 |
| 24 | fbasecurrencyid | 拆分卡片本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | foriginalval | 资产原值 | numeric | 19 | 6 | √ | 0.000000 | 资产原值 |
| 26 | fnetworth | 净值 | numeric | 19 | 6 | √ | 0.000000 | 净值 |
| 27 | fsplitperiodid | 拆分期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fbakrealcardid | 实物卡片备份 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_assetsplitentry_fid |  | fid |
| 2 | t_fa_assetsplitentry_pkey |  | fentryid |

---

## 资产条码-多选基础资料表 t_fa_assetsplit_barcode

- **表名称：** 资产条码-多选基础资料表
- **表名：** t_fa_assetsplit_barcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资产条码打印 barcm_barcodemainfile_fa](../barcm_files/barcm_barcodemainfile_fa.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_assetsplit_barcode |  | fpkid |
| 2 | idx_fa_assetspl_bc_fdetail |  | fdetailid |

---

## 拆分后卡片-多语言表 t_fa_assetsplitentry_d_l

- **表名称：** 拆分后卡片-多语言表
- **表名：** t_fa_assetsplitentry_d_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fassetname | 资产名称 | varchar | 300 |  | √ | ' ' | 资产名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_assetsplitentry_d_l |  | fpkid |
| 2 | idx_fa_assetsplitentry_d_l |  | fdetailid,flocaleid |
