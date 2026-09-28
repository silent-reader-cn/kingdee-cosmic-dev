# 映射差旅项目-er_rel_tripitem_ratetype

## 映射差旅项目-使用范围位图表 t_er_rel_exp_ratetype_m

- **表名称：** 映射差旅项目-使用范围位图表
- **表名：** t_er_rel_exp_ratetype_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_rel_exp_ratetype_m |  | forgid |

---

## 映射差旅项目-多语言表 t_er_rel_exp_ratetype_l

- **表名称：** 映射差旅项目-多语言表
- **表名：** t_er_rel_exp_ratetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rlexprattype_l_flocid |  | fid,flocaleid |
| 2 | t_er_rel_exp_ratetype_l_pkey |  | fpkid |

---

## 映射差旅项目-使用范围表 t_er_rel_exp_ratetype_u

- **表名称：** 映射差旅项目-使用范围表
- **表名：** t_er_rel_exp_ratetype_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_rel_exp_ratetype_u_uo |  | fuseorgid |
| 2 | t_er_rel_exp_ratetype_u_pkey |  | fdataid,fuseorgid |

---

## 映射差旅项目-主表 t_er_rel_exp_ratetype

- **表名称：** 映射差旅项目-主表
- **表名：** t_er_rel_exp_ratetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcompany | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftripitemid | 差旅项目 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fratetypecode | fratetypecode | varchar | 80 |  | √ | ' ' |  |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdescription | 事由 | varchar | 255 |  | √ | ' ' | 事由 |
| 19 | freimbursetype | 报账类型 | varchar | 30 |  | √ | ' ' | 报账类型,枚举: expense :费用报账 entertainment :招待费 meetting :会议费 otherexpenses :其他 |
| 20 | finvoicetypef7 | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 21 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 23 | fratetypeid | 税收分类编码 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 24 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | frelbilltype | 单据类型 | varchar | 10 |  | √ | ' ' | 单据类型,枚举: 2 :差旅报销单 1 :费用报销单 3 :对公报销单 4 :全球差旅报销单 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fbilltype | 映射类型 | varchar | 10 |  | √ | '1' | 映射类型,枚举: 1 :费用项目 2 :差旅项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_rel_exp_ratetype_pkey |  | fid |
| 2 | idx_t_er_rel_exp_ratetype_createorg |  | fcreateorgid |
| 3 | idx_t_er_rel_exp_ratetype_master |  | fmasterid |
| 4 | idx_er_relexp_ratyp_ratypid |  | fratetypeid |
| 5 | idx_er_relexp_ratyp_orgid |  | forgid |
| 6 | idx_er_relexp_ratyp_expid |  | fexpenseitemid |

---

## 其他发票因素-子表 t_er_namerflitem

- **表名称：** 其他发票因素-子表
- **表名：** t_er_namerflitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapfactor | 录入映射因素 | varchar | 255 |  | √ | ' ' | 录入映射因素 |
| 3 | finvoicefactor | 发票因素 | varchar | 50 |  | √ | ' ' | 发票因素,枚举: inv_ext_goodnames :商品名称 inv_ext_buyerorgname :收票公司 inv_ext_startcity :出发城市 inv_ext_destcity :目的城市 |
| 4 | fgoodnames | 商品名称（废弃） | varchar | 255 |  | √ | ' ' | 商品名称（废弃） |
| 5 | fmappingtype | 匹配方式 | bpchar | 1 |  | √ | '0' | 匹配方式,枚举: 0 :完全匹配 1 :模糊匹配 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_namerflitem_pkey |  | fentryid |
| 2 | idx_namerflitem_factor |  | fmappingtype,finvoicefactor,fmapfactor |
| 3 | idx_fid |  | fid |
| 4 | idx_namerflitem_gn |  | fgoodnames |

---

## 费用项目范围-子表 t_er_expenseitemrange

- **表名称：** 费用项目范围-子表
- **表名：** t_er_expenseitemrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryexpenseitem | 费用项目编码 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fentrytripitem | 差旅项目编码 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 6 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_expenseitemrange |  | fentryid |
| 2 | idx_er_expenseitemrange_fid |  | fid |
