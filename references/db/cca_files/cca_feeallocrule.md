# 费用分配规则-cca_feeallocrule

## 子单据体-子表 t_cca_feeallocruleweight

- **表名称：** 子单据体-子表
- **表名：** t_cca_feeallocruleweight

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fweight | 权重 | numeric | 23 | 10 | √ | 0 | 权重 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fdcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_feeallocruleweight_fk |  | fentryid |
| 2 | pk_cca_feeallocruleweight |  | fdetailid |

---

## 会计科目-多选基础资料表 t_cca_feeallocruleav

- **表名称：** 会计科目-多选基础资料表
- **表名：** t_cca_feeallocruleav

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_feeallocruleav |  | fpkid |
| 2 | idx_cca_feeallocruleav_fk |  | fentryid |

---

## 单据体-子表 t_cca_feeallocruleentry

- **表名称：** 单据体-子表
- **表名：** t_cca_feeallocruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcaccountview | 综合会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 3 | fkeyindicator | 关键指标 | int8 | 64 |  | √ | 0 | [关键指标 cca_keyindicator](../cca_files/cca_keyindicator.md) |
| 4 | fdetailname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fsendrule | 发送方规则 | varchar | 30 |  | √ | ' ' | 发送方规则,枚举: A :成本中心余额 B :固定金额 C :固定比率 |
| 6 | fratio | 比率 | numeric | 23 | 10 | √ | 0 | 比率 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fsendcostcentertype | 发送方成本中心类型 | varchar | 50 |  | √ | ' ' | 发送方成本中心类型,枚举: 1 :管理 2 :研发 3 :销售 4 :基本生产 5 :辅助生产 6 :采购 7 :委外 |
| 10 | fcexpenseitem | 综合费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 11 | frcostcentertype | 接收方成本中心类型 | varchar | 50 |  | √ | ' ' | 接收方成本中心类型,枚举: 1 :管理 2 :研发 3 :销售 4 :基本生产 5 :辅助生产 6 :采购 7 :委外 |
| 12 | fnum | 执行顺序 | int8 | 64 |  | √ | 0 | 执行顺序 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_feeallocruleentry |  | fentryid |
| 2 | idx_cca_feeallocruleentry_fk |  | fid |

---

## 费用分配规则-多语言表 t_cca_feeallocrule_l

- **表名称：** 费用分配规则-多语言表
- **表名：** t_cca_feeallocrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_feeallocrule_l |  | fpkid |
| 2 | idx_cca_feeallocrule_l_0 |  | fid,flocaleid |

---

## 接收方成本中心-多选基础资料表 t_cca_feeallocrulerc

- **表名称：** 接收方成本中心-多选基础资料表
- **表名：** t_cca_feeallocrulerc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_feeallocrulerc |  | fpkid |
| 2 | idx_cca_feeallocrulerc_fk |  | fentryid |

---

## 费用项目-多选基础资料表 t_cca_feeallocruleei

- **表名称：** 费用项目-多选基础资料表
- **表名：** t_cca_feeallocruleei

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_feeallocruleei_fk |  | fentryid |
| 2 | pk_cca_feeallocruleei |  | fpkid |

---

## 单据体-多语言表 t_cca_feeallocruleentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_cca_feeallocruleentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
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
| 1 | pk_cca_feeallocruleentry_l |  | fpkid |
| 2 | idx_cca_feeallocruleentry_l_0 |  | fentryid,flocaleid |

---

## 费用分配规则-主表 t_cca_feeallocrule

- **表名称：** 费用分配规则-主表
- **表名：** t_cca_feeallocrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fcalorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | falloctype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: FX :分项 ZH :综合 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnum | fnum | int4 | 32 |  | √ | 0 |  |
| 12 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 17 | fsenderalloc | 发送方参与分配 | bpchar | 1 |  | √ | '0' | 发送方参与分配 |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 分配规则编码 | varchar | 255 |  | √ | ' ' | 分配规则编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_feeallocrule_m0 |  | fmasterid |
| 2 | pk_cca_feeallocrule |  | fid |

---

## 发送方成本中心-多选基础资料表 t_cca_feeallocrulesc

- **表名称：** 发送方成本中心-多选基础资料表
- **表名：** t_cca_feeallocrulesc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_feeallocrulesc_fk |  | fentryid |
| 2 | pk_cca_feeallocrulesc |  | fpkid |
