# 初始化数据录入-pca_costinit

## 初始化数据录入-主表 t_pca_costinit

- **表名称：** 初始化数据录入-主表
- **表名：** t_pca_costinit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftotalcost | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | 项目核算主体 pca_costaccount |
| 12 | fcostobjectid | 项目核算对象 | int8 | 64 |  | √ | 0 | 项目成本核算对象 pca_costobject |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fisgetleaftask | 是否获取叶子任务节点 | bpchar | 1 |  | √ | '0' | 是否获取叶子任务节点 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costinit_bno |  | fbillno |
| 2 | pk_pca_costinit |  | fid |

---

## 成本要素明细-子表 t_pca_costinitsubentry

- **表名称：** 成本要素明细-子表
- **表名：** t_pca_costinitsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | feleamount | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdeeleamount | 不计入项目成本金额 | numeric | 23 | 10 | √ | 0 | 不计入项目成本金额 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fcostelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costinitsubentry_fk |  | fentryid |
| 2 | pk_pca_costinitsubentry |  | fdetailid |

---

## 初始明细数据-子表 t_pca_costinitentry

- **表名称：** 初始明细数据-子表
- **表名：** t_pca_costinitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeamount | 不计入项目成本金额 | numeric | 23 | 10 | √ | 0 | 不计入项目成本金额 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcostobjectid | 核算对象 | int8 | 64 |  | √ | 0 | 项目成本核算对象 pca_costobject |
| 5 | famount | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costinitentry |  | fentryid |
| 2 | idx_pca_costinitentry_fk |  | fid |
