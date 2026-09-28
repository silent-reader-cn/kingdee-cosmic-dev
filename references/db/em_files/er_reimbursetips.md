# 报销提醒设置-er_reimbursetips

## 报销提醒设置-使用范围表 t_er_reimbursetips_u

- **表名称：** 报销提醒设置-使用范围表
- **表名：** t_er_reimbursetips_u

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
| 1 | idx_t_er_reimbursetips_u_uo |  | fuseorgid |
| 2 | t_er_reimbursetips_u_pkey |  | fdataid,fuseorgid |

---

## 报销提醒设置-多语言表 t_er_reimbursetips_l

- **表名称：** 报销提醒设置-多语言表
- **表名：** t_er_reimbursetips_l

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
| 1 | idx_er_reimbursetips_l_fpkid |  | fid |
| 2 | t_er_reimbursetips_l_pkey |  | fpkid |

---

## 报销提醒设置-使用范围位图表 t_er_reimbursetips_m

- **表名称：** 报销提醒设置-使用范围位图表
- **表名：** t_er_reimbursetips_m

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
| 1 | pk_t_er_reimbursetips_m |  | forgid |

---

## 提示信息-多语言表 t_er_tipsinfo_l

- **表名称：** 提示信息-多语言表
- **表名：** t_er_tipsinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulttipscontent | 提示内容 | varchar | 2000 |  | √ | ' ' | 提示内容 |
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
| 1 | pk_t_er_tipsinfo_l |  | fpkid |
| 2 | idx_er_tipsinfo_fid |  | fentryid,flocaleid |

---

## 报销提醒设置-主表 t_er_reimbursetips

- **表名称：** 报销提醒设置-主表
- **表名：** t_er_reimbursetips

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fstatus | 数据状态 | varchar | 25 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 17 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_reimbursetips_createorg |  | fcreateorgid |
| 2 | idx_t_er_reimbursetips_master |  | fmasterid |
| 3 | t_er_reimbursetips_pkey |  | fid |
| 4 | idx_er_reimbursetips_fnum |  | fnumber,fid |
| 5 | idx_er_reimbursetips_fname |  | fname |

---

## 提示信息-子表 t_er_tipsinfo

- **表名称：** 提示信息-子表
- **表名：** t_er_tipsinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisdefaultshow | 默认展开 | bpchar | 1 |  | √ | ' ' | 默认展开 |
| 3 | fmulttipscontent | fmulttipscontent | varchar | 2000 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftipscontent | 提醒信息(废弃) | varchar | 500 |  | √ | ' ' | 提醒信息(废弃) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbilltype | 单据 | varchar | 50 |  | √ | ' ' | 单据,枚举: er_tripreimbursebill :差旅报销单 er_tripreimbill_grid :差旅报销单（表） er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_tripreqbill :出差申请单 er_tripreqbill_loan :出差申请单（借） er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_repaymentbill :还款单 er_dailyreimbursebill_B :移动话费报销单 er_dailyreimbursebill_A :额度报销单 er_applyprojectbill :立项单 er_contractbill :合同台账 er_costestimatebill :费用暂估 er_prepaybill :预付单 er_withholdingbill :费用预提单 er_costestimateassetbill :资产暂估 er_publicreimbursebill_asset :资产报账单 er_dailyapplybill_meetting :会议费申请单(分录) er_dailyapplybill_entertainment :招待费申请单(分录) er_publicreimbursebill_meetting :会议费报销单(分录) er_publicreimbursebill_entertainment :招待费报销单(分录) er_dailyapplybill_meetting_bill :会议费申请单 er_dailyapplybill_entertainment_bill :招待费申请单 er_dailyreimbursebill_meetting_bill :会议费报销单 er_dailyreimbursebill_entertainment_bill :招待费报销单 er_tripreimburse_cardgrid_DomesticTravel :国内差旅报销 er_tripreimburse_cardgrid_InternationalTravel :国际差旅报销 er_tripreqbill_inter :出差申请单(全球) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_tipsinfo_pkey |  | fentryid |
| 2 | idx_er_tipsinfo_fseq |  | fid,fseq |
