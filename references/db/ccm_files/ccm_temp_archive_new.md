# 临时信用档案申请-ccm_temp_archive_new

## 临时信用档案申请-关联追踪表 t_ccm_temp_archive_new_tc

- **表名称：** 临时信用档案申请-关联追踪表
- **表名：** t_ccm_temp_archive_new_tc

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
| 1 | pk_ccm_temp_archive_new_tc |  | fid |
| 2 | idx_ccm_temp_archive_new_tc_tbill |  | ftbillid |
| 3 | idx_ccm_temp_archive_new_tc_tid |  | ftid |

---

## 临时档案设置-子表 t_ccm_temparchive_entity

- **表名称：** 临时档案设置-子表
- **表名：** t_ccm_temparchive_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fsinglecurcontrol | 币别隔离 | bpchar | 1 |  | √ | ' ' | 币别隔离 |
| 4 | forgscope | 控制范围 | varchar | 50 |  | √ | ' ' | 控制范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 5 | fvaliddatebegindate | 有效期范围.开始 | timestamp | 0 |  |  | null | 有效期范围.开始 |
| 6 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ftempquota | 临时信用额度 | numeric | 23 | 10 | √ | 0 | 临时信用额度 |
| 10 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 11 | ftempoverdueamt | 临时逾期额度 | numeric | 23 | 10 | √ | 0 | 临时逾期额度 |
| 12 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | fe_remark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fscheme | 信用控制方案 | int8 | 64 |  | √ | 0 | 信用控制方案 ccm_schemes |
| 18 | farchiveids | 普通档案ID列表 | varchar | 200 |  | √ | ' ' | 普通档案ID列表 |
| 19 | ftempday | 临时信用天数 | int8 | 64 |  | √ | 0 | 临时信用天数 |
| 20 | fvaliddateenddate | 有效期范围.结束 | timestamp | 0 |  |  | null | 有效期范围.结束 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_temparchive_entity_fk |  | fid |
| 2 | pk_t_ccm_temparchive_entity |  | fentryid |

---

## 授信组织-多选基础资料表 t_ccm_temparchive_orgs

- **表名称：** 授信组织-多选基础资料表
- **表名：** t_ccm_temparchive_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_temparchive_orgs_fk |  | fentryid |
| 2 | pk_t_ccm_temparchive_orgs |  | fpkid |

---

## 关联子实体-子表 t_ccm_temp_archive_new_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ccm_temp_archive_new_lk

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
| 1 | pk_ccm_temp_archive_new_lk |  | fpkid |
| 2 | idx_ccm_temp_archive_new_lk_fk |  | fid |

---

## 关联子实体-子表 t_ccm_temparchive_entity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ccm_temparchive_entity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_temparchive_entity_lk |  | fpkid |
| 2 | idx_ccm_temparchive_entity_lk_fk |  | fentryid |

---

## 临时档案设置-多语言表 t_ccm_temparchive_entity_l

- **表名称：** 临时档案设置-多语言表
- **表名：** t_ccm_temparchive_entity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fe_remark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_temparchive_entity_l |  | fpkid |
| 2 | idx_ccm_temparchive_e_l |  | fentryid,flocaleid |

---

## 临时信用档案申请-主表 t_ccm_temp_archive_new

- **表名称：** 临时信用档案申请-主表
- **表名：** t_ccm_temp_archive_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | froletype2 | 维度成员类型2 | varchar | 50 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 8 | froletype3 | 维度成员类型3 | varchar | 50 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | froletype0 | 维度成员类型0 | varchar | 50 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | froletype1 | 维度成员类型1 | varchar | 50 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fdimension | 信控维度 | int8 | 64 |  | √ | 0 | 信控维度 ccm_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_temp_archive_apply_org_dim |  | forgid,fdimension |
| 2 | pk_t_ccm_temp_archive_new |  | fid |

---

## 临时信用档案申请-多语言表 t_ccm_temp_archive_new_l

- **表名称：** 临时信用档案申请-多语言表
- **表名：** t_ccm_temp_archive_new_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_temp_archive_new_l |  | fid,flocaleid |
| 2 | pk_t_ccm_temp_archive_new_l |  | fpkid |

---

## 临时信用档案申请-反写记录表 t_ccm_temp_archive_new_wb

- **表名称：** 临时信用档案申请-反写记录表
- **表名：** t_ccm_temp_archive_new_wb

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
| 1 | idx_ccm_temp_archive_new_wb_fk |  | fid |
| 2 | pk_ccm_temp_archive_new_wb |  | fentryid |
