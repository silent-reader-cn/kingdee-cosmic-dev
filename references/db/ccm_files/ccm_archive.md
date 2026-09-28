# 信用档案-ccm_archive

## 额度共享范围-多选基础资料表 t_ccm_shareorgs

- **表名称：** 额度共享范围-多选基础资料表
- **表名：** t_ccm_shareorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_shareorgs |  | fpkid |
| 2 | idx_shareorgs_bdid_id |  | fbasedataid,fid |

---

## 信用档案-主表 t_ccm_archive

- **表名称：** 信用档案-主表
- **表名：** t_ccm_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fvaliddatebegindate | 有效期范围.开始 | timestamp | 0 |  |  | null | 有效期范围.开始 |
| 4 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [信控维度 ccm_dimension](../ccm_files/ccm_dimension.md) |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsrcapplyentryid | 来源档案申请分录ID | int8 | 64 |  | √ | 0 | 来源档案申请分录ID |
| 9 | fenddate | 生效日期范围（旧）.结束 | timestamp | 0 |  |  | null | 生效日期范围（旧）.结束 |
| 10 | fiseffect | fiseffect | bpchar | 1 |  | √ | '1' |  |
| 11 | finitialdatetime | 信用初始日期 | timestamp | 0 |  |  | null | 信用初始日期 |
| 12 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | feffectstate | 生效状态（旧） | varchar | 30 |  | √ | ' ' | 生效状态（旧）,枚举: ISEFFECT :已生效 NOEFFECT :未生效 EXPRIED :已失效 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fnewrole2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | foccupyamount | 实际占用额度 | numeric | 23 | 10 | √ | 0 | 实际占用额度 |
| 17 | fnewrole3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fnewrole0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 19 | fnewrole1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2 |
| 21 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3 |
| 22 | frelatedid | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 23 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0 |
| 24 | fquota | 初始额度 | numeric | 23 | 10 | √ | 0.0000000000 | 初始额度 |
| 25 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1 |
| 26 | freducesum | 作废_占用额度 | numeric | 23 | 10 | √ | 0.0000000000 | 作废_占用额度 |
| 27 | fdimensionvalue | 维度取值 | varchar | 255 |  | √ | ' ' | 维度取值 |
| 28 | fbalance | 余额 | numeric | 23 | 10 | √ | 0.0000000000 | 余额 |
| 29 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :信用额度 qty :信用数量 days :信用天数 overdueamt :逾期额度 privilegeamt :特批总额 privilegeday :特批天数 singlebalance :单笔限额 presscontrol :压批批数 |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnewschemeid | 信用控制方案 | int8 | 64 |  | √ | 0 | [信用控制方案 ccm_schemes](../ccm_files/ccm_schemes.md) |
| 32 | funit | 额度单位 | int8 | 64 |  | √ | 0 | 额度单位 |
| 33 | fsinglecurcontrol | 币种控制 | bpchar | 1 |  | √ | '0' | 币种控制 |
| 34 | fschemeid | 作废_信控方案 | int8 | 64 |  | √ | 0 | [（废弃）信控方案 ccm_scheme](../ccm_files/ccm_scheme.md) |
| 35 | fnewarchive | 是否新档案 | bpchar | 1 |  | √ | '1' | 是否新档案 |
| 36 | frerundatetime | 信用重算日期 | timestamp | 0 |  |  | null | 信用重算日期 |
| 37 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 维度成员值0 |
| 38 | fnewroletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 bd_customergroup :客户分类 bd_operator :供应链业务员 |
| 39 | fnewroletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 bd_customergroup :客户分类 bd_operator :供应链业务员 |
| 40 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 维度成员值2 |
| 41 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 维度成员值1 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 维度成员值3 |
| 44 | fnewroletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 bd_customergroup :客户分类 bd_operator :供应链业务员 |
| 45 | fnewroletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 bd_customergroup :客户分类 bd_operator :供应链业务员 |
| 46 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fincreasesum | 作废_返还额度 | numeric | 23 | 10 | √ | 0.0000000000 | 作废_返还额度 |
| 49 | fgradeid | 信用等级 | int8 | 64 |  | √ | 0 | [（废弃）信用等级 ccm_grade](../ccm_files/ccm_grade.md) |
| 50 | forgscope | 控制组织范围 | varchar | 50 |  | √ | ' ' | 控制组织范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 52 | fbegindate | 生效日期范围（旧）.开始 | timestamp | 0 |  |  | null | 生效日期范围（旧）.开始 |
| 53 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 54 | farchivetype | 档案类型 | varchar | 30 |  | √ | ' ' | 档案类型,枚举: normal :普通档案 temp :临时档案 |
| 55 | fsrctempapplyentryid | 来源临时档案申请分录ID | int8 | 64 |  | √ | 0 | 来源临时档案申请分录ID |
| 56 | fvaliddateenddate | 有效期范围.结束 | timestamp | 0 |  |  | null | 有效期范围.结束 |
| 57 | fcheckstatus | 信用检查状态 | varchar | 50 |  | √ | 'CHECKED' | 信用检查状态,枚举: CHECKED :正常检查 UNCHECKED :信用免检 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_archive_dimval |  | fdimensionvalue |
| 2 | t_ccm_archive_pkey |  | fid |
| 3 | idx_ccm_archive_date |  | fschemeid,fbegindate,fenddate |

---

## 信用档案-多语言表 t_ccm_archive_l

- **表名称：** 信用档案-多语言表
- **表名：** t_ccm_archive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_archive_l |  | fid,flocaleid |
| 2 | pk_t_ccm_archive_l |  | fpkid |
