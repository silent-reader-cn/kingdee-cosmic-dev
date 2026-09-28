# 房地产开发企业特定业务台账-tccit_spec_bus_real_dev

## 纳税调整额-子表 t_tccit_spec_bus_nstz

- **表名称：** 纳税调整额-子表
- **表名：** t_tccit_spec_bus_nstz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspecbusrealdevnstz | 房地产开发企业特定业务计算的纳税调整额 | numeric | 23 | 10 | √ | 0 | 房地产开发企业特定业务计算的纳税调整额 |
| 3 | fsalenofinishnstz | 销售未完工开发产品特定业务计算的纳税调整额 | numeric | 23 | 10 | √ | 0 | 销售未完工开发产品特定业务计算的纳税调整额 |
| 4 | fsalefinishnstz | 销售的未完工产品转完工产品特定业务计算的纳税调整额 | numeric | 23 | 10 | √ | 0 | 销售的未完工产品转完工产品特定业务计算的纳税调整额 |
| 5 | fperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_spec_bus_nstz |  | fentryid |
| 2 | idx_tccit_spec_bus_nstz_fk |  | fid |

---

## 房地产开发企业特定业务台账-主表 t_tccit_spec_bus_real_dev

- **表名称：** 房地产开发企业特定业务台账-主表
- **表名：** t_tccit_spec_bus_real_dev

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 房地产项目编号 | varchar | 50 |  | √ | ' ' | 房地产项目编号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fitemname | 房地产项目名称 | varchar | 100 |  | √ | ' ' | 房地产项目名称 |
| 11 | fsbtype | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: yj :预缴 hj :汇算清缴 |
| 12 | fbillno | 台账编号 | varchar | 30 |  | √ | ' ' | 台账编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_spec_bus_real_dev |  | fid |
| 2 | idx_t_tccit_sbrd_fbillno |  | fbillno |

---

## 销售的未完工产品转完工产品特定业务台账-子表 t_tccit_sale_finish_e

- **表名称：** 销售的未完工产品转完工产品特定业务台账-子表
- **表名：** t_tccit_sale_finish_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsalefinishincome | 销售未完工产品转完工产品确认的销售收入 | numeric | 23 | 10 | √ | 0 | 销售未完工产品转完工产品确认的销售收入 |
| 3 | ffinishperiodstart | 起 | timestamp | 0 |  |  | null | 起 |
| 4 | ffinishperiodend | 止 | timestamp | 0 |  |  | null | 止 |
| 5 | ffinishrate | 预计计税毛利率 | numeric | 23 | 10 | √ | 0 | 预计计税毛利率 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffinishnstz | 当期纳税调整额 | numeric | 23 | 10 | √ | 0 | 当期纳税调整额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fzhsjfsdtaxincome | 转回实际发生的营业税金及附加、土地增值税 | numeric | 23 | 10 | √ | 0 | 转回实际发生的营业税金及附加、土地增值税 |
| 10 | ffinishprofit | 转回的销售未完工产品预计毛利额 | numeric | 23 | 10 | √ | 0 | 转回的销售未完工产品预计毛利额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_sale_finish_e_fk |  | fid |
| 2 | pk_tccit_sale_finish_e |  | fentryid |

---

## 销售未完工开发产品特定业务台账-子表 t_tccit_sale_no_finish_e

- **表名称：** 销售未完工开发产品特定业务台账-子表
- **表名：** t_tccit_sale_no_finish_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnofinishperiodend | 止 | timestamp | 0 |  |  | null | 止 |
| 3 | fnofinishnstz | 当期纳税调整额 | numeric | 23 | 10 | √ | 0 | 当期纳税调整额 |
| 4 | fsjfsdtaxincome | 实际发生的营业税金及附加、土地增值税 | numeric | 23 | 10 | √ | 0 | 实际发生的营业税金及附加、土地增值税 |
| 5 | fsalenofinishincome | 销售未完工产品的收入 | numeric | 23 | 10 | √ | 0 | 销售未完工产品的收入 |
| 6 | fnofinishprofit | 销售未完工产品预计毛利额 | numeric | 23 | 10 | √ | 0 | 销售未完工产品预计毛利额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnofinishrate | 预计计税毛利率 | numeric | 23 | 10 | √ | 0 | 预计计税毛利率 |
| 9 | fnofinishperiodstart | 起 | timestamp | 0 |  |  | null | 起 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_sale_no_finish_e_fk |  | fid |
| 2 | pk_tccit_sale_no_finish_e |  | fentryid |
