# 商机登记-mpm_bizopreg

## 竞争对手-多语言表 t_mpm_competentry_l

- **表名称：** 竞争对手-多语言表
- **表名：** t_mpm_competentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcompetition | 竞品 | varchar | 80 |  | √ | ' ' | 竞品 |
| 2 | fcompetstrategy | 竞争策略 | varchar | 200 |  | √ | ' ' | 竞争策略 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fcompetitor | 竞争对手 | varchar | 80 |  | √ | ' ' | 竞争对手 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_competel_fidflid |  | fentryid,flocaleid |
| 2 | pk_mpm_competentry_l |  | fpkid |

---

## 竞争对手-子表 t_mpm_competentry

- **表名称：** 竞争对手-子表
- **表名：** t_mpm_competentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompetition | 竞品 | varchar | 80 |  | √ | ' ' | 竞品 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcompetstrategy | 竞争策略 | varchar | 200 |  | √ | ' ' | 竞争策略 |
| 5 | fcompetitor | 竞争对手 | varchar | 80 |  | √ | ' ' | 竞争对手 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_competentry |  | fentryid |
| 2 | idx_mpm_competentry_fid |  | fid |

---

## 商机登记-多语言表 t_mpm_bizopreg_l

- **表名称：** 商机登记-多语言表
- **表名：** t_mpm_bizopreg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizopname | 商机名称 | varchar | 255 |  | √ | ' ' | 商机名称 |
| 3 | fbizoptrack | 商机跟踪 | varchar | 80 |  | √ | ' ' | 商机跟踪 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_bizopreg_fidflid |  | fid,flocaleid |
| 2 | pk_mpm_bizopreg_l |  | fpkid |

---

## 商机登记-分表 t_mpm_bizopreg_a

- **表名称：** 商机登记-分表
- **表名：** t_mpm_bizopreg_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizopdesc | 商机描述 | text | 0 |  |  | ' ' | 商机描述 |
| 3 | fbizopdesc_tag | 商机描述_详情 | text | 0 |  |  | ' ' | 商机描述_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_bizopreg_a |  | fid |

---

## 商机登记-主表 t_mpm_bizopreg

- **表名称：** 商机登记-主表
- **表名：** t_mpm_bizopreg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisprojectap | 已立项 | bpchar | 1 |  | √ | '0' | 已立项 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fundertakedeptid | 负责部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 6 | fbizopname | 商机名称 | varchar | 80 |  | √ | ' ' | 商机名称 |
| 7 | fconnecter | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdirectorid | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsignamount | 预计签单金额 | numeric | 23 | 10 | √ | 0 | 预计签单金额 |
| 14 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fbiztypeid | 商机类型 | int8 | 64 |  | √ | 0 | 商机类型 mpm_bizoptype |
| 16 | fbizoptrack | 商机跟踪 | varchar | 80 |  | √ | ' ' | 商机跟踪 |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 18 | fcustomertext | 客户 | varchar | 50 |  | √ | ' ' | 客户 |
| 19 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcusadress | 地址 | varchar | 255 |  | √ | ' ' | 地址 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fexpectsigndate | 预计签单日期 | timestamp | 0 |  |  | null | 预计签单日期 |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fsignprob | 成单概率(%) | numeric | 23 | 10 | √ | 0 | 成单概率(%) |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fnewcustomer | 新客户 | bpchar | 1 |  | √ | '0' | 新客户 |
| 30 | ftelephone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 31 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 32 | fbizopdate | 商机日期 | timestamp | 0 |  |  | null | 商机日期 |
| 33 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 35 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | fassocprojectid | 关联项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 37 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 41 | fcustomerid | 客户（隐藏） | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_bizopreg_billno |  | fbillno |
| 2 | pk_mpm_bizopreg |  | fid |

---

## 产品和服务-子表 t_mpm_prdserventry

- **表名称：** 产品和服务-子表
- **表名：** t_mpm_prdserventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | fbizopitem | 商机项 | varchar | 255 |  | √ | ' ' | 商机项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_prdserventry |  | fentryid |
| 2 | idx_mpm_prdserventry_fid |  | fid |

---

## 产品和服务-多语言表 t_mpm_prdserventry_l

- **表名称：** 产品和服务-多语言表
- **表名：** t_mpm_prdserventry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fbizopitem | 商机项 | varchar | 255 |  | √ | ' ' | 商机项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_prdserventry_l |  | fpkid |
| 2 | idx_mpm_prdservel_fidflid |  | fentryid,flocaleid |
