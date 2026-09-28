# 项目人员薪酬分摊单-rdem_psl_alloc_result

## 项目人员薪酬分摊单-主表 t_pca_pslalloc_result

- **表名称：** 项目人员薪酬分摊单-主表
- **表名：** t_pca_pslalloc_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcostaccount | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 12 | fisvoucher | 是否已生成凭证 | bpchar | 1 |  | √ | '0' | 是否已生成凭证 |
| 13 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_pslalloc_result |  | fid |
| 2 | idx_pca_pslalloc_result_bno |  | fbillno |

---

## 单据体-子表 t_pca_pslalloc_result_e

- **表名称：** 单据体-子表
- **表名：** t_pca_pslalloc_result_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuiamount | 失业保险 | numeric | 23 | 10 | √ | 0 | 失业保险 |
| 3 | ftotalamount | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 4 | fpersonal | 人员名称 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fhfamount | 住房公积金 | numeric | 23 | 10 | √ | 0 | 住房公积金 |
| 6 | fsmiamount | 补充医疗 | numeric | 23 | 10 | √ | 0 | 补充医疗 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbenamount | 福利费 | numeric | 23 | 10 | √ | 0 | 福利费 |
| 9 | fcostelement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 10 | ffiofamount | 五险一金 | numeric | 23 | 10 | √ | 0 | 五险一金 |
| 11 | fcostobject | 核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 12 | fmodifierfield1 | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcostsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 14 | fmeiamount | 医疗保险 | numeric | 23 | 10 | √ | 0 | 医疗保险 |
| 15 | fmaiamount | 生育保险 | numeric | 23 | 10 | √ | 0 | 生育保险 |
| 16 | freporthours | 汇报工时 | numeric | 23 | 1 |  | null | 汇报工时 |
| 17 | fmodifydatefield1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fbillnumber | 来源单据号 | varchar | 50 |  | √ | ' ' | 来源单据号 |
| 19 | feiiamount | 工伤保险 | numeric | 23 | 10 | √ | 0 | 工伤保险 |
| 20 | fspiamount | 补充养老 | numeric | 23 | 10 | √ | 0 | 补充养老 |
| 21 | ffromentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fsalamount | 工资薪金 | numeric | 23 | 10 | √ | 0 | 工资薪金 |
| 24 | feniamount | 养老保险 | numeric | 23 | 10 | √ | 0 | 养老保险 |
| 25 | folfamount | 外包劳务费 | numeric | 23 | 10 | √ | 0 | 外包劳务费 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_pslalloc_result_e |  | fentryid |
| 2 | idx_pca_pslalloc_result_e_pk |  | fid |
