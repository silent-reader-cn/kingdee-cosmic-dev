# 信用档案-ccm_archive

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

---

## 额度共享范围-多选基础资料表 t_ccm_shareorgs

- **表名称：** 额度共享范围-多选基础资料表
- **表名：** t_ccm_shareorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fsinglecurcontrol | 币别控制 | bpchar | 1 |  | √ | '0' | 币别控制 |
| 4 | fvaliddatebegindate | 有效期范围.开始 | timestamp | 0 |  |  | null | 有效期范围.开始 |
| 5 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | 信控维度 ccm_dimension |
| 6 | fschemeid | 作废_信控方案 | int8 | 64 |  | √ | 0 | （废弃）信控方案 ccm_scheme |
| 7 | fnewarchive | 是否新档案 | bpchar | 1 |  | √ | '1' | 是否新档案 |
| 8 | frerundatetime | 信用重算日期 | timestamp | 0 |  |  | null | 信用重算日期 |
| 9 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 维度成员值0 |
| 10 | fnewroletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 11 | fenddate | 生效日期范围（旧）.结束 | timestamp | 0 |  |  | null | 生效日期范围（旧）.结束 |
| 12 | fnewroletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 13 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 维度成员值2 |
| 14 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 维度成员值1 |
| 15 | fiseffect | fiseffect | bpchar | 1 |  | √ | '1' |  |
| 16 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 维度成员值3 |
| 17 | finitialdatetime | 信用初始日期 | timestamp | 0 |  |  | null | 信用初始日期 |
| 18 | feffectstate | 生效状态（旧） | varchar | 30 |  | √ | ' ' | 生效状态（旧）,枚举: ISEFFECT :已生效 NOEFFECT :未生效 EXPRIED :已失效 |
| 19 | fnewroletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fnewroletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 22 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 23 | fincreasesum | 作废_返还额度 | numeric | 23 | 10 | √ | 0.0000000000 | 作废_返还额度 |
| 24 | fgradeid | 信用等级 | int8 | 64 |  | √ | 0 | 信用等级 ccm_grade |
| 25 | fnewrole2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | foccupyamount | 实际占用额度 | numeric | 23 | 10 | √ | 0 | 实际占用额度 |
| 27 | forgscope | 控制组织范围 | varchar | 50 |  | √ | ' ' | 控制组织范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 28 | fnewrole3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fbegindate | 生效日期范围（旧）.开始 | timestamp | 0 |  |  | null | 生效日期范围（旧）.开始 |
| 30 | fnewrole0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 31 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | fnewrole1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 33 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2 |
| 34 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3 |
| 35 | frelatedid | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 36 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0 |
| 37 | fquota | 初始额度 | numeric | 23 | 10 | √ | 0.0000000000 | 初始额度 |
| 38 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1 |
| 39 | farchivetype | 档案类型 | varchar | 30 |  | √ | ' ' | 档案类型,枚举: normal :普通档案 temp :临时档案 |
| 40 | freducesum | 作废_占用额度 | numeric | 23 | 10 | √ | 0.0000000000 | 作废_占用额度 |
| 41 | fdimensionvalue | 维度取值 | varchar | 255 |  | √ | ' ' | 维度取值 |
| 42 | fbalance | 余额 | numeric | 23 | 10 | √ | 0.0000000000 | 余额 |
| 43 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :信用额度 qty :信用数量 days :信用天数 overdueamt :逾期额度 privilegeamt :特批总额 privilegeday :特批天数 |
| 44 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 45 | fnewschemeid | 信用控制方案 | int8 | 64 |  | √ | 0 | 信用控制方案 ccm_schemes |
| 46 | fvaliddateenddate | 有效期范围.结束 | timestamp | 0 |  |  | null | 有效期范围.结束 |
| 47 | funit | 额度单位 | int8 | 64 |  | √ | 0 | 额度单位 |
| 48 | fcheckstatus | 信用检查状态 | varchar | 50 |  | √ | 'CHECKED' | 信用检查状态,枚举: CHECKED :正常检查 UNCHECKED :信用免检 |

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
