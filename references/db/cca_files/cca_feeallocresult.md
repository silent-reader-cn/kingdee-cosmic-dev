# 费用分配结果-cca_feeallocresult

## 费用分配结果-主表 t_cca_feeallocresult

- **表名称：** 费用分配结果-主表
- **表名：** t_cca_feeallocresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 12 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 13 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_feeallocresult_m0 |  | fbillno |
| 2 | pk_cca_feeallocresult |  | fid |

---

## 单据体-多语言表 t_cca_feeallocresulte_l

- **表名称：** 单据体-多语言表
- **表名：** t_cca_feeallocresulte_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fruledetailname | 规则信息名称 | varchar | 255 |  | √ | ' ' | 规则信息名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cca_feeallocresulte_l_0 |  | fentryid,flocaleid |
| 2 | pk_cca_feeallocresulte_l |  | fpkid |

---

## 单据体-子表 t_cca_feeallocresulte

- **表名称：** 单据体-子表
- **表名：** t_cca_feeallocresulte

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsendamount | 发送方金额 | numeric | 23 | 10 | √ | 0 | 发送方金额 |
| 3 | fsexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fkeyindicator | 关键指标 | int8 | 64 |  | √ | 0 | [关键指标 cca_keyindicator](../cca_files/cca_keyindicator.md) |
| 5 | fraccountview | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 6 | ftotalamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 7 | fsendrule | 发送方规则 | varchar | 30 |  | √ | ' ' | 发送方规则,枚举: A :成本中心余额 B :固定金额 C :固定比率 |
| 8 | fratio | 固定比率（%） | numeric | 23 | 10 | √ | 0 | 固定比率（%） |
| 9 | fallocrule | 分配规则 | int8 | 64 |  | √ | 0 | [费用分配规则 cca_feeallocrule](../cca_files/cca_feeallocrule.md) |
| 10 | fallocamount | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fscostcenter | 发送方成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 13 | ffixamount | 固定金额 | numeric | 23 | 10 | √ | 0 | 固定金额 |
| 14 | fruledetailnum | 规则信息序号 | int8 | 64 |  | √ | 0 | 规则信息序号 |
| 15 | frcostcenter | 接收方成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 16 | fweight | 权数 | numeric | 23 | 10 | √ | 0 | 权数 |
| 17 | frexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 18 | fstandardvalue | 分配标准值 | numeric | 23 | 10 | √ | 0 | 分配标准值 |
| 19 | fruledetailname | 规则信息名称 | varchar | 255 |  | √ | ' ' | 规则信息名称 |
| 20 | faccountview | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 21 | ftotalvalue | 分配标准总值 | numeric | 23 | 10 | √ | 0 | 分配标准总值 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_feeallocresulte |  | fentryid |
| 2 | idx_cca_feeallocresulte_fk |  | fid |
