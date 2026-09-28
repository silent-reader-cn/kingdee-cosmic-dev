# 销售预测单-diif_salforecast

## 销售预测单-主表 t_diif_salforecast

- **表名称：** 销售预测单-主表
- **表名：** t_diif_salforecast

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 3 | fcustomdimname | 自定义维度名称 | varchar | 50 |  | √ | ' ' | 自定义维度名称 |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcustid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 6 | fcycleunit | 预测周期单位 | varchar | 50 |  | √ | ' ' | 预测周期单位,枚举: MONTH :月 WEEK :周 DAY :日 |
| 7 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 8 | fmaterialdim | 物料维度 | varchar | 50 |  | √ | ' ' | 物料维度 |
| 9 | frefhistorycyclecount | 参考历史周期数 | int4 | 32 |  | √ | 0 | 参考历史周期数 |
| 10 | fcustgroupid | 客户分类 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 11 | fusepromodel | 是否启用智能销售预测模型 | bpchar | 1 |  | √ | '0' | 是否启用智能销售预测模型 |
| 12 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcustomdimbasetype | 自定义维度类型 | varchar | 50 |  | √ | ' ' | 自定义维度类型,枚举: bd_tpl :基础数据模板 |
| 16 | fforecastcycle | 预测运算周期 | varchar | 50 |  | √ | ' ' | 预测运算周期 |
| 17 | fcyclecount | 预测周期数 | int4 | 32 |  | √ | 0 | 预测周期数 |
| 18 | fcustombaseid | 自定义维度 | int8 | 64 |  | √ | 0 | 基础数据模板 bd_tpl |
| 19 | fbillno | 预测单编号 | varchar | 30 |  | √ | ' ' | 预测单编号 |
| 20 | fschemebillno | 预测方案编号 | varchar | 30 |  | √ | ' ' | 预测方案编号 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 23 | fresponsibleid | 责任人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fforecastdim | 预测对象 | varchar | 50 |  | √ | ' ' | 预测对象 |
| 28 | fpricescheme | 取价方案 | varchar | 50 |  | √ | ' ' | 取价方案,枚举: LATESTPRICE :最新含税单价 PRICEBILL :价目表含税单价 |
| 29 | fschemename | 预测方案名称 | varchar | 50 |  | √ | ' ' | 预测方案名称 |
| 30 | fforecastdate | 预测日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 预测日期 |
| 31 | fresponsiblevisible | 预测单仅责任人可见 | bpchar | 1 |  | √ | '0' | 预测单仅责任人可见 |
| 32 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_salforecast |  | fid |
| 2 | idx_diif_salforecast_billno |  | fbillno |

---

## 明细信息-分表 t_diif_salforecastentry_h

- **表名称：** 明细信息-分表
- **表名：** t_diif_salforecastentry_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhqty1 | 历史数量1 | numeric | 23 | 10 | √ | 0 | 历史数量1 |
| 3 | fhqty2 | 历史数量2 | numeric | 23 | 10 | √ | 0 | 历史数量2 |
| 4 | fhqty3 | 历史数量3 | numeric | 23 | 10 | √ | 0 | 历史数量3 |
| 5 | fhamount15 | 历史金额15 | numeric | 23 | 10 | √ | 0 | 历史金额15 |
| 6 | fhamount14 | 历史金额14 | numeric | 23 | 10 | √ | 0 | 历史金额14 |
| 7 | fhamount13 | 历史金额13 | numeric | 23 | 10 | √ | 0 | 历史金额13 |
| 8 | fhamount12 | 历史金额12 | numeric | 23 | 10 | √ | 0 | 历史金额12 |
| 9 | fhamount11 | 历史金额11 | numeric | 23 | 10 | √ | 0 | 历史金额11 |
| 10 | fhamount10 | 历史金额10 | numeric | 23 | 10 | √ | 0 | 历史金额10 |
| 11 | fhamount8 | 历史金额8 | numeric | 23 | 10 | √ | 0 | 历史金额8 |
| 12 | fhamount9 | 历史金额9 | numeric | 23 | 10 | √ | 0 | 历史金额9 |
| 13 | fhamount6 | 历史金额6 | numeric | 23 | 10 | √ | 0 | 历史金额6 |
| 14 | fhamount7 | 历史金额7 | numeric | 23 | 10 | √ | 0 | 历史金额7 |
| 15 | fhamount4 | 历史金额4 | numeric | 23 | 10 | √ | 0 | 历史金额4 |
| 16 | fhamount5 | 历史金额5 | numeric | 23 | 10 | √ | 0 | 历史金额5 |
| 17 | fhamount2 | 历史金额2 | numeric | 23 | 10 | √ | 0 | 历史金额2 |
| 18 | fhamount3 | 历史金额3 | numeric | 23 | 10 | √ | 0 | 历史金额3 |
| 19 | fhamount1 | 历史金额1 | numeric | 23 | 10 | √ | 0 | 历史金额1 |
| 20 | fhqty10 | 历史数量10 | numeric | 23 | 10 | √ | 0 | 历史数量10 |
| 21 | fhqty13 | 历史数量13 | numeric | 23 | 10 | √ | 0 | 历史数量13 |
| 22 | fhqty14 | 历史数量14 | numeric | 23 | 10 | √ | 0 | 历史数量14 |
| 23 | fhqty11 | 历史数量11 | numeric | 23 | 10 | √ | 0 | 历史数量11 |
| 24 | fhqty12 | 历史数量12 | numeric | 23 | 10 | √ | 0 | 历史数量12 |
| 25 | fhqty8 | 历史数量8 | numeric | 23 | 10 | √ | 0 | 历史数量8 |
| 26 | fhqty9 | 历史数量9 | numeric | 23 | 10 | √ | 0 | 历史数量9 |
| 27 | fhqty15 | 历史数量15 | numeric | 23 | 10 | √ | 0 | 历史数量15 |
| 28 | fhqty4 | 历史数量4 | numeric | 23 | 10 | √ | 0 | 历史数量4 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fhqty5 | 历史数量5 | numeric | 23 | 10 | √ | 0 | 历史数量5 |
| 31 | fhqty6 | 历史数量6 | numeric | 23 | 10 | √ | 0 | 历史数量6 |
| 32 | fhqty7 | 历史数量7 | numeric | 23 | 10 | √ | 0 | 历史数量7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_salforecastentry_h |  | fentryid |
| 2 | idx_diif_forecastentry_h |  | fid |

