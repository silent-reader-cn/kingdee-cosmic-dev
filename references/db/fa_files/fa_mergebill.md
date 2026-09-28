# 资产合并单-fa_mergebill

## 转出资产明细-子表 t_fa_merge_out

- **表名称：** 转出资产明细-子表
- **表名：** t_fa_merge_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutchangemode | 减少方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 3 | foutoriginalval | 转出资产原值 | numeric | 19 | 6 | √ | 0 | 转出资产原值 |
| 4 | foutpreusingamount | foutpreusingamount | numeric | 19 | 6 | √ | 0 |  |
| 5 | foutbasecurrencyid | 转出本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | foutpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 7 | foutrealunitid | foutrealunitid | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | foutdecval | 转出减值准备 | numeric | 19 | 6 | √ | 0 | 转出减值准备 |
| 10 | foutdepreuseid | foutdepreuseid | int8 | 64 |  | √ | 0 |  |
| 11 | fafteroutfinid | 变更后财务信息 | int8 | 64 |  | √ | 0 | [财务卡片变更备份 fa_changebak_fin](../fa_files/fa_changebak_fin.md) |
| 12 | foutrealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 13 | foutcompfieldsv | 比较字段值 | varchar | 200 |  | √ | ' ' | 比较字段值 |
| 14 | foutaccumdepre | 转出累计折旧 | numeric | 19 | 6 | √ | 0 | 转出累计折旧 |
| 15 | fbeforeoutfinid | 变更前财务信息 | int8 | 64 |  | √ | 0 | [财务卡片变更备份 fa_changebak_fin](../fa_files/fa_changebak_fin.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | foutpreresidualval | 转出净残值 | numeric | 19 | 6 | √ | 0 | 转出净残值 |
| 18 | foutrealcardmasterid | 实物卡片masterID | int8 | 64 |  | √ | 0 | 实物卡片masterID |
| 19 | foutrealamount | foutrealamount | numeric | 23 | 10 | √ | 0 |  |
| 20 | foutfincardid | 转出财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_merge_out |  | fid |
| 2 | pk_t_fa_merge_out |  | fentryid |

---

## 转入资产明细-子表 t_fa_merge_in

- **表名称：** 转入资产明细-子表
- **表名：** t_fa_merge_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finrealcardbak | 备份实物卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 3 | finoriginalval | 转入资产原值 | numeric | 19 | 6 | √ | 0 | 转入资产原值 |
| 4 | findecval | 转入减值准备 | numeric | 19 | 6 | √ | 0 | 转入减值准备 |
| 5 | finbasecurrencyid | 转入本位币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | finpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 7 | finfincardid | 转入财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 8 | fincompfieldsv | 比较字段值 | varchar | 200 |  | √ | ' ' | 比较字段值 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fafterinfinid | 变更后财务信息 | int8 | 64 |  | √ | 0 | [财务卡片变更备份 fa_changebak_fin](../fa_files/fa_changebak_fin.md) |
| 11 | fbeforeinfinid | 变更前财务信息 | int8 | 64 |  | √ | 0 | [财务卡片变更备份 fa_changebak_fin](../fa_files/fa_changebak_fin.md) |
| 12 | finrealunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | finaccumdepre | 转入累计折旧 | numeric | 19 | 6 | √ | 0 | 转入累计折旧 |
| 14 | finrealcardid | 资产名称 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 15 | findepredamount | 转入已折旧期数 | numeric | 19 | 6 | √ | 0 | 转入已折旧期数 |
| 16 | finpreresidualval | 转入净残值 | numeric | 19 | 6 | √ | 0 | 转入净残值 |
| 17 | finchangemode | 增减方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 18 | fmergeperiodid | 合并期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 19 | finrealcardmasterid | 实物卡片masterID | int8 | 64 |  | √ | 0 | 实物卡片masterID |
| 20 | finrealamount | 转入资产数量 | numeric | 23 | 10 | √ | 0 | 转入资产数量 |
| 21 | findepreuseid | findepreuseid | int8 | 64 |  | √ | 0 |  |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_merge_in |  | fentryid |
| 2 | idx_fa_merge_in |  | fid |

---

## 资产合并单-主表 t_fa_mergebill

- **表名称：** 资产合并单-主表
- **表名：** t_fa_mergebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmergedate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fvoucherflag | 记账标识 | bpchar | 1 |  | √ | 'A' | 记账标识,枚举: A :无需记账 B :待记账 C :已记账 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 11 | frealcardid | 转入资产 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :完全转入已有 2 :完全转入新增 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_mergebill_org |  | forgid,fmergedate |
| 2 | idx_fa_mergebill_billno |  | fbillno |
| 3 | pk_t_fa_mergebill |  | fid |

---

## 资产合并单-多语言表 t_fa_mergebill_l

- **表名称：** 资产合并单-多语言表
- **表名：** t_fa_mergebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_mergebill_l |  | fpkid |
| 2 | idx_fa_mergebill_l |  | fid,flocaleid |
