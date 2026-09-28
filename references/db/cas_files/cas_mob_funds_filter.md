# 币别组织筛选-cas_mob_funds_filter

## 币别组织筛选-主表 t_cas_fundsmobfilter

- **表名称：** 币别组织筛选-主表
- **表名：** t_cas_fundsmobfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrencyld | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fmulbasedataorg | 组织 | varchar | 4000 |  | √ | ' ' | 组织 |
| 4 | fprivacypolicy | 是否签署隐私协议 | varchar | 10 |  | √ | '0' | 是否签署隐私协议,枚举: 1 :已勾选 0 :未勾选 |
| 5 | fprivacypolicynumber | 隐私协议版本号 | varchar | 200 |  |  | null | 隐私协议版本号 |
| 6 | fuserid | 用户id | varchar | 255 |  | √ | ' ' | 用户id |
| 7 | fcombofield | 选择币种类型 | varchar | 10 |  | √ | ' ' | 选择币种类型,枚举: base :本位币 report :报告币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_fundsmobfilter |  | fuserid |
| 2 | pk_t_cas_fundsmobfilter |  | fid |
