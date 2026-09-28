# 抵消表动态数据-xkcr_dynamicrptdata

## 抵消表动态数据-主表 t_xkcr_dynamicrpt

- **表名称：** 抵消表动态数据-主表
- **表名：** t_xkcr_dynamicrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frptid | 报表 | varchar | 36 |  | √ | ' ' | 合并报表基础 xkcr_rptbase |
| 3 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 4 | fcurrunitid | 金额单位 | int8 | 64 |  | √ | 0 | 金额单位 xkbd_amountunit |
| 5 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 6 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 7 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 13 :合并报表_工作底稿模板 10 :合并报表_个别报表模板 31 :合并报表_抵消表 30 :合并报表_抵消表模板 2 :穿透报表 1 :个别报表 14 :合并报表_汇总报表 17 :合并报表_个别报表 20 :调整报表 3 :报表模板 4 :自定义报表 11 :合并报表_合并报表模板 50 :阿米巴报表模板 16 :合并报表工作底稿 12 :合并报表_汇总报表模板 15 :合并报表_合并报表 |
| 8 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |
| 11 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fsheetid | 表页ID | varchar | 36 |  | √ | ' ' | 表页ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_drpt_frptid |  | frptid |
| 2 | pk_t_xkcr_dynamicrpt |  | fid |

---

## 动态罗列表数据组-子表 t_xkcr_dynamicentry

- **表名称：** 动态罗列表数据组-子表
- **表名：** t_xkcr_dynamicentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | felimtypeid | 抵销类型 | int8 | 64 |  | √ | 0 | 抵销类型 xkcr_eliminationtype |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ftranstypeid | 交易种类 | int8 | 64 |  | √ | 0 | 交易类型 xkcr_transactiontype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_dynamicentry |  | fentryid |
| 2 | idx_xkcr_dentry_fid |  | fid |

---

## 项目数据-子表 t_xkcr_dynamicitemdata

- **表名称：** 项目数据-子表
- **表名：** t_xkcr_dynamicitemdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 2 | fitemvalue | 值 | numeric | 23 | 10 | √ | 0 | 值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdatadirect | 取数方 | int4 | 32 |  | √ | 0 | 取数方 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fitemid | 报表项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkcr_dynamicitemdata |  | fdetailid |
| 2 | idx_xkcr_ditemdata_fentryid |  | fentryid |

---

## 维度数据-子表 t_xkcr_dynamicdimedata

- **表名称：** 维度数据-子表
- **表名：** t_xkcr_dynamicdimedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimebaseid | 基础资料ID | varchar | 50 |  | √ | ' ' | 基础资料ID |
| 2 | fdimename | 名称 | varchar | 2000 |  | √ | ' ' | 名称 |
| 3 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_dimedata_fentryid |  | fentryid |
| 2 | pk_t_xkcr_dynamicdimedata |  | fdetailid |
