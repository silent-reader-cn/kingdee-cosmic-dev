# 信用档案申请-ccm_archive_apply_new

## 信用档案设置-子表 t_ccm_archive_apply_entry

- **表名称：** 信用档案设置-子表
- **表名：** t_ccm_archive_apply_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 信用数量 | numeric | 23 | 10 | √ | 0 | 信用数量 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | farchiveid | 档案ID | int8 | 64 |  | √ | 0 | 档案ID |
| 5 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 6 | fprivilegeamt | 特批总额 | numeric | 23 | 10 | √ | 0 | 特批总额 |
| 7 | fsinglecurcontrol | 币别隔离 | bpchar | 1 |  | √ | ' ' | 币别隔离 |
| 8 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foverdueamt | 逾期额度 | numeric | 23 | 10 | √ | 0 | 逾期额度 |
| 11 | fprivilegeday | 特批天数 | int8 | 64 |  | √ | 0 | 特批天数 |
| 12 | fquota | 信用额度 | numeric | 23 | 10 | √ | 0 | 信用额度 |
| 13 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fchecktypelist | 信用控制形式 | varchar | 100 |  | √ | ' ' | 信用控制形式 |
| 15 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fscheme | 信用控制方案 | int8 | 64 |  | √ | 0 | 信用控制方案 ccm_schemes |
| 19 | farchiveids | 档案ID列表 | varchar | 200 |  | √ | ' ' | 档案ID列表 |
| 20 | fday | 信用天数 | int8 | 64 |  | √ | 0 | 信用天数 |
| 21 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fgrade | 信用等级 | int8 | 64 |  | √ | 0 | 信用等级 ccm_grade |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_apply_entry_archive |  | farchiveid |
| 2 | pk_t_ccm_archive_apply_entry |  | fentryid |

---

## 信用档案设置-多语言表 t_ccm_archive_apply_entry_l

- **表名称：** 信用档案设置-多语言表
- **表名：** t_ccm_archive_apply_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
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
| 1 | pk_t_ccm_archive_apply_entry_l |  | fpkid |
| 2 | idx_ccm_archive_apply_entry_l |  | fentryid,flocaleid |

---

## 额度共享范围分录-子表 t_ccm_archive_apply_share

- **表名称：** 额度共享范围分录-子表
- **表名：** t_ccm_archive_apply_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgfield | 授信组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_archive_apply_share |  | fentryid |
| 2 | idx_apply_share_org |  | forgfield |

---

## 信用档案申请-主表 t_ccm_archive_apply_new

- **表名称：** 信用档案申请-主表
- **表名：** t_ccm_archive_apply_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgscope | 控制组织范围 | varchar | 50 |  | √ | ' ' | 控制组织范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 7 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | froletype2 | 维度成员类型2 | varchar | 50 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 9 | froletype3 | 维度成员类型3 | varchar | 50 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | froletype0 | 维度成员类型0 | varchar | 50 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | froletype1 | 维度成员类型1 | varchar | 50 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fupgradedata | 是否升级数据 | bpchar | 1 |  | √ | ' ' | 是否升级数据 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fdimension | 信控维度 | int8 | 64 |  | √ | 0 | 信控维度 ccm_dimension |
| 19 | fshareorgname | 授信组织名称 | varchar | 50 |  | √ | ' ' | 授信组织名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_apply_org_dim |  | fdimension,forgid |
| 2 | pk_t_ccm_archive_apply_new |  | fid |
