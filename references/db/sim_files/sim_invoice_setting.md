# 销方地址电话-sim_invoice_setting

## 销方地址电话-主表 t_sim_invoice_setting

- **表名称：** 销方地址电话-主表
- **表名：** t_sim_invoice_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 3 | finvoiceaddr | 地址电话 | varchar | 100 |  | √ | ' ' | 地址电话 |
| 4 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 5 | ftaxno | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 6 | fopenuserbank | 开户行及账号 | varchar | 100 |  | √ | ' ' | 开户行及账号 |
| 7 | fbankaccount | fbankaccount | varchar | 50 |  | √ | ' ' |  |
| 8 | ffilter | 匹配规则 | varchar | 255 |  | √ | ' ' | 匹配规则 |
| 9 | fshopno | 店铺编号 | varchar | 30 |  | √ | ' ' | 店铺编号 |
| 10 | ffilter_tag | 匹配规则_详情 | text | 0 |  |  | null | 匹配规则_详情 |
| 11 | fshopreferred | 店铺简称 | varchar | 50 |  | √ | ' ' | 店铺简称 |
| 12 | fischeck | 是否默认选中 | varchar | 8 |  | √ | ' ' | 是否默认选中,枚举: 0 :否 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_invoice_setting |  | ftaxno |
| 2 | pk_sim_invoice_setting |  | fid |
