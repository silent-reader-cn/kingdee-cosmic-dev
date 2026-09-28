# 资产变更单-fa_change_dept

## 资产变更单-主表 t_fa_changebill

- **表名称：** 资产变更单-主表
- **表名：** t_fa_changebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsourceid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 8 | fhasvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 9 | fnewchangetype | 变更类型 | int8 | 64 |  | √ | 0 | 变更类型 fa_change_type |
| 10 | fvoucherflag | 记账标识 | bpchar | 1 |  | √ | 'A' | 记账标识,枚举: B :待记账 C :已记账 A :无需记账 |
| 11 | fchangetype | 旧变更类型 | varchar | 50 |  | √ | 'ASSETVALUE' | 旧变更类型 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fappliantid | 变更申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcetype | 来源方式 | bpchar | 1 |  | √ | '1' | 来源方式,枚举: 1 :移动端移交或领用 2 :手工新增 3 :在建工程 4 :合同变更 |
| 17 | fchangedate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chabil_fbillno |  | fbillno |
| 2 | t_fa_changebill_pkey |  | fid |
| 3 | idx_fa_chabil_org_comb |  | forgid,fchangedate |

---

## 资产条码-多选基础资料表 t_fa_card_barcode

- **表名称：** 资产条码-多选基础资料表
- **表名：** t_fa_card_barcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_barcode |  | fpkid |
| 2 | idx_fa_card_bc_fdetail |  | fid |

---

## 关联子实体-子表 t_fa_changebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_changebill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_changebill_lk_fk |  | fid |
| 2 | pk_fa_changebill_lk |  | fpkid |

---

## 资产变更单-反写记录表 t_fa_changebill_wb

- **表名称：** 资产变更单-反写记录表
- **表名：** t_fa_changebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_changebill_wb_fk |  | fid |
| 2 | pk_fa_changebill_wb |  | fentryid |

---

## 财务变更详情-子表 t_fa_changebillfinentry

- **表名称：** 财务变更详情-子表
- **表名：** t_fa_changebillfinentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fisadjustdepre | 未来适用 | bpchar | 1 |  | √ | '0' | 未来适用 |
| 2 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | fbeforefininfo | 变更前财务信息 | int8 | 64 |  | √ | 0 | 财务卡片变更备份 fa_changebak_fin |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fafterfininfo | 变更后财务信息 | int8 | 64 |  | √ | 0 | 财务卡片变更备份 fa_changebak_fin |
| 7 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 11 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chgfentry |  | fentryid |
| 2 | t_fa_changebillfinentry_pkey |  | fdetailid |

---

## 变更项目-多选基础资料表 t_fa_changebill_chgitem

- **表名称：** 变更项目-多选基础资料表
- **表名：** t_fa_changebill_chgitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 变更项目 fa_change_item |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_changebill_chgitem |  | fid |
| 2 | pk_t_fa_changebill_chgitem |  | fpkid |

---

## 变更详情分录-子表 t_fa_changebillentry_d

- **表名称：** 变更详情分录-子表
- **表名：** t_fa_changebillentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fafterrealinfo | fafterrealinfo | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbfrchgdesc | 变更前摘要 | varchar | 100 |  |  | ' ' | 变更前摘要 |
| 5 | freason | 变更理由 | varchar | 255 |  |  | ' ' | 变更理由 |
| 6 | faftchg | 变更后 | varchar | 500 |  |  | ' ' | 变更后 |
| 7 | frealcardid | 卡片编号 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 8 | faftchgdesc | 变更后摘要 | varchar | 100 |  |  | ' ' | 变更后摘要 |
| 9 | fbfrchg | 变更前 | varchar | 500 |  |  | ' ' | 变更前 |
| 10 | fbeforefininfo | 变更前财务信息 | int8 | 64 |  | √ | 0 | 财务卡片变更备份 fa_changebak_fin |
| 11 | fbfrorginval | fbfrorginval | numeric | 19 | 6 | √ | 0.000000 |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fafterfininfo | 变更后财务信息 | int8 | 64 |  | √ | 0 | 财务卡片变更备份 fa_changebak_fin |
| 14 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 15 | fentryid | 分录 | int8 | 64 |  | √ | 0 | 分录 |
| 16 | faftorginval | faftorginval | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | faftrealcardid | 变更后实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 18 | fbeforerealinfo | fbeforerealinfo | int8 | 64 |  | √ | 0 |  |
| 19 | fdepreuseid | fdepreuseid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chabilent_d_fentryid |  | fentryid |
| 2 | t_fa_changebillentry_d_pkey |  | fdetailid |
| 3 | idx_fa_chabilent_d_fid |  | fid |

---

## 实物变更详情-子表 t_fa_changebillrealentry

- **表名称：** 实物变更详情-子表
- **表名：** t_fa_changebillrealentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | faftrealcardid | 变更后实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 5 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_changebillrealentry_pkey |  | fentryid |
| 2 | idx_fa_chgreal |  | fid |

---

## 资产变更单-关联追踪表 t_fa_changebill_tc

- **表名称：** 资产变更单-关联追踪表
- **表名：** t_fa_changebill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_changebill_tc |  | fid |
| 2 | idx_fa_changebill_tc_tid |  | ftid |
| 3 | idx_fa_changebill_tc_tbill |  | ftbillid |

---

## 变更字段分录-子表 t_fa_changefieldentry

- **表名称：** 变更字段分录-子表
- **表名：** t_fa_changefieldentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffield | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | freason | 变更理由 | varchar | 255 |  | √ | ' ' | 变更理由 |
| 5 | frealcardid | 资产名称 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 6 | fbeforevalue | 变更前的值 | varchar | 255 |  | √ | ' ' | 变更前的值 |
| 7 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 8 | faftervalue | 变更后的值 | varchar | 255 |  | √ | ' ' | 变更后的值 |
| 9 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fisadjustdepre | 未来适用 | bpchar | 1 |  | √ | '1' | 未来适用 |
| 11 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fassetnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 16 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chgfieldentry |  | fid |
| 2 | t_fa_changefieldentry_pkey |  | fentryid |
