# 定标金额-pds_conformamount

## 定标金额分录-子表 t_pds_conformamountentry

- **表名称：** 定标金额分录-子表
- **表名：** t_pds_conformamountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 3 | fparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 4 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsysresultid | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 7 | famount | 定标金额 | numeric | 23 | 10 | √ | 0 | 定标金额 |
| 8 | fdescription | 检查情况 | varchar | 255 |  | √ | ' ' | 检查情况 |
| 9 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 12 | fpreamount | 项目预估金额 | numeric | 23 | 10 | √ | 0 | 项目预估金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformamountentry_pro |  | fprojectid |
| 2 | idx_pds_conformamountentry_pid |  | fparentid |
| 3 | pk_pds_conformamountentry |  | fentryid |
| 4 | idx_pds_conformamountentry_fid |  | fid |

---

## 定标金额-主表 t_pds_conformamount

- **表名称：** 定标金额-主表
- **表名：** t_pds_conformamount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 3 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 4 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformamount_pid |  | fparentid |
| 2 | pk_pds_conformamount |  | fid |
