# 发票回调配置-ar_invoiceconfig

## 发票回调配置-主表 t_ar_invoicecfg

- **表名称：** 发票回调配置-主表
- **表名：** t_ar_invoicecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 结果文本 | varchar | 255 |  | √ | ' ' | 结果文本 |
| 3 | floginaddr | 苍穹登陆地址 | varchar | 100 |  | √ | ' ' | 苍穹登陆地址 |
| 4 | floginname | 登陆用户名/手机号 | varchar | 30 |  | √ | ' ' | 登陆用户名/手机号 |
| 5 | fmessage_tag | 结果文本_详情 | text | 0 |  |  | null | 结果文本_详情 |
| 6 | fappid | 第三方应用 | int8 | 64 |  | √ | 0 | [第三方应用（废弃） open_3rdapps](../open_files/open_3rdapps.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_ic_floginname |  | floginname |
| 2 | t_ar_invoicecfg_pkey |  | fid |

---

## 单据体-子表 t_ar_invoicecfgentry

- **表名称：** 单据体-子表
- **表名：** t_ar_invoicecfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfigid | 发票云配置 | int8 | 64 |  | √ | 0 | [发票云配置 er_bd_kdinvoicecloudcfg](../basedata_files/er_bd_kdinvoicecloudcfg.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | frevenuenumber | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_invoicecfgentry_pkey |  | fentryid |
| 2 | idx_ar_ice_configid |  | fconfigid |