---

## 明细信息-子表 t_diif_salforecastentry

- **表名称：** 明细信息-子表
- **表名：** t_diif_salforecastentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | falgorithm | 预测模型 | varchar | 50 |  | √ | ' ' | 预测模型,枚举: TE :三重指数平滑算法 MA :移动平均算法 |
| 7 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fprice | 参考单价 | numeric | 23 | 10 | √ | 0 | 参考单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_forecastentry |  | fid |
| 2 | pk_t_diif_salforecastentry |  | fentryid |

---

## 明细信息-分表 t_diif_salforecastentry_f

- **表名称：** 明细信息-分表
- **表名：** t_diif_salforecastentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffamount3 | 预测金额3 | numeric | 23 | 10 | √ | 0 | 预测金额3 |
| 3 | ffamount2 | 预测金额2 | numeric | 23 | 10 | √ | 0 | 预测金额2 |
| 4 | ffamount1 | 预测金额1 | numeric | 23 | 10 | √ | 0 | 预测金额1 |
| 5 | ffamount15 | 预测金额15 | numeric | 23 | 10 | √ | 0 | 预测金额15 |
| 6 | ffamount7 | 预测金额7 | numeric | 23 | 10 | √ | 0 | 预测金额7 |
| 7 | ffamount13 | 预测金额13 | numeric | 23 | 10 | √ | 0 | 预测金额13 |
| 8 | ffamount6 | 预测金额6 | numeric | 23 | 10 | √ | 0 | 预测金额6 |
| 9 | ffamount14 | 预测金额14 | numeric | 23 | 10 | √ | 0 | 预测金额14 |
| 10 | ffamount5 | 预测金额5 | numeric | 23 | 10 | √ | 0 | 预测金额5 |
| 11 | ffamount11 | 预测金额11 | numeric | 23 | 10 | √ | 0 | 预测金额11 |
| 12 | ffamount4 | 预测金额4 | numeric | 23 | 10 | √ | 0 | 预测金额4 |
| 13 | ffamount12 | 预测金额12 | numeric | 23 | 10 | √ | 0 | 预测金额12 |
| 14 | ffamount10 | 预测金额10 | numeric | 23 | 10 | √ | 0 | 预测金额10 |
| 15 | ffqty1 | 预测数量1 | numeric | 23 | 10 | √ | 0 | 预测数量1 |
| 16 | ffqty2 | 预测数量2 | numeric | 23 | 10 | √ | 0 | 预测数量2 |
| 17 | ffqty3 | 预测数量3 | numeric | 23 | 10 | √ | 0 | 预测数量3 |
| 18 | ffqty4 | 预测数量4 | numeric | 23 | 10 | √ | 0 | 预测数量4 |
| 19 | ffqty5 | 预测数量5 | numeric | 23 | 10 | √ | 0 | 预测数量5 |
| 20 | ffqty6 | 预测数量6 | numeric | 23 | 10 | √ | 0 | 预测数量6 |
| 21 | ffqty13 | 预测数量13 | numeric | 23 | 10 | √ | 0 | 预测数量13 |
| 22 | ffqty7 | 预测数量7 | numeric | 23 | 10 | √ | 0 | 预测数量7 |
| 23 | ffqty14 | 预测数量14 | numeric | 23 | 10 | √ | 0 | 预测数量14 |
| 24 | ffqty8 | 预测数量8 | numeric | 23 | 10 | √ | 0 | 预测数量8 |
| 25 | ffqty15 | 预测数量15 | numeric | 23 | 10 | √ | 0 | 预测数量15 |
| 26 | ffqty9 | 预测数量9 | numeric | 23 | 10 | √ | 0 | 预测数量9 |
| 27 | ffamount9 | 预测金额9 | numeric | 23 | 10 | √ | 0 | 预测金额9 |
| 28 | ffamount8 | 预测金额8 | numeric | 23 | 10 | √ | 0 | 预测金额8 |
| 29 | ffqty10 | 预测数量10 | numeric | 23 | 10 | √ | 0 | 预测数量10 |
| 30 | ffqty11 | 预测数量11 | numeric | 23 | 10 | √ | 0 | 预测数量11 |
| 31 | ffqty12 | 预测数量12 | numeric | 23 | 10 | √ | 0 | 预测数量12 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_forecastentry_f |  | fid |
| 2 | pk_t_diif_salforecastentry_f |  | fentryid |

