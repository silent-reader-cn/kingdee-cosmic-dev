# 供应商ABC-pm_supplier_abc_data

## 供应商ABC-主表 t_pm_supplierabc

- **表名称：** 供应商ABC-主表
- **表名：** t_pm_supplierabc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsuppliernumber | 供应商编码 | varchar | 100 |  | √ | ' ' | 供应商编码 |
| 3 | fpurproportion | 采购比例 | numeric | 23 | 10 | √ | 0 | 采购比例 |
| 4 | fgroup | ABC分类 | bpchar | 1 |  | √ | ' ' | ABC分类 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 7 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 8 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pm_supplierabc_supid |  | fsupplierid |
| 2 | pk_t_pm_supplierabc |  | fid |
