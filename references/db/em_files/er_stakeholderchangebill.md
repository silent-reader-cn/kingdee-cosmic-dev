# 干系人变更单-er_stakeholderchangebill

## 关联子实体-子表 t_er_stakeholderbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_stakeholderbill_lk

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
| 1 | idx_er_stakeholderbill_lk_fk |  | fid |
| 2 | pk_t_er_stakeholderbill_lk |  | fpkid |

---

## 干系人变更单-主表 t_er_stakeholderbill

- **表名称：** 干系人变更单-主表
- **表名：** t_er_stakeholderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 4 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fremarks | fremarks | varchar | 200 |  | √ | ' ' |  |
| 9 | fdescription | 事由 | varchar | 600 |  | √ | ' ' | 事由 |
| 10 | fchangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: 1 :干系人变更 2 :干系人变更+申请人变更 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fapplierposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 14 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 17 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 18 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 19 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_stakeholderbill |  | fid |
| 2 | idx_er_stake_fbillstatus |  | fbillstatus |
| 3 | idx_er_stake_fbillno |  | fbillno |

---

## 关联子实体-子表 t_er_stakeholderdetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_stakeholderdetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_stakeholderdetail_lk |  | fpkid |
| 2 | idx_er_stakeholderdetail_lk_fk |  | fdetailid |

---

## 干系人(变更后)-多选基础资料表 t_er_stakeholderafter

- **表名称：** 干系人(变更后)-多选基础资料表
- **表名：** t_er_stakeholderafter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_stakeholderafter |  | fpkid |
| 2 | idx_er_stakeholderafter_fk |  | fdetailid |

---

## 变更明细-子表 t_er_stakeholderdetail

- **表名称：** 变更明细-子表
- **表名：** t_er_stakeholderdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierafter | 申请人(变更后) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcdeptid | 反写部门id | varchar | 50 |  | √ | ' ' | 反写部门id |
| 4 | fremarks | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fapplierbefore | 申请人(变更前) | varchar | 200 |  | √ | ' ' | 申请人(变更前) |
| 7 | foribilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_tripreqbill :出差申请单 er_applyprojectbill :立项单 er_costestimatebill :暂估单 er_prepaybill :预付单 er_contractbill :合同台账单 er_withholdingbill :费用预提单 er_publicreimbursebill :对公报销单 er_dailyreimbursebill :费用报销单 er_tripreimbursebill :差旅报销单 er_dailyvehiclebill :用车申请单 er_tripreimburse_cardgrid :全球差旅报销单 er_tripreqbill_inter :全球出差申请单 er_billingpool :账单池 er_applypaybill :挂账付款申请单 |
| 8 | fstakeholderbefore | 干系人(变更前) | varchar | 200 |  | √ | ' ' | 干系人(变更前) |
| 9 | foribillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 11 | foribillid | 源单单据ID | varchar | 50 |  | √ | ' ' | 源单单据ID |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | foridescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_stakeholderdetail_fk |  | fid |
| 2 | pk_er_stakeholderdetail |  | fdetailid |

---

## 干系人变更单-反写记录表 t_er_stakeholderbill_wb

- **表名称：** 干系人变更单-反写记录表
- **表名：** t_er_stakeholderbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_stakeholderbill_wb_fk |  | fid |
| 2 | pk_er_stakeholderbill_wb |  | fentryid |

---

## 干系人变更单-关联追踪表 t_er_stakeholderbill_tc

- **表名称：** 干系人变更单-关联追踪表
- **表名：** t_er_stakeholderbill_tc

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
| 1 | idx_er_stakeholderbill_tc_tid |  | ftid |
| 2 | pk_er_stakeholderbill_tc |  | fid |
| 3 | idx_er_stakeholderbill_tc_tbill |  | ftbillid |

---

## 干系人变更单-多语言表 t_er_stakeholderbill_l

- **表名称：** 干系人变更单-多语言表
- **表名：** t_er_stakeholderbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_stakeholderbill_l |  | fpkid |
| 2 | idx_er_stakeholderbill_l_0 |  | fid,flocaleid |
