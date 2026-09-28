# 采购预测单-mrp_pur_fctdata

## 单据体-子表 t_mrp_pur_fctentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_pur_fctentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpublished | 发布状态 | bpchar | 1 |  | √ | '0' | 发布状态,枚举: 0 :未发布 1 :已发布 |
| 3 | foperator | 计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftotalqty | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fpublishtime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fremarks | 调整原因 | varchar | 255 |  | √ | ' ' | 调整原因 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsplittime | 拆分时间 | timestamp | 0 |  |  | null | 拆分时间 |
| 12 | fplantag | 计划标识 | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdateqty_tag | 日期数量信息_详情 | text | 0 |  |  | null | 日期数量信息_详情 |
| 15 | fsplited | 拆分状态 | varchar | 10 |  | √ | ' ' | 拆分状态,枚举: Y :已拆分 N :未拆分 D :拆分中 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fdateqty | 日期数量信息 | varchar | 255 |  | √ | ' ' | 日期数量信息 |
| 18 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fpublisher | 发布者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fwasteqty | 三品仓库 | numeric | 23 | 10 | √ | 0 | 三品仓库 |
| 21 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: A :系统输出 B :发布数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_pur_fctentry |  | fid,fseq |
| 2 | pk_t_mrp_pur_fctentry |  | fentryid |

---

## 采购预测单-主表 t_mrp_pur_fctdata

- **表名称：** 采购预测单-主表
- **表名：** t_mrp_pur_fctdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fdateinfo_tag | 日期信息_详情 | text | 0 |  |  | null | 日期信息_详情 |
| 4 | fplangramid | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案 |
| 5 | fdateinfo | 日期信息 | varchar | 255 |  | √ | ' ' | 日期信息 |
| 6 | fcaculatelog | 计划运算号 | varchar | 255 |  | √ | ' ' | 计划运算号 |
| 7 | fis_latest_data | 是否最新版本数据 | bpchar | 1 |  | √ | '0' | 是否最新版本数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_pur_fctdata_p |  | fplangramid |
| 2 | pk_t_mrp_pur_fctdata |  | fid |
| 3 | idx_mrp_pur_fctdata_v |  | fis_latest_data |
| 4 | idx_mrp_pur_fctdata |  | fcaculatelog |