---

## 明细信息-分表 t_diif_salforecastentry_r

- **表名称：** 明细信息-分表
- **表名：** t_diif_salforecastentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frqty3 | 预测记录数量3 | numeric | 23 | 10 | √ | 0 | 预测记录数量3 |
| 3 | frqty2 | 预测记录数量2 | numeric | 23 | 10 | √ | 0 | 预测记录数量2 |
| 4 | frqty5 | 预测记录数量5 | numeric | 23 | 10 | √ | 0 | 预测记录数量5 |
| 5 | frqty4 | 预测记录数量4 | numeric | 23 | 10 | √ | 0 | 预测记录数量4 |
| 6 | frqty7 | 预测记录数量7 | numeric | 23 | 10 | √ | 0 | 预测记录数量7 |
| 7 | frqty6 | 预测记录数量6 | numeric | 23 | 10 | √ | 0 | 预测记录数量6 |
| 8 | frqty9 | 预测记录数量9 | numeric | 23 | 10 | √ | 0 | 预测记录数量9 |
| 9 | frqty8 | 预测记录数量8 | numeric | 23 | 10 | √ | 0 | 预测记录数量8 |
| 10 | framount5 | 预测记录金额5 | numeric | 23 | 10 | √ | 0 | 预测记录金额5 |
| 11 | framount4 | 预测记录金额4 | numeric | 23 | 10 | √ | 0 | 预测记录金额4 |
| 12 | framount7 | 预测记录金额7 | numeric | 23 | 10 | √ | 0 | 预测记录金额7 |
| 13 | framount6 | 预测记录金额6 | numeric | 23 | 10 | √ | 0 | 预测记录金额6 |
| 14 | framount9 | 预测记录金额9 | numeric | 23 | 10 | √ | 0 | 预测记录金额9 |
| 15 | framount8 | 预测记录金额8 | numeric | 23 | 10 | √ | 0 | 预测记录金额8 |
| 16 | frqty1 | 预测记录数量1 | numeric | 23 | 10 | √ | 0 | 预测记录数量1 |
| 17 | framount1 | 预测记录金额1 | numeric | 23 | 10 | √ | 0 | 预测记录金额1 |
| 18 | framount3 | 预测记录金额3 | numeric | 23 | 10 | √ | 0 | 预测记录金额3 |
| 19 | framount2 | 预测记录金额2 | numeric | 23 | 10 | √ | 0 | 预测记录金额2 |
| 20 | framount11 | 预测记录金额11 | numeric | 23 | 10 | √ | 0 | 预测记录金额11 |
| 21 | framount12 | 预测记录金额12 | numeric | 23 | 10 | √ | 0 | 预测记录金额12 |
| 22 | framount13 | 预测记录金额13 | numeric | 23 | 10 | √ | 0 | 预测记录金额13 |
| 23 | framount14 | 预测记录金额14 | numeric | 23 | 10 | √ | 0 | 预测记录金额14 |
| 24 | framount10 | 预测记录金额10 | numeric | 23 | 10 | √ | 0 | 预测记录金额10 |
| 25 | framount15 | 预测记录金额15 | numeric | 23 | 10 | √ | 0 | 预测记录金额15 |
| 26 | frqty11 | 预测记录数量11 | numeric | 23 | 10 | √ | 0 | 预测记录数量11 |
| 27 | frqty12 | 预测记录数量12 | numeric | 23 | 10 | √ | 0 | 预测记录数量12 |
| 28 | frqty10 | 预测记录数量10 | numeric | 23 | 10 | √ | 0 | 预测记录数量10 |
| 29 | frqty15 | 预测记录数量15 | numeric | 23 | 10 | √ | 0 | 预测记录数量15 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 31 | frqty13 | 预测记录数量13 | numeric | 23 | 10 | √ | 0 | 预测记录数量13 |
| 32 | frqty14 | 预测记录数量14 | numeric | 23 | 10 | √ | 0 | 预测记录数量14 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_salforecastentry_r |  | fentryid |
| 2 | idx_diif_salforecastentry_r |  | fid |

---

## 销售预测单-多语言表 t_diif_salforecast_l

- **表名称：** 销售预测单-多语言表
- **表名：** t_diif_salforecast_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_diif_salforecast_l |  | fid,flocaleid |
| 2 | pk_t_diif_salforecast_l |  | fpkid |
