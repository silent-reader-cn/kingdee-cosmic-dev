# 金融产品收入台账-tcvat_fpisa

## 单据体-子表 t_tcvat_fpisa_ent

- **表名称：** 单据体-子表
- **表名：** t_tcvat_fpisa_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffprevenueincltax | 金融商品转让销售额（含税） | numeric | 23 | 10 | √ | 0 | 金融商品转让销售额（含税） |
| 3 | ffpcostincltax | 金融商品转让成本（含税） | numeric | 23 | 10 | √ | 0 | 金融商品转让成本（含税） |
| 4 | floanrevenueexcltax | 贷款服务销售额（不含税） | numeric | 23 | 10 | √ | 0 | 贷款服务销售额（不含税） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffprevenueexcltax | 金融商品转让销售额（不含税） | numeric | 23 | 10 | √ | 0 | 金融商品转让销售额（不含税） |
| 7 | ffpcostexcltax | 金融商品转让成本（不含税） | numeric | 23 | 10 | √ | 0 | 金融商品转让成本（不含税） |
| 8 | ftotalrevenueexcltax | 总销售额（不含税） | numeric | 23 | 10 | √ | 0 | 总销售额（不含税） |
| 9 | ftotalcostexcltax | 总成本（不含税） | numeric | 23 | 10 | √ | 0 | 总成本（不含税） |
| 10 | ftaxexemcode | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 11 | ftotalrevenueincltax | 总销售额（含税） | numeric | 23 | 10 | √ | 0 | 总销售额（含税） |
| 12 | fbeginfpincomeincltax | 期初金融商品转让差价收入（含税） | numeric | 23 | 10 | √ | 0 | 期初金融商品转让差价收入（含税） |
| 13 | fperiodfpincomeexcltax | 本月金融商品转让差价收入（不含税） | numeric | 23 | 10 | √ | 0 | 本月金融商品转让差价收入（不含税） |
| 14 | fperiodfpincomeincltax | 本月金融商品转让差价收入（含税） | numeric | 23 | 10 | √ | 0 | 本月金融商品转让差价收入（含税） |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fincometype | 收入类型 | varchar | 50 |  | √ | ' ' | 收入类型,枚举: mssr :免税收入 yssr :应税收入 |
| 17 | floanrevenueincltax | 贷款服务销售额（含税） | numeric | 23 | 10 | √ | 0 | 贷款服务销售额（含税） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_fpisa_ent |  | fentryid |
| 2 | idx_tcvat_fpisa_ent_fk |  | fid |

---

## 金融产品收入台账-主表 t_tcvat_fpisa

- **表名称：** 金融产品收入台账-主表
- **表名：** t_tcvat_fpisa

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodto | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: import :引入 |
| 11 | fbillno | 台账编号 | varchar | 30 |  | √ | ' ' | 台账编号 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fperiodfrom | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_fpisa_org_sq |  | forgid,fperiodfrom,fperiodto |
| 2 | pk_tcvat_fpisa |  | fid |
