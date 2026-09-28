# 信用档案变更单-ccm_xarchive

## 信用档案变更单-反写记录表 t_ccm_xarchive_wb

- **表名称：** 信用档案变更单-反写记录表
- **表名：** t_ccm_xarchive_wb

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
| 1 | idx_ccm_xarchive_wb_fk |  | fid |
| 2 | pk_ccm_xarchive_wb |  | fentryid |

---

## 授信组织-多选基础资料表 t_ccm_xarchive_orgs

- **表名称：** 授信组织-多选基础资料表
- **表名：** t_ccm_xarchive_orgs

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
| 1 | pk_t_ccm_xarchive_orgs |  | fpkid |
| 2 | idx_ccm_xarchive_orgs |  | fentryid,fbasedataid |

---

## 信用档案变更单-多语言表 t_ccm_xarchive_l

- **表名称：** 信用档案变更单-多语言表
- **表名：** t_ccm_xarchive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 变更原因 | varchar | 50 |  | √ | ' ' | 变更原因 |
| 3 | fcomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_xarchive_l |  | fpkid |
| 2 | idx_ccm_xarchive_l_id_local |  | fid,flocaleid |

---

## 信用档案变更单-主表 t_ccm_xarchive

- **表名称：** 信用档案变更单-主表
- **表名：** t_ccm_xarchive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 变更原因 | varchar | 50 |  | √ | ' ' | 变更原因 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | froletype2 | 维度成员类型2 | varchar | 50 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 8 | froletype3 | 维度成员类型3 | varchar | 50 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | froletype0 | 维度成员类型0 | varchar | 50 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | froletype1 | 维度成员类型1 | varchar | 50 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fdimension | 信控维度 | int8 | 64 |  | √ | 0 | 信控维度 ccm_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_xarchive |  | fid |
| 2 | idx_ccm_xarchive_billno |  | fbillno |

---

## 信用档案变更单-关联追踪表 t_ccm_xarchive_tc

- **表名称：** 信用档案变更单-关联追踪表
- **表名：** t_ccm_xarchive_tc

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
| 1 | idx_ccm_xarchive_tc_tbill |  | ftbillid |
| 2 | idx_ccm_xarchive_tc_tid |  | ftid |
| 3 | pk_ccm_xarchive_tc |  | fid |

---

## 关联子实体-子表 t_ccm_xarchive_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ccm_xarchive_lk

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
| 1 | idx_ccm_xarchive_lk_fk |  | fid |
| 2 | pk_ccm_xarchive_lk |  | fpkid |

---

## 变更详情单据体-子表 t_ccm_xarchive_entity

- **表名称：** 变更详情单据体-子表
- **表名：** t_ccm_xarchive_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foldsinglecurcontrol | 原币别隔离 | bpchar | 1 |  | √ | ' ' | 原币别隔离 |
| 3 | fnewsinglecurcontrol | 新币别隔离 | bpchar | 1 |  | √ | ' ' | 新币别隔离 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | foldexratetable | 原汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 6 | fnewexratetable | 新汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 7 | foldassingday | 原信用天数 | int8 | 64 |  | √ | 0 | 原信用天数 |
| 8 | fnewcurrencyfield | 新币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | fnewgrade | 新信用等级 | int8 | 64 |  | √ | 0 | 信用等级 ccm_grade |
| 11 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fnewformula | 新信用额度 | numeric | 23 | 10 | √ | 0 | 新信用额度 |
| 14 | fnewassingday | 新信用天数 | int8 | 64 |  | √ | 0 | 新信用天数 |
| 15 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | foldscheme | 原信控方案 | int8 | 64 |  | √ | 0 | 信用控制方案 ccm_schemes |
| 17 | fnewassingbalance | 新逾期额度 | numeric | 23 | 10 | √ | 0 | 新逾期额度 |
| 18 | fnewcheckstatus | 新信用检查状态 | varchar | 50 |  | √ | ' ' | 新信用检查状态,枚举: CHECKED :正常检查 UNCHECKED :信用免检 |
| 19 | foldassingbalance | 原逾期额度 | numeric | 23 | 10 | √ | 0 | 原逾期额度 |
| 20 | forgscope | 控制范围 | varchar | 50 |  | √ | ' ' | 控制范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 21 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | foldformula | 原信用额度 | numeric | 23 | 10 | √ | 0 | 原信用额度 |
| 23 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 24 | foldcurrencyfield | 原币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fentrycomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 26 | fnewscheme | 新信控方案 | int8 | 64 |  | √ | 0 | 信用控制方案 ccm_schemes |
| 27 | foldgrade | 原信用等级 | int8 | 64 |  | √ | 0 | 信用等级 ccm_grade |
| 28 | foldcheckstatus | 原信用检查状态 | varchar | 50 |  | √ | ' ' | 原信用检查状态,枚举: CHECKED :正常检查 UNCHECKED :信用免检 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_xarchive_e_fid |  | fid |
| 2 | pk_ccm_xarchive_entity |  | fentryid |

---

## 关联子实体-子表 t_ccm_xarchive_entity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ccm_xarchive_entity_lk

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
| 1 | pk_ccm_xarchive_entity_lk |  | fpkid |
| 2 | idx_ccm_xarchive_entity_lk_fk |  | fentryid |
