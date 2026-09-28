# 税务一般折旧-tdm_tax_depreciation

## 税务一般折旧-主表 t_tdm_tax_depreciation

- **表名称：** 税务一般折旧-主表
- **表名：** t_tdm_tax_depreciation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 3 | fcalctaxbase | 计税基础 | numeric | 23 | 10 | √ | 0 | 计税基础 |
| 4 | ftaxresidualvalue | 税务预计净残值 | numeric | 23 | 10 | √ | 0 | 税务预计净残值 |
| 5 | ftaxassetcategory | 税务资产类别 | varchar | 100 |  | √ | ' ' | 税务资产类别 |
| 6 | fmodifier | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 8 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 10 | ftaxyearamount | 税务一般本年折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务一般本年折旧摊销额 |
| 11 | ftaxcumulativeamount | 税务一般累计折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务一般累计折旧摊销额 |
| 12 | fext | fext | varchar | 50 |  |  | null |  |
| 13 | ftaxamortizationmethod | 税务一般折旧摊销方法 | varchar | 50 |  | √ | ' ' | 税务一般折旧摊销方法 |
| 14 | fassetcode | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
| 15 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统同步 import :模板引入 sysgen :系统生成 |
| 16 | ftaxcurrentamount | 税务一般当期折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务一般当期折旧摊销额 |
| 17 | ftaxamortizationperiods | 税务一般折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务一般折旧摊销期数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tax_depreciation_1 |  | fassetcode,faccountingperiod,forg |
| 2 | idx_tdm_tax_depreciation_0 |  | forg |
| 3 | pk_tdm_tax_depreciation |  | fid |
