# 收函登记-gm_receiveletter

## 收函登记-关联追踪表 t_gm_receiveletter_tc

- **表名称：** 收函登记-关联追踪表
- **表名：** t_gm_receiveletter_tc

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
| 1 | pk_gm_receiveletter_tc |  | fid |
| 2 | idx_gm_receiveletter_tc_tbill |  | ftbillid |
| 3 | idx_gm_receiveletter_tc_tid |  | ftid |

---

## 关联子实体-子表 t_gm_receiveletter_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gm_receiveletter_lk

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
| 1 | idx_gm_receiveletter_lk_fk |  | fid |
| 2 | pk_gm_receiveletter_lk |  | fpkid |

---

## 收函登记-主表 t_gm_receiveletter

- **表名称：** 收函登记-主表
- **表名：** t_gm_receiveletter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: registering :登记中 registered :已登记 claimed :已索赔 cancelled :已注销 |
| 4 | flettertype | 开函人类型 | varchar | 30 |  | √ | ' ' | 开函人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_user :职员 other :其他 |
| 5 | famount | 保函金额 | numeric | 19 | 6 | √ | 0 | 保函金额 |
| 6 | fguaranteeterm | 保函期限 | varchar | 30 |  | √ | ' ' | 保函期限 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fguaranteetypeid | 保函类型 | int8 | 64 |  | √ | 0 | [保函类型 gm_guaranteetype](../gm_files/gm_guaranteetype.md) |
| 9 | fguaranteevarietyid | 保函品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fclaimdate | 索赔日期 | timestamp | 0 |  |  | null | 索赔日期 |
| 12 | fexpiredate | 开函到期日 | timestamp | 0 |  |  | null | 开函到期日 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | frecbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 16 | fsourcebilltype | 源单类型 | varchar | 80 |  | √ | ' ' | 源单类型,枚举: 开函登记 :gm_letterofguarantee |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fguaranteepurpose | 保函用途 | varchar | 255 |  | √ | ' ' | 保函用途 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 22 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 24 | ftextletter | 开函人 | varchar | 80 |  | √ | ' ' | 开函人 |
| 25 | feassrcid | eas数据id | varchar | 50 |  | √ | ' ' | eas数据id |
| 26 | frecorgid | 被担保人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fstartdate | 开函起始日 | timestamp | 0 |  |  | null | 开函起始日 |
| 28 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 29 | fcanceldate | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 30 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 31 | fguaranteeno | 保函编号 | varchar | 255 |  | √ | ' ' | 保函编号 |
| 32 | fletterid | 开函人id | int8 | 64 |  | √ | 0 | 开函人id |
| 33 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 other :其他 none :信用/无担保 |
| 34 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | ffinorginfoid | 金融机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gm_receivelet_fofgid |  | forgid |
| 2 | pk_t_gm_receiveletter |  | fid |
| 3 | idxt_gm_receivelet_fbillno |  | fbillno |
| 4 | idx_gm_receivelet_feassrcid |  | feassrcid |

---

## 收函登记-反写记录表 t_gm_receiveletter_wb

- **表名称：** 收函登记-反写记录表
- **表名：** t_gm_receiveletter_wb

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
| 1 | pk_gm_receiveletter_wb |  | fentryid |
| 2 | idx_gm_receiveletter_wb_fk |  | fid |

---

## 收函登记-多语言表 t_gm_receiveletter_l

- **表名称：** 收函登记-多语言表
- **表名：** t_gm_receiveletter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gm_receiveletl_fid |  | fid |
| 2 | pk_t_gm_receiveletter_l |  | fpkid |
