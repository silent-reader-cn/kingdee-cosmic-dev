# 项目人员薪酬录入-pca_proj_pslsalenter

## 项目人员薪酬录入-主表 t_pca_proj_pslsalenter

- **表名称：** 项目人员薪酬录入-主表
- **表名：** t_pca_proj_pslsalenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fdetailenter | 明细录入 | bpchar | 1 |  | √ | '0' | 明细录入 |
| 7 | fcalorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcostaccount | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_proj_pslsalenter |  | fid |
| 2 | idx_pca_proj_pslsalenter_bno |  | fbillno |
| 3 | idx_pca_proj_pslsalenter_acct |  | fcostaccount,fperiod |

---

## 单据体-子表 t_pca_proj_pslsalenter_e

- **表名称：** 单据体-子表
- **表名：** t_pca_proj_pslsalenter_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallocstatus | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: 0 :未分摊 1 :已分摊 2 :分摊中 |
| 3 | fuiamount | 失业保险 | numeric | 23 | 10 | √ | 0 | 失业保险 |
| 4 | fmeiamount | 医疗保险 | numeric | 23 | 10 | √ | 0 | 医疗保险 |
| 5 | ftotalworkinghours | 本月总工时 | numeric | 23 | 1 |  | null | 本月总工时 |
| 6 | fmaiamount | 生育保险 | numeric | 23 | 10 | √ | 0 | 生育保险 |
| 7 | fpersonal | 人员名称 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsmiamount | 补充医疗 | numeric | 23 | 10 | √ | 0 | 补充医疗 |
| 9 | fhfamount | 住房公积金 | numeric | 23 | 10 | √ | 0 | 住房公积金 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fbenamount | 福利费 | numeric | 23 | 10 | √ | 0 | 福利费 |
| 12 | feiiamount | 工伤保险 | numeric | 23 | 10 | √ | 0 | 工伤保险 |
| 13 | fspiamount | 补充养老 | numeric | 23 | 10 | √ | 0 | 补充养老 |
| 14 | ffiofamount | 五险一金 | numeric | 23 | 10 | √ | 0 | 五险一金 |
| 15 | falloctime | 分摊时间 | timestamp | 0 |  |  | null | 分摊时间 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | feniamount | 养老保险 | numeric | 23 | 10 | √ | 0 | 养老保险 |
| 18 | fsalamount | 工资薪金 | numeric | 23 | 10 | √ | 0 | 工资薪金 |
| 19 | folfamount | 外包劳务费 | numeric | 23 | 10 | √ | 0 | 外包劳务费 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_proj_pslsalenter_e_pk |  | fid |
| 2 | pk_pca_proj_pslsalenter_e |  | fentryid |
